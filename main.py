import lyricsgenius

token = "SJgV3xqS7Lim040mG6wG0e5pJAX6LrSZ4UIod4Dm392eBtALTyfVF18scCWbwMEP"
genius = lyricsgenius.Genius(token)

#artist = genius.search_artist("Andmax", max_songs=3, sort="title")
#print(artist)
#print("split")
#print(artist.songs)

#song = genius.search_song("haunt u", "lil peep")
#print(song.lyrics)

# def lyricFinder(Song,Artist):
#      song = genius.search_song(Song, Artist)
#      if song:
#         lyrics_lines = song.lyrics.split('\n')
#         lyrics_dict = {i+1: line for i, line in enumerate(lyrics_lines) if line.strip() != ''}
#         return lyrics_dict

def lyricFinder(Song,Artist):
    song = genius.search_song(Song, Artist)
    if song:
        lyrics_lines = song.lyrics.split('\n')
        filtered_lines = [line for line in lyrics_lines if not line.startswith('[') and line.strip() != '']
        lyrics_dict = {i+1: line for i, line in enumerate(filtered_lines)}
        return lyrics_dict
    else:
        return None
Lyrics = lyricFinder("runaway","Kanye west")

print(Lyrics)
   

