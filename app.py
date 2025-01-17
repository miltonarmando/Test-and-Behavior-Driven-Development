from flask import Flask, jsonify, request
from models import db, Product

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.serialize())

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.json
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.price = data.get("price", product.price)
    product.availability = data.get("availability", product.availability)
    db.session.commit()
    return jsonify(product.serialize())

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return "", 204

@app.route("/products", methods=["GET"])
def list_products():
    filters = {}
    if "name" in request.args:
        filters["name"] = request.args["name"]
    if "category" in request.args:
        filters["category"] = request.args["category"]
    if "availability" in request.args:
        filters["availability"] = request.args.get("availability") == "true"
    products = Product.query.filter_by(**filters).all()
    return jsonify([product.serialize() for product in products])

@app.route("/products", methods=["POST"])
def create_product():
    data = request.json
    new_product = Product(
        name=data["name"],
        category=data["category"],
        price=data["price"],
        availability=data["availability"]
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.serialize()), 201

if __name__ == "__main__":
    app.run(debug=True)
