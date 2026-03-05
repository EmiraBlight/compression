class entry:
    animal: str = ""
    age: int = 0
    adopted: bool = False

    def __init__(self, params: list[str]):
        self.animal = params[0]
        self.age = int(params[1])
        self.adopted = True if params[2] == "True" else False

    def __repr__(self):
        return f"animal: {self.animal}\nage:{self.age}\nis adopted: {self.adopted}"

    def toBin(self) -> str:
        result: str = ""
        match self.animal:
            case "cat":
                result += "1000"
            case "dog":
                result += "0100"
            case "turtle":
                result += "0010"
            case "bird":
                result += "0001"
            case _:
                raise Exception("Animal not in domain")
        if self.age > 100 or self.age < 1:
            raise Exception("Age not in domain")
        age = "0000000000"
        bit = (self.age - 1) // 10
        age = age[:bit] + "1" + age[bit + 1 :]
        result += age
        if self.adopted:
            return result + "10"
        return result + "01"
