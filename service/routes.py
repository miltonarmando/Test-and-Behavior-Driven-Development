from flask import Blueprint, jsonify, request
from models import Product, db

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route("/products", methods=["GET"])
def list_products():
    try:
        products = Product.query.all()
        return jsonify([product.serialize() for product in products])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_blueprint.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    try:
        product = db.session.get(Product, product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        return jsonify(product.serialize())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_blueprint.route("/products", methods=["POST"])
def create_product():
    try:
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
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@routes_blueprint.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    try:
        product = db.session.get(Product, product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        data = request.json
        product.name = data.get("name", product.name)
        product.category = data.get("category", product.category)
        product.price = data.get("price", product.price)
        product.availability = data.get("availability", product.availability)
        db.session.commit()
        return jsonify(product.serialize())
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@routes_blueprint.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        product = db.session.get(Product, product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        db.session.delete(product)
        db.session.commit()
        return "", 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes_blueprint.route("/products/search", methods=["GET"])
def search_products():
    try:
        name = request.args.get("name")
        category = request.args.get("category")
        availability = request.args.get("availability")

        query = Product.query
        if name:
            query = query.filter(Product.name.ilike(f"%{name}%"))
        if category:
            query = query.filter(Product.category.ilike(f"%{category}%"))
        if availability:
            query = query.filter(Product.availability == (availability.lower() == "true"))

        products = query.all()
        return jsonify([product.serialize() for product in products])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
