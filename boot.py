import json
import os
import shutil
from time import sleep

with open("logo.json", "r") as file:
    logo = json.load(file)

columns = shutil.get_terminal_size().columns
read = 0
subtitle = [
    "Reading data",
    "Reading data.",
    "Reading data..",
    "Reading data...",
    "Reading data",
    "Reading data.",
    "Loading commands",
    "Loading commands.",
    "Loading commands..",
    "Loading commands...",
    "Loading commands",
    "Loading commands.",
    "Loading commands..",
    "Loading commands...",
    "Launching mOSs",
    "Launching mOSs.",
    "Launching mOSs..",
    "Launching mOSs...",
    "Welcome bro!",
    "Welcome bro!",
    "Welcome bro!",
]

while read != len(subtitle):
    os.system("clear")
    print("\n\n\n")
    for row in logo["logo.img"]:
        print(row.center(columns))
    print("")
    print(subtitle[read].center(columns))
    print("\n\n\n")
    sleep(0.5)
    read += 1
