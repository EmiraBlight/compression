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

    def getWords(self) -> None:

        transpose = list(zip(*self.bitmap))
        line = ["".join(i) for i in transpose]
        new_arr = []
        for col in line:
            new_arr.append(
                [
                    col[i : i + self.wordSize - 1]
                    for i in range(0, len(col), self.wordSize - 1)
                ]
            )

        self.words = new_arr

    def wah(self):
        self.getWords()
        result: str = ""
        in_run: bool = False
        run_len: int = 0
        run_type: None | str = None
        for col in self.words:
            result = ""
            for word in col:
                if len(word) != self.wordSize - 1:
                    if in_run and run_type:
                        result += "1" + run_type + f"{run_len:0{self.wordSize - 2}b}"
                        run_type = None
                        run_len = 0
                        in_run = False

                    result += "0" + word + "0" * (self.wordSize - len(word) - 1)

                elif in_run and run_type:
                    if self.isRun(word):
                        if word[0] == run_type:
                            run_len += 1
                            if len(bin(run_len + 1)) > self.wordSize:
                                result += (
                                    "1" + run_type + f"{run_len:0{self.wordSize - 2}b}"
                                )
                                run_len = 1
                        else:
                            result += (
                                "1" + run_type + f"{run_len:0{self.wordSize - 2}b}"
                            )
                            run_type = word[0]
                    else:
                        result += "1" + run_type + f"{run_len:0{self.wordSize - 2}b}"
                        result += "0" + word
                        run_type = None
                        in_run = False
                        run_len = 0

                else:
                    if self.isRun(word):
                        in_run = True
                        run_len = 1
                        run_type = word[0]
                    else:
                        result += "0" + word
            print(result)
