# Meeting Summary Generator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-%3E%3D3.12-blue.svg)](https://www.python.org/downloads/release)


This project is designed to help you easily create summaries of your group meetings using Python. It leverages the Whisper model for speech recognition and the Gemma model from Ollama for generating concise meeting summaries.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Features

- **Speech to Text**: Converts audio recordings of meetings into text using the Whisper model.
- **Text Summarization**: Generates concise summaries of meeting transcriptions using the Gemma model.
- **Flexible Output**: Save the transcriptions and summaries to specified directories for easy access.

## Requirements

- Python 3.12.4 or higher.
- Ollama serve models.
- Required Python packages:
  - `speechrecognition`
  - `ollama`
  - `openai-whisper`

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/franciscopalmeromoya/meeting-summaries.git
    cd meeting-summaries
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Install Whisper and Gemma models**:
    - Follow the official instructions for installing and setting up [Whisper](https://github.com/openai/whisper) .
    - Install the Ollama Gemma model as per the instructions provided on the [Ollama website](https://ollama.com/).

## Usage

### Speech to Text

Convert an audio file to text using the `speech2text.py` script.

```sh
python speech2text.py -a path/to/your/audio/file.wav -o path/to/output/directory -m base
```

- `-a`: Path to the audio file (required).
- `-o`: Path to the output directory (optional).
- `-m`: Whisper model to use (default is `base`).

### Generate Meeting Summary

Generate a summary from a text file using the `gemma.py` script.

```sh
python gemma.py -a path/to/your/transcription.txt -o path/to/output/directory -m general
```

- `-a`: Path to the text file (required).
- `-o`: Path to the output directory (optional).
- `-m`: Gemma prompt mode (default is `general`). Options are `general` and `key-takeaways`.

## Examples

### Example 1: Convert Audio to Text

```sh
python speech2text.py -a meeting_audio.wav -o transcriptions -m base
```

### Example 2: Generate Summary from Transcription

```sh
python gemma.py -a transcriptions/meeting_audio.txt -o summaries -m key-takeaways
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/MIT) website for details.
