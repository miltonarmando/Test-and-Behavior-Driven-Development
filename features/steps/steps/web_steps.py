from behave import given, when, then  # Importing Behave's step decorators for BDD
from app import create_app  # Importing the function to create the Flask application

# Given step to navigate to the products page
@given('I am on the products page')
def step_impl(context):
    context.client = create_app().test_client()  # Creating a test client to simulate requests to the application

# When step to search for products by name
@when('I search for products by name "{name}"')
def step_impl(context, name):
    context.response = context.client.get(f"/products/search?name={name}")  # Sending a GET request to search for products by name

# Then step to check that the product with the given name is in the response
@then('I should see the product "{name}"')
def step_impl(context, name):
    products = context.response.json  # Getting the list of products from the response in JSON format
    assert any(product['name'] == name for product in products)  # Assert that at least one product in the response has the given name
