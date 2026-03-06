from row import entry


class db:
    rows: list[entry] = []
    bitmap: list[str] = []
    compressOrder: str = ""
    wordSize: int = 8
    words: list[str] = []

    def __init__(self, file: str):
        f = open(file, "r")
        self.rows = [entry(line.split(",")) for line in f.read().splitlines()]
        self.bitmap = [i.toBin() for i in self.rows]
        f.close()

    def __repr__(self) -> str:
        result = ""
        for i in range(len(self.rows)):
            result += f"Entry:{self.rows[i]}\nbin:{self.bitmap[i]}\n"
            result += "-" * 50 + "\n"
        return result

    def toBin(self, file) -> None:
        f = open(file, "w")
        for i in self.bitmap:
            f.write(i + "\n")
        f.close()

    def getOrder(self) -> None:
        result = ""
        if self.bitmap == []:
            raise Exception("bitmap not defined or database is empty!")
        for i in range(16):
            for j in range(len(self.bitmap)):
                result += self.bitmap[j][i]
        self.compressOrder = result

    def getWords(self) -> None:
        self.words = [
            str(self.compressOrder[i : i + self.wordSize - 1])
            for i in range(0, len(self.bitmap), self.wordSize - 1)
        ]
