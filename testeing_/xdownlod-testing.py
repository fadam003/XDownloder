import pafy
from hurry.filesize import size
video = pafy.new('https://www.youtube.com/watch?v=B_VeP1S-T8Q&start_radio=1&list=RDB_VeP1S-T8Q')

print(video.title)
print(video.thumb)
streams = video.streams
for s in streams:
    print(s.get_filesize())