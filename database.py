from row import entry


class db:
    rows: list[entry]
    bitmap: list[str]

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

    def toBin(self, file):
        f = open(file, "w")
        for i in self.bitmap:
            f.write(i + "\n")
        f.close()
