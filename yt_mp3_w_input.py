import os
from pytube import YouTube
from moviepy.editor import *
import argparse
import shutil

# Set up argparse to take in command line arguments
# parser = argparse.ArgumentParser(description='Download a YouTube video as an MP3 file')
# parser.add_argument('link', type=str, help='YouTube video link')
# parser.add_argument('filename', type=str, help='Output file name')
# args = parser.parse_args()

link = str(input("Input your yt link here: "))
# create a YouTube object
yt = YouTube(link)

# get the highest quality audio stream
audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

# download the audio stream
audio_stream.download()

# create an AudioFileClip object from the downloaded file
audio_file_path = audio_stream.default_filename
audio_clip = AudioFileClip(audio_file_path)

filename = str(input("Input your music name here: "))
# write the audio clip to an MP3 file
mp3_file_path = f"{filename}.mp3"
audio_clip.write_audiofile(mp3_file_path)

# close the audio clip
audio_clip.close()

# remove the video file
os.remove(audio_file_path)

destiny = str(input("Input your file destiny here: "))
# move the MP3 file to the Music directory
shutil.move(mp3_file_path, destiny)