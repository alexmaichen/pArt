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
# TODO make this fully modifiable by the user using the currently unused CONJ list, which would be filled with the types the user wants to declare, at will
CONJ      = []

NULL      = 0
INFINITIV = 1
PRESENT   = 2
PRETERIT  = 3
PERFECT   = 4

infi = []
pres = []
pret = []
pref = []

with open(wordListFileName) as wordLptr:
    infi = wordLptr.readline().split(" ")
    pres = wordLptr.readline().split(" ")
    pret = wordLptr.readline().split(" ")
    perf = wordLptr.readline().split(" ")

for i in range(len(infi)):
    infi[i] = infi[i].rstrip()
for i in range(len(pres)):
    pres[i] = pres[i].rstrip()
for i in range(len(pret)):
    pret[i] = pret[i].rstrip()
for i in range(len(perf)):
    perf[i] = perf[i].rstrip()

# thought randomizing might be nice so as to have some variance in what words appear (and where they appear) from one time to the next
infi = shuffle(infi)
pres = shuffle(pres)
pret = shuffle(pret)
perf = shuffle(perf)

# pixel art 2dlist
drawing = []

with open(pixelArtFileName) as pixelAptr:
    i = 0
    for line in pixelAptr:
        line = charRemove(line, " ")
        drawing.append(line.rstrip())
        i += 1

"""generate grid"""
# init window
root = Tk()
frm = ttk.Frame(root)
frm.grid()

# populate grid with values and display everything
for x in range(len(drawing)):
    for y in range(len(drawing[x])):
        wordT = int(drawing[x][y])
        word = ""
        if pres and pret and infi and perf:

            if wordT == PRESENT:
                word = pres.pop()
            if wordT == PRETERIT:
                word = pret.pop()
            if wordT == INFINITIV:
                word = infi.pop()
            if wordT == PERFECT:
                word = perf.pop()
                
            ttk.Button(frm, text = word).grid(column = y, row = x)
        else:
            raise ValueError("Did not supply enough values to populate grid.")
root.mainloop()
