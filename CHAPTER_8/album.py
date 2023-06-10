def make_album(artist_name, album_title, number_of_songs =None):
    """dictionary that represnets artist and their albums"""
    artist_info = {'name': artist_name, 'album': album_title}
    if number_of_songs:
        artist_info['number_of_song'] = number_of_songs
    return artist_info

full_info = make_album('davido', 'timeless')
full_info1 = make_album('osas', 'forever', number_of_songs = 7)
full_info2 = make_album('burna boy', 'timeflies')
print(full_info)
print(full_info1)
print(full_info2)
