from pytube import YouTube, streams, Playlist


def baixar_video(link):

    yt = YouTube(link)
    print('baixando...')
    ys = yt.streams.get_highest_resolution().download()
    print('Sucesso.')


def baixar_playlist(link):

    yt = Playlist(link)
    print('baixando...')
    for url in yt:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path='playlist')
    print('Sucesso.')


if __name__ == '__main__':

    link = input('Insira o link ')
    tipo = int(input(' digite 0 para video unico ou 1 pra playlist '))

    if tipo == 0:
        baixar_video(link)
    else:
        baixar_playlist(link)
