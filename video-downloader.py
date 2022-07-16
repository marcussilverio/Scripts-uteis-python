import pytube
url = input("Enter url video: ")
path = 'D:\Videos\Youtube'
pytube.YouTube(url).streams.get_highest_resolution().download(path)
