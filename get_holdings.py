import json
import requests
from holding import Holding


def getHoldings(etf: str) -> list:
    holdings = []
    html = requests.get("https://www.zacks.com/funds/etf/" +
                        etf + "/holding", headers={"User-Agent": "008"})

    jsons = json.loads(html.text[html.text.find(
        "etf_holdings.formatted_data")+30:html.text.find("etf_holdings.table_header")-2])

    for _ in jsons:
        holding: Holding = Holding()
        if("truncated" in _[0]):
            holding.name = _[0][_[0].find("title")+7:_[0].find("\">")]
            # holding.name = _[0]
        else:
            holding.name = _[0]
        if("button" in _[1]):
            holding.symbol = _[1][_[1].find(
                "<span class=\"hoverquote-symbol\">")+32:_[1].find("<span class=\"sr-only\">")]
            # holding.symbol = _[1]
        else:
            holding.symbol = _[1]
        holding.link = "https://www.zacks.com/stock/quote/" + holding.symbol
        holding.amountHolding = int(_[2].replace(',', ''))
        holding.percentageHolding = float(_[3])

        holdings.append(holding.toObject())

    return holdings
