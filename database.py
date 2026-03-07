from row import entry


class db:
    rows: list[entry] = []
    bitmap: list[str] = []
    compressOrder: str = ""
    wordSize: int = 8
    words: list[str] = []

    @staticmethod
    def isRun(s: str) -> bool:
        return len(set(s)) == 1

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
            for i in range(0, len(self.compressOrder), self.wordSize - 1)
        ]

    def wah(self):
        self.getWords()
        result: str = ""
        in_run: bool = False
        run_len: int = 0
        run_type: None | str = None

        for string in self.words:
            print(string)
            if in_run and run_type:
                if self.isRun(string):
                    if string[0] == run_type:
                        run_len += 1

                        if len(bin(run_len)) > self.wordSize:
                            result += (
                                "1" + run_type + f"{run_len:0{self.wordSize - 2}b}"
                            )
                            run_len = 1
                    else:
                        result += "1" + run_type + f"{run_len:0{self.wordSize - 2}b}"
                        run_type = string[0]
                else:
                    result += "1" + run_type + f"{run_len:0{self.wordSize - 2}b}"
                    result += "0" + string
                    run_type = None
                    in_run = False
                    run_len = 0

            else:
                if self.isRun(string):
                    in_run = True
                    run_len = 1
                    run_type = string[0]
                else:
                    result += "0" + string

        # print(result)
