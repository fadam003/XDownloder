from django.shortcuts import render
import pafy
from hurry.filesize import size

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        video = pafy.new(url)
        title = video.title
        thumb = video.thumb
        streams = video.streams
        oursize = [size(s.get_filesize()) for s in streams]
        format = [s.extension for s in streams]
        quality = [s.quality[-3:] for s in streams]
        download = [s.url for s in streams]
        context = {
            'title': title,
            'thumb': thumb,
            'streams': zip(format,quality,download,oursize),
        }
        return render(request,'detail.html',context)
    return render(request,'home.html',{})


