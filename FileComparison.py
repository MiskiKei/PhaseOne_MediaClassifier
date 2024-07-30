import difflib
import openai
import os


# Load the text from the files
with open('transcription_english_translated.txt', 'r') as file1:
    text1 = file1.read()

with open('transcription_english.txt', 'r') as file2:
    text2 = file2.read()

matcher = difflib.SequenceMatcher(None, text1, text2)

# Get the similarity ratio
similarity_ratio = matcher.ratio()

print(f'Similarity ratio: {similarity_ratio * 100:.2f}%')


# Initialize the OpenAI client with the API key from the environment variable
openai.api_key = ("sk-None-TLCg5QcUvBkbUTUD97L3T3BlbkFJRXg5BnJ2uz1mISptqmfw")

# Read the content of the two files
with open("transcription_english_translated.txt", "r") as file1, open("transcription_english.txt", "r") as file2:
    text1 = file1.read()
    text2 = file2.read()

# Prepare the messages for the chat completion
messages = [
    {"role": "system", "content": "You are a kind and helpful assistant."},
    {"role": "user", "content": f"Compare these two texts for similarity:\n\nText 1:\n{text1}\n\nText 2:\n{text2}"}
]

# Call the OpenAI API to compare the texts
try:
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    # Extract and print the reply
    reply = chat_completion['choices'][0]['message']['content']
    print(f"ChatGPT: {reply}")
except Exception as e:
    print(f"An error occurred: {e}")