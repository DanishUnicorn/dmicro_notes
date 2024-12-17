import speech_recognition as sr
from pydub import AudioSegment

# Path to .m4a file
audio_file_path = "/Users/bruger/Desktop/Folders/KU/Master/year_1/blok_2/DM/DMnotes/dairy_microbiology/Lecture_memos/L13/slide_34-36.m4a"

try:
    # Convert from .m4a to .wav
    audio = AudioSegment.from_file(audio_file_path, format="m4a")
    audio.export("converted.wav", format="wav")

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the .wav file
    with sr.AudioFile("converted.wav") as source:
        audio_data = recognizer.record(source)

    # Recognize speech
    text = recognizer.recognize_google(audio_data)
    print("Transcription:", text)

except sr.RequestError as e:
    print(f"Could not request results from the speech recognition service; {e}")
except sr.UnknownValueError:
    print("Speech recognition could not understand the audio")
except Exception as e:
    print(f"An error occurred: {e}")

# You can now copy paste into a .txt file