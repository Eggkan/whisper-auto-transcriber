# 🎙️ Whisper Auto Transcriber

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![OpenAI](https://img.shields.io/badge/Model-OpenAI%20Whisper-green?style=flat-square)
![Automation](https://img.shields.io/badge/Category-Automation-orange?style=flat-square)

A lightweight Python automation script that converts audio files (MP3) into text (TXT) using OpenAI's state-of-the-art **Whisper** model. Designed to automate the transcription of lectures, meetings, and voice notes locally without needing cloud APIs.

---

## ⚡ Key Features

*   **Local Processing:** Runs entirely on your machine (Privacy-focused).
*   **High Accuracy:** Utilizes the `small` Whisper model for a balance between speed and precision.
*   **Multi-language Support:** Configured for Turkish (`tr`), but supports multilingual detection.
*   **Automatic Saving:** Generates a text file in the same directory as the source audio.

---

## 🛠 Prerequisites

Before running the script, ensure you have **FFmpeg** installed on your system, as it is required by Whisper for audio processing.

### 1. Install FFmpeg
*   **Windows:** `winget install ffmpeg` (or download from official site)
*   **Mac:** `brew install ffmpeg`
*   **Linux:** `sudo apt update && sudo apt install ffmpeg`

### 2. Install Python Packages
```bash
pip install openai-whisper

#1 Clone the repository:
git clone https://github.com/yourusername/whisper-auto-transcriber.git
#2 Run the script:
python ses_kaydi.py

### Notes
#Paste the file path of your MP3 file when prompted.
#The script will generate a _transkript.txt file in the same location.
