# Indian Sign Language to Text/Speech Translation Using YOLO Algorithm

## Overview
This project implements a system to translate Indian Sign Language (ISL) gestures into text and synthesized speech in real-time. Utilizing a YOLO-based object detection model for hand gesture recognition and a text-to-speech engine, the system bridges the communication gap between deaf or hard-of-hearing individuals and those who communicate via spoken language.

Key features:
- **Real-time Gesture Detection:** Uses YOLO to detect and classify ISL hand gestures from a live webcam feed.
- **Text & Speech Output:** Converts recognized gestures into text and generates corresponding speech using Python’s `pyttsx3` library.
- **End-to-End Pipeline:** Incorporates image acquisition, preprocessing, model inference, and output rendering.

## Repository Structure
