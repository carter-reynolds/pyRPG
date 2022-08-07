import tkinter as tk
from tkinter import ttk
import random as rand

class Tile:
    def __init__(self, type, color, chance = 0):
        self.type = type
        self.color = color
        self.chance = chance


# Adds up to 60%
tiles = [
    Tile('water', 'blue', 20),
    Tile('mine', 'black', 20),
    Tile('combat', 'red', 10),
    Tile('town', 'brown', 5),
    Tile('bank', 'green', 3),
    Tile('treasure', 'yellow', 2),
]


def randomTile():
    roll = rand.randint(1, 100)

    # Generate a list of chance ranges
    # When we roll, we see which range it falls in
    sum = 0
    ranges = []
    for tile in tiles:
        if (roll <= sum + tile.chance):
            return tile
        else:
            ranges.append(sum + tile.chance)
            sum += tile.chance

    # If roll was not in any of the ranges, return default
    return Tile('default', 'white')


style = ttk.Style()
style.configure("BW.TLabel", foreground="red", background="red", width=2, height=2)

class Map:
    def __init__(self, container):
        self.map = tk.Frame(container)

    def display(self):
        self.map.pack()

    def populate(self, rows, cols):
        for i in range (0,rows):
            for j in range (0, cols):
                tile = randomTile()
                print(tile.color)

                square = ttk.Button(self.map, text='', style="BW.TLabel")
                square.grid(column=i, row=j)

