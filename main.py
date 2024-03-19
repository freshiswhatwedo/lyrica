import lyricsgenius

token = "SJgV3xqS7Lim040mG6wG0e5pJAX6LrSZ4UIod4Dm392eBtALTyfVF18scCWbwMEP"
genius = lyricsgenius.Genius(token)

#artist = genius.search_artist("Andmax", max_songs=3, sort="title")
#print(artist)
#print("split")
#print(artist.songs)

#song = genius.search_song("haunt u", "lil peep")
#print(song.lyrics)

def lyricFinder(Song,Artist):{
     song = genius.search_song(Song, Artist)
     return song.lyrics

}
Lyrics = lyricFinder("Carnival","Kanye west")

print(Lyrics)
   

