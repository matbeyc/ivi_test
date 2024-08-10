from flask import Flask, jsonify, request

app = Flask(__name__)

chocolates = [
    {"id": 1, "name": "Dark Chocolate", "price": 2.5},
    {"id": 2, "name": "Milk Chocolate", "price": 2.0},
    {"id": 3, "name": "White Chocolate", "price": 3.0},
]

user_balance = {"user_id": 1, "balance": 10.0}


@app.route("/chocolates", methods=["GET"])
def get_chocolates():
    return jsonify(chocolates)


@app.route("/chocolates/<int:chocolate_id>/price", methods=["GET"])
def get_chocolate_price(chocolate_id):
    chocolate = next((choc for choc in chocolates if choc["id"] == chocolate_id), None)
    if chocolate:
        return jsonify({"price": chocolate["price"]})
    else:
        return jsonify({"error": "Chocolate not found"}), 404


@app.route("/buy/<int:chocolate_id>", methods=["POST"])
def buy_chocolate(chocolate_id):
    chocolate = next((choc for choc in chocolates if choc["id"] == chocolate_id), None)
    if not chocolate:
        return jsonify({"error": "Chocolate not found"}), 404

    global user_balance
    if user_balance["balance"] >= chocolate["price"]:
        user_balance["balance"] -= chocolate["price"]
        return jsonify(
            {"message": "Purchase successful", "balance": user_balance["balance"]}
        )
    else:
        return jsonify({"error": "Insufficient balance"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
