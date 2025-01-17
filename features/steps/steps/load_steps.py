from behave import given, when, then
from models import Product
from app import db

@given("there are products in the database")
def step_impl(context):
    db.create_all()
    context.product = Product(name="Sample Product", category="Sample Category", price=20.0, availability=True)
    db.session.add(context.product)
    db.session.commit()

@when("I query the products")
def step_impl(context):
    context.response = context.client.get("/products")

@then("I should get a list of products")
def step_impl(context):
    assert len(context.response.json) > 0
