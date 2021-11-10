from urllib3.util.url import Url


class Holding:
    name: str
    link: Url
    symbol: str
    percentageHolding: str

    def __init__(self):
        self.name = ""
        self.link = Url()
        self.symbol = ""
        self.percentageHolding = ""

    def __str__(self) -> str:
        return (self.name + ", " + self.link + ", " + self.symbol + ", " + self.percentageHolding)

    def toObject(self) -> object:
        return {
            "name": self.name,
            "link": self.link,
            "symbol": self.symbol,
            "percentageHolding": self.percentageHolding
        }
