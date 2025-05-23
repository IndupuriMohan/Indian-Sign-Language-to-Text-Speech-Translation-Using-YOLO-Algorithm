# Indian-Sign-Language-to-Text-Speech-Translation-Using-YOLO-Algorithm

Overview

This project implements a system to translate Indian Sign Language (ISL) gestures into text and synthesized speech in real-time. Utilizing a YOLO-based object detection model for hand gesture recognition and a text-to-speech engine, the system bridges the communication gap between deaf or hard-of-hearing individuals and those who communicate via spoken language.

Key features:

Real-time Gesture Detection: Uses YOLO to detect and classify ISL hand gestures from a live webcam feed.

Text & Speech Output: Converts recognized gestures into text and generates corresponding speech using Python’s pyttsx3 library.

End-to-End Pipeline: Incorporates image acquisition, preprocessing, model inference, and output rendering.

Repository Structure

├── data/                   # Dataset and annotations (data.yaml)
├── runs/                   # Training and detection logs
│   └── detect/train/       # Training arguments and results
├── train/                  # YOLO training artifacts
│   └── labels/             # Ground truth labels for training
├── src/                    # Source code
│   ├── detect.py           # YOLO detection script
│   ├── train.py            # YOLO training script
│   └── gesture_to_speech.py# Gesture-to-text/speech conversion module
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
└── .gitignore              # Files and folders to ignore

Installation

Clone the repository

git clone https://github.com/IndupuriMohan/Indian-Sign-Language-to-Text-Speech-Translation-Using-YOLO-Algorithm.git
cd Indian-Sign-Language-to-Text-Speech-Translation-Using-YOLO-Algorithm

Create a virtual environment

python -m venv venv
source venv/bin/activate     # On Windows: venv\\Scripts\\activate

Install dependencies

pip install -r requirements.txt

Usage

1. Train the YOLO model

python src/train.py --data data/data.yaml --cfg yolov5s.yaml --epochs 25 --batch-size 16

data.yaml: Dataset configuration (classes and paths)

yolov5s.yaml: Model configuration file

2. Detect gestures in real-time

python src/detect.py --weights runs/train/exp/weights/best.pt --source 0

--source 0: Use default webcam input.

3. Convert detected gestures to speech

The detect.py script automatically calls gesture_to_speech.py upon recognizing a gesture, converting it into text display and spoken output.

Dataset

The dataset consists of 7800 self-collected images covering:

Digits 0-9

Alphabets A-Z

50 pre-defined sign words

Images are split into train, val, and test sets.

Preprocessing includes resizing to 80×60 pixels and color-space conversion (RGB → HSV).

Model Architecture

YOLOv5 object detection for locating hand regions.

CNN classifier (ResNet-50 / VGG-19 / AlexNet via transfer learning) for gesture classification.

GANs (DCGAN / SRGAN) used to augment and generate synthetic sign images.

Results

Recognition Accuracy: Up to 92.5% on static gesture classification.

Real-time Latency: Approximately 1-2 seconds per detection and conversion.

Acknowledgements

Dr. Smitha Patil, Assistant Professor, Presidency University, for project guidance.

Presidency University School of CSE for support and infrastructure.

Dataset contributors: M. Venkata Subhash, CH Thiru Mohith, P. Chakradhar Rao, I. Mohan Vamsi.

License

This project is licensed under the MIT License.

