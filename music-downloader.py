import pytube
url = input("Enter video url: ")
path = 'D:\Musicas'
pytube.YouTube(url).streams.get_audio_only().download(path)