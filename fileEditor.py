import json
import os

from colorama import Fore, Style


def saveData(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def editz(line, data):
    if line in data:
        os.system("clear")
        print(Fore.YELLOW + f"{line}\n" + Style.RESET_ALL)
        editing = True
        if data[line] == []:
            pass
        else:
            for i, b in enumerate(data[line], start=0):
                print(f"{i}    {b}")
        while editing:
            try:
                edit = input(f"{i + 1}    ")
            except UnboundLocalError:
                edit = input("0    ")

            if edit == ":quit":
                editing = False
                os.system("clear")
                saveData(data)

            elif edit.startswith(":delete "):
                edit = edit.split(" ", 1)[1]
                del data[line][int(edit)]
                os.system("clear")
                print(Fore.YELLOW + f"{line}\n" + Style.RESET_ALL)
                for i, b in enumerate(data[line], start=0):
                    print(f"{i}    {b}")

            elif edit.startswith(":edit "):
                edit = edit.split(" ", 1)[1]
                os.system("clear")
                for i, b in enumerate(data[line], start=0):
                    print(f"{i}    {b}")
                data[line][int(edit)] = input(f"Edit line {edit}: ")
                os.system("clear")
                for i, b in enumerate(data[line], start=0):
                    print(f"{i}    {b}")

            elif edit.startswith(":insert "):
                edit = edit.split(" ", 1)[1]
                os.system("clear")
                for i, b in enumerate(data[line], start=0):
                    print(f"{i}    {b}")
                ins = input(f"Insert at line {edit}: ")
                data[line].insert(int(float(edit)), ins)
                os.system("clear")
                for i, b in enumerate(data[line], start=0):
                    print(f"{i}    {b}")

            else:
                data[line].append(edit)
                os.system("clear")
                for i, b in enumerate(data[line], start=0):
                    print(f"{i}    {b}")
    else:
        print(f"KeyError, {line} doesn't exist!")
