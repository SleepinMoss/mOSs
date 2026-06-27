import json
import os
from pathlib import Path
from time import sleep

from colorama import Fore, Style

from fileEditor import editz
from fileManager import fileCommands, fileMan
from pkgManager import pkg
from runner import runFile
from spkgManager import spkg

os.system("clear")

data = {}
command = 0
running = True


def loadData():
    global data
    with open("data.json", "r") as f:
        data = json.load(f)


def saveData():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def recognizeCommands(line):
    global running
    command = line.split(" ")[0]
    try:
        args = line.split(" ", 1)[1]
    except IndexError:
        args = ""

    if command == "echo":
        print(args)

    elif command == "help":
        print(Fore.YELLOW + "echo 'text'               = Print some text")
        print("create 'file'             = Create file")
        print("delete 'file'             = Delete file")
        print("edit 'file'               = Edit file")
        print("duplicate 'file'          = Duplicate file")
        print("rename 'file'             = Rename file")
        print("sleep 'seconds'           = Sleep for 'seconds'")
        print("list                      = List file")
        print("clear                     = Clear prompt")
        print("quit                      = Turn off mOSs")
        print("pkg install 'pkg'         = Install a package")
        print("pkg push 'pkg'            = Push your package to pkg repository")
        print("pkg list                  = List available packages")
        print("pkg search 'pkg'          = Search similiar packages")
        print("spkg install 'spkg'       = Install a special package")
        print("spkg list                 = List available special packages")
        print("spkg search 'spkg'        = Search similiar special packages")
        print(
            "'file'                    = Run (.os .py) or show (.img .vid normal) file"
            + Style.RESET_ALL
        )

    elif command == "clear":
        os.system("clear")

    elif command == "quit":
        running = False
        saveData()

    elif command == "sleep":
        try:
            sleep(int(args))
        except ValueError:
            print(Fore.RED + f"'{args}' is not even a number, lmao!")

    elif command == "edit":
        editz(args, data)

    elif line in data:
        if line.endswith(".os"):
            for com in data[line]:
                recognizeCommands(com)
        else:
            runFile(line, data)

    elif command == "pkg":
        command = args.split(" ")[0]
        try:
            args = args.split(" ", 1)[1]
        except IndexError:
            args = ""
        pkg(command, args, data)

    elif command == "spkg":
        command = args.split(" ")[0]
        try:
            args = args.split(" ", 1)[1]
        except IndexError:
            args = ""
        spkg(command, args, data)

    else:
        if command in fileCommands:
            fileMan(line, data)
            return

        for file in os.listdir("./spkg"):
            if line == file:
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
                    return

        targetFile = line + ".json"
        for file in os.listdir("./pkg"):
            if file == targetFile:
                print(f"{line} has not been installed yet")
                yesNo = input("Do you want to install it? y/n : ")
                if yesNo == "y":
                    print(f"Found {line} in pkg repository!")
                    sleep(0.2)
                    print("Installing...")
                    sleep(0.8)
                    filePath = Path(__file__).parent / "pkg" / targetFile
                    with open(filePath, "r", encoding="utf-8") as f:
                        package = json.load(f)[line]
                    data[line] = package
                    saveData()
                    print(f"{targetFile} installed succesfully!")
                    return

        print(f"Command {line} doesn't exist")


os.system("python3 boot.py")

loadData()
while running:
    command = input(Fore.BLUE + "/home > " + Style.RESET_ALL)
    recognizeCommands(command)
