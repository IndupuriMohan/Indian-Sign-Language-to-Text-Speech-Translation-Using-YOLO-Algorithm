import streamlit as st
import os
from PIL import Image, ImageOps
import warnings
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import numpy as np
import speech_recognition as sr
import tempfile

warnings.filterwarnings("ignore")

image_dir = "images/"
target_size = (150, 150)

st.title("Simple Sign Language Image Viewer")

if 'text_input' not in st.session_state:
    st.session_state.text_input = ''

# ========== WebRTC-based Microphone Input ==========
class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio_data = []

    def recv(self, frame):
        audio_bytes = frame.to_ndarray().tobytes()
        self.audio_data.append(audio_bytes)
        return frame

    def get_audio_text(self):
        audio_bytes_combined = b''.join(self.audio_data)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio_bytes_combined)
            f.flush()
            with sr.AudioFile(f.name) as source:
                audio = self.recognizer.record(source)
                try:
                    return self.recognizer.recognize_google(audio)
                except Exception as e:
                    return f"Speech recognition error: {e}"

processor = AudioProcessor()
ctx = webrtc_streamer(key="speech", audio_processor_factory=lambda: processor, media_stream_constraints={"audio": True, "video": False})

if ctx.audio_processor:
    if st.button("Transcribe"):
        result = ctx.audio_processor.get_audio_text()
        st.session_state.text_input = result
        st.write(f"You said: {result}")

# ========== Image Display Function ==========
def show_images(text):
    images = [f"{image_dir}{char}.jpg" for char in text.lower() if os.path.exists(f"{image_dir}{char}.jpg")]
    if not images:
        st.write("No images found for that input.")
        return

    if 'current_image_index' not in st.session_state:
        st.session_state.current_image_index = 0

    num_images = len(images)

    if num_images > 0:
        col1, col2, col3 = st.columns((1, 4, 1))

        if col1.button("<--"):
            st.session_state.current_image_index = (st.session_state.current_image_index - 1) % num_images

        try:
            img = Image.open(images[st.session_state.current_image_index])
            img = img.resize(target_size, Image.Resampling.LANCZOS)
            img = ImageOps.expand(img, border=(10, 10, 10, 10), fill="white")
            col2.image(img, use_column_width=True, caption=f"Image {st.session_state.current_image_index + 1}/{num_images}")
        except Exception as e:
            col2.error(f"Error displaying image: {e}")

        if col3.button("-->"):
            st.session_state.current_image_index = (st.session_state.current_image_index + 1) % num_images

# Show images based on speech input
show_images(st.session_state.text_input)
