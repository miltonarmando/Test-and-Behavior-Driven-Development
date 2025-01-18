from behave import given, when, then  # Importing Behave's step decorators for BDD
from models import Product  # Importing the Product model
from app import db  # Importing the database instance

# Given step to set up products in the database
@given("there are products in the database")
def step_impl(context):
    db.create_all()  # Create all database tables
    # Creating a sample product with predefined attributes
    context.product = Product(name="Sample Product", category="Sample Category", price=20.0, availability=True)
    db.session.add(context.product)  # Add the product to the database session
    db.session.commit()  # Commit the transaction to save the product in the database

# When step to query the products from the API
@when("I query the products")
def step_impl(context):
    context.response = context.client.get("/products")  # Sending a GET request to the /products endpoint

# Then step to assert that the response contains a list of products
@then("I should get a list of products")
def step_impl(context):
    assert len(context.response.json) > 0  # Assert that the response JSON contains at least one product
