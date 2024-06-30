import ollama
import argparse

# Initialize argument parser
parser = argparse.ArgumentParser(description="Generate a meeting summary using Gemma")
parser.add_argument('-a', type=str, required=True, help='Path to the text file')
parser.add_argument('-o', type=str, required=False, help='Path to the output directory')
parser.add_argument('-m', type=str, required=False, help="Select Gemma prompt mode. Default is 'general'")


# Parse arguments
args = parser.parse_args()
text_file_path = args.a
output_dir = args.o
if args.m is None:
    gemma_mode = "general"
else: 
    gemma_mode = args.m

with open(text_file_path, 'r') as text_file:
    content = text_file.read()

prompt = {
    "general": "Please provide a concise summary of the following meeting transcription. Highlight the main points discussed, key decisions made, and any action items assigned.",
    "key-takeaways" : "Summarize the following meeting transcription by listing the key takeaways, including important discussion points, decisions made, and any tasks or action items assigned to participants."
}

response = ollama.chat(model='gemma:7b', messages=[
  {
    'role': 'user',
    'content': prompt[gemma_mode] + "\n" + content,
  },
])
print(response['message']['content'])