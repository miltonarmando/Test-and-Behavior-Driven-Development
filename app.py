from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "availability": self.availability,
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Root route with HTML page
@app.route("/")
def index():
    return render_template("index.html")

# RESTful API routes
@app.route("/products", methods=["GET"])
def list_products():
    products = Product.query.all()
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


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
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


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = db.session.get(Product, product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return "", 204

@app.route("/products/search", methods=["GET"])
def search_products():
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


if __name__ == "__main__":
    app.run(debug=True)
