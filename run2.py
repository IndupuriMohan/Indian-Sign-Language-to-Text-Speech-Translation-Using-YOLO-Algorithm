from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import numpy as np
import tempfile

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
