from math import *
from tkinter import *

root = Tk()
w, h = 1280, 720
canv = Canvas(root, width=w, height=h, bg='black')
pi = 3.14


def Pifagor(x0, y0, a, L, N):
    k = 0.6
    if N > 0:
        x1 = x0 + L * cos(a)
        y1 = y0 - L * sin(a)
        line = canv.create_line(int(x0), int(y0), int(x1), int(y1), fill='orange')
        Pifagor(x1, y1, a + pi / 4, L * k, N - 1)
        Pifagor(x1, y1, a - pi / 4, L * k, N - 1)
        Pifagor(x1, y1, a + pi / 6, L * k, N - 1)
        Pifagor(x1, y1, a - pi / 6, L * k, N - 1)


Pifagor(640, 720, pi / 2, 300, 8)
canv.pack()
root.mainloop()
