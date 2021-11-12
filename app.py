from flask import Flask, jsonify, request, logging
from flask.wrappers import Response
from get_holdings import getHoldings

app = Flask(__name__)
logging.create_logger(app)


@app.route('/list', methods=["GET"])
def getHolding() -> Response:
    etf = request.args.get("etf")
    app.logger.debug(etf)
    try:
        list = getHoldings(etf)
        return jsonify(list)
    except IndexError:
        return jsonify(data="We are unable to find the holdings for the requested ETF.", errors="Data not found."), 404


if(__name__ == "__main__"):
    app.run(debug=True)
