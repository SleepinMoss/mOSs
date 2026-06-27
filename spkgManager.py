import json
import os
from time import sleep


def saveData(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def spkg(command, args, data):
    if command == "install":
        print("Searching...")
        sleep(1)
        for file in os.listdir("./spkg"):
            if args == file:
                print(f"Found {args} in spkg repository!")
                sleep(0.5)
                print("Installing...")
                sleep(2)
                data[args] = []
                saveData(data)
                print(f"{args} installed succesfully!")
                return
        print(f"{args} doesn't exist in spkg repo")

    elif command == "search":
        print("Searching...")
        sleep(1)
        found = False
        for file in os.listdir("./spkg"):
            if args in file:
                print(f"Found {file}!")
                found = True
        if not found:
            print(f"Can't find {args} or similiar package!")

    elif command == "list":
        for file in os.listdir("./spkg"):
            if file.endswith(".py") and file != "main.py":
                print(f"'{file}'")
