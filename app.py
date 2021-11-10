from os import error
from flask import Flask, jsonify, request
from getHoldings import getHoldings

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get():
    etf = request.args.get("etf")
    try:
        list = getHoldings(etf)
        return jsonify(list)
    except IndexError:
        return jsonify(data="We are unable to find the holdings for the requested ETF.", errors="Data not found."), 404


if(__name__ == "__main__"):
    app.run(debug=True)
