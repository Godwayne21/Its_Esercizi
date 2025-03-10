def make_album(artist_name, album_title, num=None)-> dict[str,str]:

    dict_album = {'name': artist_name, 'title': album_title}

    if num:

        dict_album ['num'] = num

while True:

    artist_name = str(input("What's the name? (insert 'exit' to quit)"))

    if artist_name == 'exit':

        break

    album_title = str(input("What's the album? (insert 'exit' to quit)"))
    if album_title == 'exit':

        break

    num = str(input("What's the song? (insert 'exit' to quit)"))    
    if num == 'exit':

        break

album = make_album(artist_name,album_title,num)

print(album)