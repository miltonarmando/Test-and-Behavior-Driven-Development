from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy()

class Product(db.Model):
    # Define the 'Product' class as a model representing a table in the database
    
    # Define the columns for the 'Product' table
    id = db.Column(db.Integer, primary_key=True)  # Unique product ID (primary key)
    name = db.Column(db.String(80), nullable=False)  # Product name (must be provided)
    category = db.Column(db.String(80), nullable=False)  # Product category (must be provided)
    price = db.Column(db.Float, nullable=False)  # Product price (must be provided)
    availability = db.Column(db.Boolean, nullable=False)  # Availability status (must be provided)
    
    def serialize(self):
        """
        Convert the 'Product' object into a dictionary to be returned as JSON.
        
        Returns:
        - A dictionary representation of the product with keys: id, name, category, price, and availability
        """
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "availability": self.availability,
        }
