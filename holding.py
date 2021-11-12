from typing import Any


class Holding:
    name: str
    symbol: str
    percentageHolding: Any
    amountHolding: int
    link: str

    def __init__(self):
        self.name = ""
        self.symbol = ""
        self.percentageHolding = 0.00
        self.amountHolding = 0
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
