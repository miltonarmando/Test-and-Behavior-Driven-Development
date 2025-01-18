import pytest  # Import pytest for writing and running tests
from models import Product, db  # Import the Product model and database instance from models
from flask import jsonify  # Import jsonify from Flask for returning JSON responses

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

# Test function to verify reading a product by ID
def test_read_product(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        response = app.test_client().get('/products/1')  # Send GET request to retrieve product by ID
        data = response.get_json()  # Parse the response as JSON
        assert data['name'] == "Test Product"  # Assert that the product name matches the expected value

# Test function to verify updating a product by ID
def test_update_product(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        response = app.test_client().put('/products/1', json={"name": "Updated Product"})  # Send PUT request to update the product
        data = response.get_json()  # Parse the response as JSON
        assert data['name'] == "Updated Product"  # Assert that the product name is updated correctly

# Test function to verify deleting a product by ID
def test_delete_product(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        response = app.test_client().delete('/products/1')  # Send DELETE request to delete the product
        assert response.status_code == 204  # Assert that the status code is 204 (No Content), indicating successful deletion

# Test function to verify listing all products
def test_list_all_products(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        response = app.test_client().get('/products')  # Send GET request to retrieve all products
        data = response.get_json()  # Parse the response as JSON
        assert len(data) > 0  # Assert that the product list contains at least one product

# Test function to verify finding products by name
def test_find_by_name(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        response = app.test_client().get('/products/search?name=Test Product')  # Send GET request to search by name
        data = response.get_json()  # Parse the response as JSON
        assert len(data) > 0  # Assert that the search results contain at least one product

# Test function to verify finding products by category
def test_find_by_category(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        response = app.test_client().get('/products/search?category=Category 1')  # Send GET request to search by category
        data = response.get_json()  # Parse the response as JSON
        assert len(data) > 0  # Assert that the search results contain at least one product

# Test function to verify finding products by availability status
def test_find_by_availability(app, new_product):
    with app.app_context():  # Start an app context to perform DB operations
        db.session.add(new_product)  # Add the new product to the session
        db.session.commit()  # Commit the transaction to the database
        response = app.test_client().get('/products/search?availability=true')  # Send GET request to search by availability
        data = response.get_json()  # Parse the response as JSON
        assert len(data) > 0  # Assert that the search results contain at least one product
