from flask import Blueprint, jsonify, request  # Importing necessary Flask modules
from models import Product, db  # Importing the Product model and the db instance

# Creating a Blueprint to organize the routes for the application
routes_blueprint = Blueprint('routes', __name__)

# Route to list all products in the database
@routes_blueprint.route("/products", methods=["GET"])
def list_products():
    try:
        products = Product.query.all()  # Query all products from the database
        return jsonify([product.serialize() for product in products])  # Return the list of serialized products
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error message in case of an exception

# Route to get a single product by its ID
@routes_blueprint.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    try:
        product = db.session.get(Product, product_id)  # Fetch the product by ID from the database
        if not product:
            return jsonify({"error": "Product not found"}), 404  # Return error if the product is not found
        return jsonify(product.serialize())  # Return the serialized product data
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error message in case of an exception

# Route to create a new product
@routes_blueprint.route("/products", methods=["POST"])
def create_product():
    try:
        data = request.json  # Get the JSON data from the request
        new_product = Product(
            name=data["name"],
            category=data["category"],
            price=data["price"],
            availability=data["availability"]
        )
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to save the product in the database
        return jsonify(new_product.serialize()), 201  # Return the serialized product with a 201 status code
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return an error message in case of an exception

# Route to update an existing product by its ID
@routes_blueprint.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    try:
        product = db.session.get(Product, product_id)  # Fetch the product by ID from the database
        if not product:
            return jsonify({"error": "Product not found"}), 404  # Return error if the product is not found
        data = request.json  # Get the JSON data from the request
        # Update the product fields with the new data, keeping the old values if no new data is provided
        product.name = data.get("name", product.name)
        product.category = data.get("category", product.category)
        product.price = data.get("price", product.price)
        product.availability = data.get("availability", product.availability)
        db.session.commit()  # Commit the transaction to save the updated product
        return jsonify(product.serialize())  # Return the serialized updated product
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return an error message in case of an exception

# Route to delete a product by its ID
@routes_blueprint.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        product = db.session.get(Product, product_id)  # Fetch the product by ID from the database
        if not product:
            return jsonify({"error": "Product not found"}), 404  # Return error if the product is not found
        db.session.delete(product)  # Delete the product from the session
        db.session.commit()  # Commit the transaction to remove the product from the database
        return "", 204  # Return a 204 status code indicating successful deletion with no content
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error message in case of an exception

# Route to search for products based on various parameters (name, category, availability)
@routes_blueprint.route("/products/search", methods=["GET"])
def search_products():
    try:
        # Get the query parameters from the request
        name = request.args.get("name")
        category = request.args.get("category")
        availability = request.args.get("availability")

        query = Product.query  # Start the query for products
        # Filter products based on the provided parameters
        if name:
            query = query.filter(Product.name.ilike(f"%{name}%"))
        if category:
            query = query.filter(Product.category.ilike(f"%{category}%"))
        if availability:
            query = query.filter(Product.availability == (availability.lower() == "true"))

        products = query.all()  # Execute the query to get the filtered products
        return jsonify([product.serialize() for product in products])  # Return the list of serialized products
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error message in case of an exception
