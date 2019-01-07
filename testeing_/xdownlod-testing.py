import pafy
from hurry.filesize import size
video = pafy.new(Youtubeurl)

print(video.title)
print(video.thumb)
streams = video.streams
for s in streams:
    print(size(s.get_filesize())) #gives us the size of the videos in M
