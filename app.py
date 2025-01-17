from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI and disable modification tracking
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)


# Database Model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique product ID (Primary Key)
    name = db.Column(db.String(80), nullable=False)  # Product name (required)
    category = db.Column(db.String(80), nullable=False)  # Product category (required)
    price = db.Column(db.Float, nullable=False)  # Product price (required)
    availability = db.Column(db.Boolean, default=True)  # Product availability (defaults to True)

    def serialize(self):
        """
        Convert a Product object into a dictionary for JSON output.
        
        Returns:
        - A dictionary with product information: id, name, category, price, and availability
        """
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "availability": self.availability,
        }


# Initialize the database (creates tables)
with app.app_context():
    db.create_all()


# Home route: Renders the index.html template
@app.route("/")
def index():
    return render_template("index.html")


# Route to list all products (GET method)
@app.route("/products", methods=["GET"])
def list_products():
    # Query all products from the database
    products = Product.query.all()
    # Return a JSON response with the serialized product list
    return jsonify([product.serialize() for product in products])


# Route to search products by name, category, or availability (GET method)
@app.route("/products/search", methods=["GET"])
def search_products():
    # Get search parameters from the query string
    name = request.args.get("name")
    category = request.args.get("category")
    availability = request.args.get("availability")

    # Start building the query
    query = Product.query
    
    # Filter by name if provided
    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
    # Filter by category if provided
    if category:
        query = query.filter(Product.category.ilike(f"%{category}%"))
    # Filter by availability if provided
    if availability:
        query = query.filter(Product.availability == (availability.lower() == "true"))

    # Execute the query and return matching products
    products = query.all()
    return jsonify([product.serialize() for product in products])


# Route to create a new product (POST method)
@app.route("/products", methods=["POST"])
def create_product():
    # Get product data from the request body (JSON)
    data = request.json
    # Create a new product object
    new_product = Product(
        name=data["name"],
        category=data["category"],
        price=data["price"],
        availability=data["availability"],
    )
    # Add the new product to the session and commit to the database
    db.session.add(new_product)
    db.session.commit()
    # Return the serialized new product with a 201 status code
    return jsonify(new_product.serialize()), 201


# Route to update an existing product by ID (PUT method)
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    # Get the product to update by its ID (returns 404 if not found)
    product = Product.query.get_or_404(product_id)
    # Get updated product data from the request body (JSON)
    data = request.json
    # Update the product attributes with the provided data
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.price = data.get("price", product.price)
    product.availability = data.get("availability", product.availability)
    # Commit the changes to the database
    db.session.commit()
    # Return the serialized updated product
    return jsonify(product.serialize())


# Route to delete a product by ID (DELETE method)
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    # Get the product to delete by its ID (returns 404 if not found)
    product = Product.query.get_or_404(product_id)
    # Delete the product from the session and commit the change
    db.session.delete(product)
    db.session.commit()
    # Return a 204 status code (No Content) to indicate successful deletion
    return "", 204


# Start the Flask application with debugging enabled
if __name__ == "__main__":
    app.run(debug=True)
