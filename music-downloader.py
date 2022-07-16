import pytube
import os
url = input("Enter url video: ")
path = 'D:\Musicas'
yt = pytube.YouTube(url)
out_file = yt.streams.get_audio_only().download(path)
base, ext = os.path.splitext(out_file)
new_file = base +'.mp3'
os.rename(out_file, new_file)
print(yt.title + " has been successfully downloaded.")