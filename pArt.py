"""init"""
from tkinter import *
from tkinter import ttk

#shuffle a list or string
def shuffle(string: str) -> str:
    from random import randint
    s = []
    d = []
    while len(s) != len(string): # make sure it has copied every entry
        r = randint(0, len(string) - 1)
        while r in d:
            r = (r+1)%len(string)
        # memory which entries have been copied already
        d.append(r)
        s.append(string[r])
    return s

#remove all instances of a given char from a given string
def charRemove(string: str, charToRemove: str) -> str:
    w = ""
    for c in string:
        if c != charToRemove:
            w += c
    return w

pixelArtFileName = "pa_pixels.txt"
wordListFileName = "pa_words.txt"

# colorcoded constants to fill pixel art with
conj = []
with open(wordListFileName) as wordLptr:
    nLines = 0
    for line in wordLptr:
        nLines += 1
        line = line.rstrip().split(" ")
        conj.append(line)
        print(line)

# pixel art 2dlist
drawing = []

with open(pixelArtFileName) as pixelAptr:
    for line in pixelAptr:
        line = charRemove(line, " ")
        drawing.append(line.rstrip())

# init window
root = Tk()
frm = ttk.Frame(root)
frm.grid()

# populate grid with values and display everything
for x in range(len(drawing)):
    for y in range(len(drawing[x])):
        wordT = int(drawing[x][y])
        if wordT > nLines:
            raise ValueError("A pixel in " + pixelArtFileName + " does not have any associated words in " + wordListFileName)
        if wordT == 0:
            word = ""
        elif conj[wordT - 1]:
            word = conj[wordT - 1].pop()
        else:
            raise ValueError("Did not sufficiently populate line " + str(wordT) + " in " + wordListFileName)
        ttk.Button(frm, text = word).grid(column = y, row = x)
root.mainloop()
