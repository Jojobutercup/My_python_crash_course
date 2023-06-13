def make_album(artistName, albumTitle, numSongsInAlbum=None):
    artistInfo = {
    'name': artistName,
    'album': albumTitle,
    }
    if numSongsInAlbum:
        artistInfo['numSongsInAlbum'] = numSongsInAlbum

    prompt = "please enter your favourite artist and their album"
    prompt += "\nThis will help us recommend musics to you"
    prompt += "\nAritist Name: "

    while True:
        polledArtist = input(f"{prompt} (enter 'q' to quit): ")
        if polledArtist == 'q':
            break
        polledAlbum = input("Artist Album (enter 'q' to quit): ")
        if polledAlbum == 'q':
            break
        artistInfo['polledArtist'] = polledArtist
        artistInfo['polledAlbum'] = polledAlbum

    return artistInfo

storedInfo = make_album('davido', 'timeless',  numSongsInAlbum= 10)
storedInf = make_album('davido', 'timeless')
print(storedInfo)
print(storedInf)
