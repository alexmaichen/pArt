"""init"""
from tkinter import *
from tkinter import ttk

def shuffle(string: str) -> str: # shuffle the elements of a python3 list randomly
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

pixelArtFileName = "pa_pixels.txt"
wordListFileName = "pa_words.txt"

# colorcoded constants to fill pixel art with
# TODO make this fully modifiable by the user using the currently unused CONJ list, which would be filled with the types the user wants to declare, at will
CONJ      = []

NULL      = 0
INFINITIV = WH = 1
PRESENT   = BL = 2
PRETERIT  = BR = 3
PERFECT   = OR = 4

infi = []
pres = []
pret = []
pref = []

with open(wordListFileName) as wordLptr:
    infi = wordLptr.readline().split(" ")
    pres = wordLptr.readline().split(" ")
    pret = wordLptr.readline().split(" ")
    perf = wordLptr.readline().split(" ")

# thought randomizing might be nice so as to have some variance in what words appear (and where they appear) from one time to the next
infi = shuffle(infi)
pres = shuffle(pres)
pret = shuffle(pret)
perf = shuffle(perf)

# pixel art 2dlist
drawing = []

with open(pixelArtFileName) as pixelAptr:
    for line in pixelAptr:
        drawing.append(line)

"""generate grid"""
# init window
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

#
for x in range(len(drawing)):
    for y in range(len(drawing[x])):
        wordT = drawing[x][y]
        word = ""
        if pres and pret and infi and perf:
            if wordT == PRESENT:
                word = str(y)+str(x) + " = " + pres.pop()
            if wordT == PRETERIT:
                word = str(y)+str(x) + " = " + pret.pop()
            if wordT == INFINITIV:
                word = str(y)+str(x) + " = " + infi.pop()
            if wordT == PERFECT:
                word = str(y)+str(x) + " = " + perf.pop()
            ttk.Button(frm, text=word).grid(column=1+y, row=0+x)
        else:
            root.destroy()
            raise ValueError("Did not supply enough values to populate grid.")
root.mainloop()
