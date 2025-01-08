from extract import extract_audio_streams
from fetch import fetch_youtube_page
from download import select_best_audio_stream , get_audio_url , download_audio
import subprocess

def convert_to_wav(input_path, output_path):
    """Convert the downloaded audio file to WAV format using FFmpeg."""
    try:
        result = subprocess.run(
            ["ffmpeg", "-i", input_path, "-ar", "44100", "-ac", "2", output_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print(f"FFmpeg output: {result.stdout.decode()}")
        print(f"FFmpeg error (if any): {result.stderr.decode()}")
        print(f"Converted to WAV: {output_path}")
    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)
        print(f"Error output: {e.stderr.decode()}")
        raise


video_url = "https://www.youtube.com/watch?v=gRgmVsjA7g0"

html = fetch_youtube_page(video_url)

audio_streams = extract_audio_streams(html)


if not audio_streams:
    print("No audio streams found!")
    exit()

# Select the best audio stream
best_stream = select_best_audio_stream(audio_streams)
print("Selected audio stream:", best_stream)

# Get the audio URL
try:
    audio_url = get_audio_url(best_stream)
    print("Audio URL:", audio_url)
except NotImplementedError as e:
    print("Decryption required:", e)
    exit()
except ValueError as e:
    print("Error retrieving audio URL:", e)
    exit()

# Download the audio stream
output_file = "output_audio.webm"
print(f"Downloading audio to {output_file}...")
temp_file = download_audio(audio_url, "temp_audio")
print(f"Downloaded temporary file: {temp_file}")

# Convert to WAV format
wav_file = "output_audio.wav"
convert_to_wav(temp_file, wav_file)

