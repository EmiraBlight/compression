from io import TextIOWrapper

from row import row


def readFile(name: str) -> list[row]:
    """returns a list of lists that consist a str, int bool each
    Ex "bird,84,False" -> ["bird", 84, False]
    this will make logic easier later down the line"""
    f: TextIOWrapper = open(name, "r")
    return [row(entry.split(",")) for entry in f.read().splitlines()]


def toFile(arr: list[row], fileName: str) -> None:
    f = open(fileName, "w")
    for i in arr:
        f.write(i.toBin() + "\n")
    f.close()


rows = readFile("data/animals_small.txt")

toFile(rows, "animals_small")
