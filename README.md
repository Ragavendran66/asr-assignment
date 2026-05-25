# Automatic Speech Recognition (ASR) using OpenAI Whisper

This project uses OpenAI Whisper to transcribe audio/video recordings into text and evaluate transcription accuracy using Word Error Rate (WER).

## Features

- Speech-to-text transcription using Whisper
- Supports MP4 and WAV files
- Batch processing of audio recordings
- CSV export of transcription results
- Accuracy evaluation using WER metric

## Technologies Used

- Python
- OpenAI Whisper
- Pandas
- JiWER
- FFmpeg

## Project Structure

```bash
asr-assignment/
│
├── audio/
├── outputs/
├── whisper_asr.py
├── metrics.py
├── ground_truth.csv
├── requirements.txt
└── report.md
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Install FFmpeg:

```bash
winget install ffmpeg
```

## Run Transcription

```bash
python whisper_asr.py
```

## Run Evaluation Metrics

```bash
python metrics.py
```

## Output

- Transcription CSV stored in:
  `output/whisper_output.csv`

- WER evaluation displayed in terminal.

## Sample Use Cases

- Noisy environment transcription
- Hinglish speech recognition
- Bangalore location-based speech samples
- ASR model evaluation

## Done by Ragavendran

Ragavendran R
