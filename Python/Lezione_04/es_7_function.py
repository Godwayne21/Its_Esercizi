def make_album(artist_name, album_title, num=None)-> dict[str,str]:

    dict_album = {'name': artist_name, 'title': album_title}

    if num:
        dict_album['num'] = num

    return dict_album

album1 = make_album("Elton", "Free", "Dive")
album2 = make_album("James", "Plus")
album3 = make_album("Ed", "Talker")

print(album1)
print(album2)
print(album3)