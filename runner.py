import json
import os
from time import sleep


def loadData():
    global data
    with open("data.json", "r") as f:
        data = json.load(f)


def saveData():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def runFile(line, data):
    if line.endswith(".img"):
        for row in data[line]:
            print(row)

    elif line.endswith(".vid"):
        os.system("clear")
        for row in data[line]:
            if row == ".":
                sleep(0.1)
                os.system("clear")
            elif row == ",":
                sleep(0.03)
                os.system("clear")
            else:
                print(row)

    elif line.endswith(".py"):
        if line != "main.py":
            try:
                if line in data:
                    originalDir = os.getcwd()
                    os.chdir("./spkg")
                    os.system(f"python3 {line}")
                    os.chdir(originalDir)
                    loadData()
                else:
                    for line in os.listdir("./spkg"):
                        if os.path.isfile(line):
                            print(f"Special package {line} has not been installed yet")
                            yesNo = input("Do you want to install it? y/n : ")
                            if yesNo == "y":
                                print("Searching...")
                                sleep(1)
                                print(f"Found {line} in spkg repository!")
                                sleep(0.5)
                                print("Installing...")
                                sleep(2)
                                data[line] = []
                                saveData()
                                print(f"{line} installed succesfully!")
            except KeyError:
                print(f"Special pkg {line} doesn't exist!")

    else:
        print(f"\n {line} \n")
        for i, b in enumerate(data[line], start=0):
            print(f"{i}    {b}")
        print("")
