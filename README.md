# Indian Sign Language to Text/Speech Translation using YOLOv5
Project Overview
This project develops a real-time Indian Sign Language (ISL) to Text/Speech Translation System using the YOLOv5 object detection algorithm. The system aims to bridge the communication gap between deaf individuals using ISL and hearing individuals by translating ISL gestures into text or speech. It leverages YOLOv5 for accurate and efficient hand gesture detection, combined with computer vision and natural language processing (NLP) techniques to enable seamless, real-time communication.
The system is trained on a self-developed dataset containing digits (0-9), alphabets (A-Z), and 50 predefined ISL words. YOLOv5's robust object detection capabilities allow for high-precision recognition of hand gestures, achieving an accuracy of 92.5% in real-time applications. The system supports two-way communication, multilingual audio input, and is designed for deployment in public spaces, educational settings, and mobile applications.
Features

Real-Time Gesture Detection: Uses YOLOv5 to detect ISL gestures with high accuracy and minimal latency.
Two-Way Communication: Supports ISL-to-text/audio and speech-to-ISL translation.
Multilingual Support: Processes audio inputs in multiple Indian languages (e.g., Hindi, Tamil, Telugu).
User-Friendly Interface: Designed for accessibility in public spaces, classrooms, and mobile platforms.
Comprehensive ISL Dataset: Includes a diverse dataset of ISL gestures for numbers, alphabets, and words.
Speech Output: Converts recognized gestures to speech using the Pyttsx3 library.

Installation
To set up the project locally, follow these steps:
Prerequisites

Python 3.8+
Libraries: PyTorch, OpenCV, NumPy, Pyttsx3, Matplotlib
Hardware: Webcam for gesture capture, optional GPU for faster training/inference
Dataset: Custom ISL dataset (available in the repository or can be recreated as described)

Steps

Clone the Repository:
git clone https://github.com/IndupuriMohan/Indian-Sign-Language-to-Text-Speech-Translation-Using-YOLO-Algorithm.git
cd isl-translation-system


Install Dependencies:
pip install -r requirements.txt

Ensure PyTorch is installed with GPU support if available (see PyTorch installation guide).

Install YOLOv5:Clone the YOLOv5 repository and install its dependencies:
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..


Download the Dataset:

The dataset is included in the data/ directory or can be recreated as described in the Dataset section.
Ensure the dataset follows YOLOv5's required format (e.g., images and labels in images/ and labels/ folders).


Download Pre-trained YOLOv5 Weights:

Use pre-trained YOLOv5 weights (e.g., yolov5s.pt) from the YOLOv5 repository.
Place the weights in the yolov5/weights/ directory.


Run the Application:
pythonrun2.py



Usage

Gesture Capture:

Use a webcam to capture ISL gestures in real-time.
Ensure proper lighting and a plain background for optimal YOLOv5 performance.


Gesture Detection with YOLOv5:

YOLOv5 processes video frames to detect and classify ISL gestures.
Outputs are mapped to corresponding text labels or speech using Pyttsx3.


Speech-to-ISL Translation:

Input audio via a microphone, transcribed using Automatic Speech Recognition (ASR).
A Seq2Seq model with attention mechanism translates text to ISL gestures, displayed as animations or images.


Customization:

Adjust detection confidence thresholds or gesture speed via the configuration file (config.yaml).
Modify language preferences or regional ISL variations through the user interface.



Dataset
The dataset is a self-collected set of 7800 images covering:

Digits: 0-9
Alphabets: A-Z
Words: 50 predefined ISL signs
Image Details:
Resolution: 4000x3000 pixels (resized to 80x60 for processing)
Format: RGB, converted to HSV for preprocessing
Split: ~5500 training, 1180 validation, 1160 test images


Augmentation: Applied shearing, zoom, horizontal/vertical flips to enhance dataset diversity.
YOLOv5 Format: Images are annotated with bounding boxes and class labels compatible with YOLOv5 (e.g., .txt files in YOLO format).

The dataset structure is shown in the project report (Figure 4.2), with balanced class distribution (Figure 4.3).
Model Architecture
The system primarily uses YOLOv5 for gesture detection, with additional components for speech processing:

YOLOv5:
Variant: YOLOv5s (small) for efficient real-time detection
Input: 80x60x3 (HSV images)
Output: Bounding boxes and class probabilities for ISL gestures (26 alphabets + 50 words + 10 digits)
Training: Fine-tuned on the custom ISL dataset for 25 epochs


Seq2Seq with Attention:
Used for speech-to-ISL translation
Encoder: LSTM/GRU for processing speech/text
Decoder: Generates ISL gesture sequences with attention mechanism


Preprocessing:
Images are resized to 80x60 and converted to HSV color space.
Augmentation techniques (shearing, zoom, flips) enhance model robustness.



Performance

Accuracy: 92.5% for gesture recognition using YOLOv5
Real-Time Latency: ~1-2 seconds for audio-to-ISL translation
Multilingual Support: 80-88% accuracy across Hindi, Tamil, Telugu, and English
Two-Way Communication: 75% accuracy for ISL-to-text/audio translation
Challenges:
Background noise reduces audio processing accuracy (60-70% in noisy environments)
Complex or fast gestures may lower detection accuracy



Results

Gesture Detection: YOLOv5 achieves high accuracy for static and dynamic ISL gestures.
Real-Time Performance: Suitable for live events, classrooms, and public spaces.
User Feedback: Positive response for usability and gesture clarity, with requests for offline mode and expanded language support.
Dataset Contribution: A comprehensive ISL dataset for future research in sign language recognition.

Future Work

Improve background subtraction for complex environments using advanced preprocessing.
Enhance gesture detection in low-light conditions.
Expand the ISL dataset to include more regional variations and complex sentences.
Develop a mobile application for broader accessibility.
Integrate noise-cancellation techniques for robust audio processing.
Support bidirectional translation with improved NLP for contextual understanding.

References
The project references are listed in the full report (FIRST_REPORT.docx). Key citations include:

Sun et al. (2013) on Kinect-based sign language recognition.
Chen et al. (2003) on gesture recognition using Hidden Markov Models.
Ultralytics YOLOv5 documentation for object detection implementation.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments
This project was developed to promote inclusive communication for the deaf community in India. We acknowledge the contributions of all team members and the guidance provided by referenced studies and the YOLOv5 framework by Ultralytics.
