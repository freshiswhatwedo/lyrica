import lyricsgenius
import 

token = "SJgV3xqS7Lim040mG6wG0e5pJAX6LrSZ4UIod4Dm392eBtALTyfVF18scCWbwMEP"
genius = lyricsgenius.Genius(token)
#artist = genius.search_artist("Andmax", max_songs=3, sort="title")
#print(artist)
#print("split")
#print(artist.songs)

#song = genius.search_song("haunt u", "lil peep")
#print(song.lyrics)

def lyricFinder(Song,Artist):
      song = genius.search_song(Song, Artist)
      if song:
        lyrics_lines = song.lyrics.split('\n')
        lyrics_dict = {i+1: line for i, line in enumerate(lyrics_lines) if line.strip() != ''}
        return lyrics_dict
      

def lineNumber(L):
    for i in L:
        value = 0
        value = value + 1
        int(value)
        return value


Song = input("Whats the songs name?")
Artist = input("Whats the artists name?")

Lyrics = lyricFinder(Song,Artist)
linenumber = lineNumber(Lyrics)

lineNumber = list(Lyrics.values())

print(lineNumber)

# for i in Lyrics[range(2,lineNumber)]
# print(Lyrics)
   

