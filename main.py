import lyricsgenius

token = "SJgV3xqS7Lim040mG6wG0e5pJAX6LrSZ4UIod4Dm392eBtALTyfVF18scCWbwMEP"
genius = lyricsgenius.Genius(token)

artist = genius.search_artist("Andmax", max_songs=3, sort="title")
print(artist)
print("")
print(artist.songs)

