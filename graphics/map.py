import tkinter as tk

window = tk.Tk()

map = tk.Frame(window)
map.pack()

for i in range (0,10):
    for j in range (0, 10):
        color = "black"
        if (i + j) % 2 == 0:
            color = "white"
        square = tk.Button(map, bg=color, width=2, height=2, text = '')
        square.grid(column=i, row=j)

