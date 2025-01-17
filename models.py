from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "availability": self.availability,
        }
