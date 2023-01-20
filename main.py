from pytube import YouTube, streams


link = input('Insira o link')
yt = YouTube(link)
ys = yt.streams.get_highest_resolution().download()


