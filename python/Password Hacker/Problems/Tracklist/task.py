def tracklist(**kwargs):
    for artist, albums in kwargs.items():
        print(artist)
        for k, v in albums.items():
            print('ALBUM:', k, 'TRACK:', v)
