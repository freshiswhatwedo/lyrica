import syncedlyrics

song = "haunt u"
artist= "lil peep"
lrc = syncedlyrics.search(f"[{song}] [{artist}]")

print(lrc)

file = open("./lyrics.txt","a")
file.write = lrc
file.close

