import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file = "/Users/bruger/Desktop/Folders/KU/Master/year_1/blok_2/DM/DMnotes/dairy_microbiology/Lecture_memos/test_03.m4a"

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Recognize speech using Sphinx (offline)
try:
    text = recognizer.recognize_sphinx(audio_data)
    print("Transcription: " + text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))