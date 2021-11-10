import requests
from bs4 import BeautifulSoup
from holding import Holding


def getHoldings(etf) -> list:
    holdings = []
    html = requests.get("https://www.marketwatch.com/investing/fund/" +
                        etf + "/holdings?mod=mw_quote_tab")

    soup = BeautifulSoup(html.text, "html.parser")
    table = soup.find_all(
        "table", class_="table table--primary align--right row-hover")[0]

    rows = table.find_all("tr")
    for row in rows:
        holding = Holding()
        if(row.a == None):
            continue
        else:
            for data in row.find_all("td"):
                for child in data.children:
                    if("%" in child):
                        holding.percentageHolding = child
                    elif("https" in str(child)):
                        link = BeautifulSoup(str(child), "html.parser")
                        holding.link = link.a["href"]
                        holding.name = link.string
                    elif("%" not in child and "link" not in child):
                        holding.symbol = child.string

        holdings.append(holding.toObject())
    return holdings
