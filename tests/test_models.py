import pytest  # Import pytest for writing and running tests
from models import Product  # Import the Product model from the models module
from app import app, db  # Import the app instance and the database from the app module

# Fixture to set up the app for testing
@pytest.fixture
def app():
    app = app('testing')  # Initialize the app in 'testing' mode
    with app.app_context():  # Create an app context for database operations
        db.create_all()  # Create all database tables
        yield app  # Yield the app instance to be used in tests
        db.drop_all()  # Drop all tables after the test is done

# Fixture to create a new product instance for testing
@pytest.fixture
def new_product():
    return Product(name="Test Product", category="Category 1", price=10.0, availability=True)  # Return a new product instance

# Test function to verify product creation
def test_create_product(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        product = Product.query.first()  # Retrieve the first product from the database
        assert product.name == "Test Product"  # Assert the product name matches the expected value

# Test function to verify product update
def test_update_product(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        product = Product.query.first()  # Retrieve the first product from the database
        product.name = "Updated Product"  # Update the product's name
        db.session.commit()  # Commit the changes to the database
        assert product.name == "Updated Product"  # Assert the product name is updated correctly

# Test function to verify product deletion
def test_delete_product(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        product = Product.query.first()  # Retrieve the first product from the database
        db.session.delete(product)  # Delete the product from the session
        db.session.commit()  # Commit the transaction to the database
        assert Product.query.count() == 0  # Assert that the product count is now 0

# Test function to verify listing of all products
def test_list_all_products(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        products = Product.query.all()  # Retrieve all products from the database
        assert len(products) > 0  # Assert that the product list contains at least one product

# Test function to verify finding a product by its name
def test_find_product_by_name(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        product = Product.query.filter_by(name="Test Product").first()  # Find the product by name
        assert product is not None  # Assert that the product exists

# Test function to verify finding a product by its category
def test_find_product_by_category(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        product = Product.query.filter_by(category="Category 1").first()  # Find the product by category
        assert product is not None  # Assert that the product exists

# Test function to verify finding a product by its availability status
def test_find_product_by_availability(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        product = Product.query.filter_by(availability=True).first()  # Find the product by availability
        assert product is not None  # Assert that the product exists
