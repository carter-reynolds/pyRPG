import tkinter as tk

class Map:
    def __init__(self, container):
        self.map = tk.Frame(container)

    def display(self):
        self.map.pack()

    def populate(self, rows, cols):
        for i in range (0,rows):
            for j in range (0, cols):
                if (i + j) % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                square = tk.Button(self.map, bg=color, width=2, height=2, text = '')
                square.grid(column=i, row=j)

