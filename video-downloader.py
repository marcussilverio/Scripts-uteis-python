import pytube
url = input("Enter video url: ")
path = 'D:\Videos\Youtube'
pytube.YouTube(url).streams.get_highest_resolution().download(path)
