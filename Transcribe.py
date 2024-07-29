import whisper
import ssl
import warnings

# Bypass SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Suppress the specific warning
warnings.filterwarnings("ignore", category=FutureWarning, module='whisper')


def transcribe_audio(model, input_file, output_file):
    try:
        print(f"Transcribing {input_file}...")
        # Transcribe the audio file
        result = model.transcribe(input_file, fp16=False)
        # Write the transcription to a file
        with open(output_file, "w") as f:
            f.write(result["text"])
        print(f"Transcription for {input_file} saved to {output_file}")
    except Exception as e:
        print(f"Error transcribing {input_file}: {e}")


def main():
    try:
        # Load the Whisper model
        print("Loading Whisper model...")
        model = whisper.load_model("base")
        print("Model loaded successfully.")

        # Transcribe and save the English audio file
        transcribe_audio(model, "output_english.mp4", "transcription_english.txt")

        # Transcribe and save the Spanish audio file
        transcribe_audio(model, "output_spanish.mp4", "transcription_spanish.txt")


    except Exception as e:
        print(f"Error loading model or transcribing audio: {e}")


if __name__ == "__main__":
    main()
