from flask import Flask, render_template, request, jsonify
from products import get_products, get_recommendations

app = Flask(__name__)

products = get_products()


@app.route("/")
def home():
    return render_template("index.html", products=products)


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify(products)

    results = []

    for product in products:
        text = " ".join([
            str(product["name"]),
            str(product["category"]),
            str(product["description"])
        ]).lower()

        # Search every word, not just the complete phrase
        words = query.split()

        if all(word in text for word in words):
            results.append(product)

    return jsonify(results)


@app.route("/recommendations/<int:product_id>")
def recommendations(product_id):
    return jsonify(get_recommendations(product_id, products))


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email", "").strip()
    password = data.get("password", "").strip()

    if email and password:
        return jsonify({
            "success": True,
            "message": "Login successful! Welcome to ShopSmart."
        })

    return jsonify({
        "success": False,
        "message": "Please enter email and password."
    })


if __name__ == "__main__":
    app.run(debug=True)