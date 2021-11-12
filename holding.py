class Holding:
    name: str
    symbol: str
    percentageHolding: int
    amountHolding: int
    link: str

    def __init__(self):
        self.name = ""
        self.symbol = ""
        self.percentageHolding = ""
        self.amountHolding = ""
        self.link = ""

    def __str__(self) -> str:
        return (self.name + ", " + self.symbol + ", " + self.link + ", " + str(self.percentageHolding) + ", " + str(self.amountHolding))

    def toObject(self) -> object:
        return {
            "name": self.name,
            "symbol": self.symbol,
            "link": self.link,
            "percentageHolding": self.percentageHolding,
            "amountHolding": self.amountHolding
        }
