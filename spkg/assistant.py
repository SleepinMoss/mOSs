import json
import random

with open("pattern.json", "r") as jsonPattern:
    chain = json.load(jsonPattern)


def generateText(chain, startWord, length=10):
    result = [startWord]

    for _ in range(length):
        if startWord in chain:
            startWord = random.choice(chain[startWord])
            result.append(startWord)
        else:
            break

    return " ".join(result)


while True:
    prompt = input("Ask AI > ")
    prompt = (
        prompt.lower()
        .replace(",", "")
        .replace(".", "")
        .replace("?", "")
        .replace("'", "")
    )
    promptSplit = prompt.split()

    for i in range(len(promptSplit) - 1):
        currentWord = promptSplit[i]
        nextWord = promptSplit[i + 1]

        if currentWord not in chain:
            chain[currentWord] = []

        chain[currentWord].append(nextWord)

    with open("pattern.json", "w") as jsonPattern:
        json.dump(chain, jsonPattern, indent=4)

    keyword = random.choice(promptSplit)

    print("\n" + generateText(chain, keyword, random.randint(5, 20)) + "\n")
