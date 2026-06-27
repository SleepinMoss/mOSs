from colorama import Fore, Style

fileCommands = ["create", "delete", "duplicate", "rename", "list"]


def fileMan(line, data):
    if line.startswith("create "):
        line = line.split(" ", 1)[1]
        if line in data:
            print("That file already exist!")
        else:
            data[line] = []

    elif line.startswith("delete "):
        line = line.split(" ", 1)[1]
        try:
            data.pop(line)
        except KeyError:
            print(f"KeyError, {line} doesn't exist!")

    elif line.startswith("duplicate "):
        line = line.split(" ", 1)[1]
        try:
            temp = data[line]
            new = input(Fore.YELLOW + "Duplicated file name > " + Style.RESET_ALL)
            if new in data:
                print("That file already exist!")
            else:
                data[new] = temp
        except KeyError:
            print(f"Can't find {line}")

    elif line.startswith("rename "):
        line = line.split(" ", 1)[1]
        try:
            temp = data[line]
            new = input(Fore.YELLOW + "Rename file to > " + Style.RESET_ALL)
            if new in data:
                print("That file already exist!")
            else:
                data[new] = temp
                data.pop(line)
        except KeyError:
            print(f"Can't find {line}")

    elif line == "list":
        for file in data:
            if file.endswith(".os"):
                print(Fore.YELLOW + f"⤷{file}")
        for file in data:
            if file.endswith(".img"):
                print(f"⤷{file}")
        for file in data:
            if file.endswith(".vid"):
                print(f"⤷{file}")
        for file in data:
            if file.endswith(".py"):
                print(f"⤷{file}")
        for file in data:
            if "." not in file:
                print(f"⤷{file}")
        print("" + Style.RESET_ALL)
