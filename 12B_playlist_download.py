from pytube import Playlist
py = Playlist("https://youtu.be/n9vuTrR7Z6M?t=38")
print(f'Downloading : {py.title}')
for video in py.videos:
    video.streams.first().download()
