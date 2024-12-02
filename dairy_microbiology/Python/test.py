import os
from pydub import AudioSegment
import speech_recognition as sr

# Function to convert M4A to WAV
def convert_m4a_to_wav(m4a_file):
    audio = AudioSegment.from_file(m4a_file, format='m4a')
    wav_file = m4a_file.replace('.m4a', '.wav')
    audio.export(wav_file, format='wav')
    return wav_file

# Function to transcribe audio
def transcribe_audio(wav_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)  # read the entire audio file
        try:
            text = recognizer.recognize_google(audio_data)  # use Google Web Speech API
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

# Main function
def main():
    m4a_file = '/Users/bruger/Desktop/Folders/KU/Master/year_1/blok_2/DM/DMnotes/dairy_microbiology/Lecture_memos/test.m4a'  # Replace with your M4A file path
    wav_file = convert_m4a_to_wav(m4a_file)
    transcription = transcribe_audio(wav_file)
    print("Transcription:")
    print(transcription)

    # Clean up the WAV file if desired
    os.remove(wav_file)

if __name__ == "__main__":
    main()