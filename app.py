from flask import Flask, jsonify, request
from getHoldings import getHoldings

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get():
    etf = request.args.get("etf")
    return jsonify(getHoldings(etf))


if(__name__ == "__main__"):
    app.run(debug=True)
