import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from pydub.silence import detect_nonsilent

# Paths for input and output
input_audio_path = "/Users/bruger/Desktop/Folders/KU/Master/year_1/blok_2/DM/DMnotes/dairy_microbiology/Lecture_memos/L13/slide_34-36.m4a"
output_folder = "/Users/bruger/Desktop/Folders/KU/Master/year_1/blok_2/DM/DMnotes/dairy_microbiology/Lecture_memos/Processed_Files"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Define paths for intermediate files
converted_wav_path = os.path.join(output_folder, "converted.wav")
transcription_path = os.path.join(output_folder, "transcription.txt")

# Customizable chunk length in milliseconds
chunk_length_ms = 15000  # 15 seconds per chunk

try:
    # Step 1: Enhance audio volume and normalize
    print("Enhancing audio volume and normalizing...")
    audio = AudioSegment.from_file(input_audio_path, format="m4a")
    louder_audio = audio + 10  # Increase volume
    normalized_audio = louder_audio.normalize()

    # Step 2: Export the enhanced audio as .wav
    print("Converting to .wav format...")
    normalized_audio.export(converted_wav_path, format="wav")
    print(f"Converted file saved to: {converted_wav_path}")

    # Step 3: Split audio into chunks
    print("Splitting audio into chunks...")
    chunks = make_chunks(normalized_audio, chunk_length_ms)

    recognizer = sr.Recognizer()
    all_text = ""

    for i, chunk in enumerate(chunks):
        # Remove silence from the chunk
        nonsilent_ranges = detect_nonsilent(chunk, min_silence_len=500, silence_thresh=-40)
        for start, end in nonsilent_ranges:
            chunk = chunk[start:end]

        chunk_file = os.path.join(output_folder, f"chunk_{i + 1}.wav")
        chunk.export(chunk_file, format="wav")
        print(f"Processing chunk {i + 1}/{len(chunks)}...")

        with sr.AudioFile(chunk_file) as source:
            audio_data = recognizer.record(source)

        try:
            # Recognize speech for each chunk
            text = recognizer.recognize_google(audio_data, language="en-US")
            all_text += f"Chunk {i + 1}:\n{text}\n\n"
        except sr.UnknownValueError:
            print(f"Chunk {i + 1}: Could not understand the audio")
            all_text += f"Chunk {i + 1}: [Unintelligible]\n\n"
        except sr.RequestError as e:
            print(f"Chunk {i + 1}: Recognition connection failed: {e}")
            all_text += f"Chunk {i + 1}: [Connection failed]\n\n"

    # Step 4: Save transcription to a .txt file
    with open(transcription_path, "w") as file:
        file.write(all_text)
    print(f"Transcription saved to: {transcription_path}")

except Exception as e:
    print(f"An error occurred: {e}")
