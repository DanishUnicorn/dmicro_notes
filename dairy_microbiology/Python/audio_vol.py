from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("/Users/bruger/Desktop/Folders/KU/Master/year_1/blok_2/DM/DMnotes/dairy_microbiology/Lecture_memos/L13/slide_37-55.m4a", format="m4a")

# Increase volume by 10 dB (adjust value as needed)
louder_audio = audio + 10  # You can also use negative values to decrease volume

# Export the modified audio file
louder_audio.export("/Users/bruger/Desktop/Folders/KU/Master/year_1/blok_2/DM/DMnotes/dairy_microbiology/Lecture_memos/L13/slide_37-55_pDB.wav", format="wav")

print("Volume adjustment complete. File saved as output.m4a.")
