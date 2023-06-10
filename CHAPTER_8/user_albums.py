def make_album(artist_name, album_title, number_of_songs =None):
    """dictionary that represnets artist and their albums"""
    artist_info = {'name': artist_name, 'album': album_title}
    if number_of_songs:
        artist_info['number_of_song'] = number_of_songs
    return artist_info

while True:
    print("Please enter your favourite artist name and title")
    artistName = input("artist full name?: ")
    if artistName == 'quit':
        break
    album_title = input("Artist released album: ")
    if album_title == 'quit':
        break

    full_info = make_album(artistName, album_title)
    print(full_info)

full_info0 = make_album('davido', 'timeless')
full_info1 = make_album('osas', 'forever', number_of_songs = 7)
full_info2 = make_album('burna boy', 'timeflies')

print(full_info0)
print(full_info1)
print(full_info2)
