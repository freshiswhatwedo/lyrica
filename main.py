import syncedlyrics
from io import open

song = "haunt u"
artist= "lil peep"
lrc = syncedlyrics.search(f"[{song}] [{artist}]")

text = "asddasdasads"

file = open("./LRC","w")
file.write(lrc)
file.close

file = open("./LRC","r")
file = file.read()
print(file)

