import csv


def load_products():
    products = []

    with open("products.csv", "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        # Check CSV columns
        print("CSV Columns:", reader.fieldnames)

        for row in reader:

            product = {
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"]),
                "old_price": float(row["old_price"]),
                "rating": float(row["rating"]),
                "reviews": int(row["reviews"]),
                "discount": int(row["discount"]),
                "image": row["image"],
                "description": row["description"],

                # Features
                "features": [
                    feature.strip()
                    for feature in row["features"].split(";")
                    if feature.strip()
                ]
            }

            products.append(product)

    return products


def get_products():
    return products


def get_recommendations(product_id):
    selected_product = None

    for product in products:
        if product["id"] == product_id:
            selected_product = product
            break

    if selected_product is None:
        return []

    recommendations = []

    for product in products:

        if product["id"] != product_id:

            if product["category"] == selected_product["category"]:
                recommendations.append(product)

    # Sort by rating
    recommendations.sort(
        key=lambda x: x["rating"],
        reverse=True
    )

    return recommendations[:4]


# Load products when program starts
products = load_products()