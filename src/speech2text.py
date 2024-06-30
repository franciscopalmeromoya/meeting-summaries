import speech_recognition as sr
import argparse
import os

# Initialize argument parser
parser = argparse.ArgumentParser(description="Speech to text using Whisper")
parser.add_argument('-a', type=str, required=True, help='Path to the audio file')
parser.add_argument('-o', type=str, required=False, help='Path to the output directory')
parser.add_argument('-m', type=str, required=False, help='Select Whisper model. Default is base')

# Parse arguments
args = parser.parse_args()
audio_file_path = args.a
output_dir = args.o
if args.m is not None:
    model = "base"
else:
    model = args.m

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the audio file as the audio source
with sr.AudioFile(audio_file_path) as source:
    audio = recognizer.record(source)  # Read the entire audio file

# Recognize speech using Whisper
try:
    print(f"Processing {os.path.basename(audio_file_path)} using Whisper {model} model...")
    text = recognizer.recognize_whisper(audio, model=model)
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print(f"Whisper error; {e}")
else: 
    print("Whisper thinks you said: " + text)
    if output_dir is not None:
        name = os.path.splitext(os.path.basename(audio_file_path))[0]
        with open(os.path.join(output_dir, f"{name}.txt"), 'w') as output_file:
            output_file.write(text)
    else:
        print("Please, provide an output directory to save the text.")

