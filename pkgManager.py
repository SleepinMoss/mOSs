import json
import os
from pathlib import Path
from time import sleep


def saveData(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def pkg(command, args, data):
    if command == "install":
        print("Searching...")
        sleep(1)
        targetFile = args + ".json"
        for file in os.listdir("./pkg"):
            if file == targetFile:
                print(f"Found {args} in pkg repository!")
                sleep(0.2)
                print("Installing...")
                sleep(0.8)
                filePath = Path(__file__).parent / "pkg" / targetFile
                with open(filePath, "r", encoding="utf-8") as f:
                    package = json.load(f)[args]
                data[args] = package
                saveData(data)
                print(f"{args} installed succesfully!")
                return
        print(f"{args} doesn't exist in pkg repo")

    elif command == "push":
        if args in data:
            print("Reading package...")
            targetFile = args + ".json"
            sleep(1)
            for file in os.listdir("./pkg"):
                if targetFile == file:
                    print(f"Error. Package {args} is already in the repository!")
                    print("If you still want to push it, change your package name")
                    return
            print("Pushing package...")
            package = {}
            package[args] = data[args]
            with open(targetFile, "w") as f:
                json.dump(package, f, indent=4)
            filePath = Path(__file__).parent / "pkg"
            os.system(f"mv '{targetFile}' {filePath}")
            sleep(2.5)
            print(f"Package {args} pushed succesfully!")
        else:
            print(f"KeyError, can't find {args}")

    elif command == "search":
        print("Searching for package...")
        sleep(0.5)
        for file in os.listdir("./pkg"):
            if args in file:
                targetFile = file.replace(".json", "")
                print(f"Found {targetFile}!")
                return
        print(f"Can't find '{args}' or similiar package!")

    elif command == "list":
        for file in os.listdir("./pkg"):
            targetFile = file.replace(".json", "")
            print(f"'{targetFile}'")
