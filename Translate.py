from deep_translator import GoogleTranslator


def split_text(text, max_length=5000):
    chunks = []
    current_chunk = []
    current_length = 0

    for word in text.split():
        if current_length + len(word) + 1 > max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1
        else:
            current_chunk.append(word)
            current_length += len(word) + 1

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


# Read the Spanish transcription from the file
with open("transcription_spanish.txt", "r") as f:
    spanish_text = f.read()

# Split the Spanish text into smaller chunks
chunks = split_text(spanish_text)

# Ensure all chunks are within the valid length
for chunk in chunks:
    assert len(chunk) <= 5000, f"Chunk length exceeds 5000 characters: {len(chunk)}"

# Translate each chunk and combine the results
translated_chunks = [GoogleTranslator(source='auto', target='en').translate(chunk) for chunk in chunks]
translated_text = ' '.join(translated_chunks)

# Print the translated text
print(translated_text)

# Store in file
with open("transcription_english_translated.txt", "w") as f:
    f.write(translated_text)
