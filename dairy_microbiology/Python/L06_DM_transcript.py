import speech_recognition as sr
from pydub import AudioSegment

# Path to your audio file
audio_file_path = "/Users/bruger/Desktop/Folders/KU/Master/year_1/blok_2/DM/DMnotes/dairy_microbiology/Lecture_memos/test.m4a"

try:
    # Convert the audio file to a format that the recognizer can understand
    audio = AudioSegment.from_file(audio_file_path, format="m4a")
    audio.export("converted.wav", format="wav")

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile("converted.wav") as source:
        audio_data = recognizer.record(source)

    # Recognize the speech in the audio file
    text = recognizer.recognize_google(audio_data)
    print("Transcription:", text)

except sr.RequestError as e:
    print(f"Could not request results from the speech recognition service; {e}")
except sr.UnknownValueError:
    print("Speech recognition could not understand the audio")
except Exception as e:
    print(f"An error occurred: {e}")