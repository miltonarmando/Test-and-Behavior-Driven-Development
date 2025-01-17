import pytest
from models import Product
from app import app, db

@pytest.fixture
def app():
    app = app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def new_product():
    return Product(name="Test Product", category="Category 1", price=10.0, availability=True)

def test_create_product(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        product = Product.query.first()
        assert product.name == "Test Product"

def test_update_product(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        product = Product.query.first()
        product.name = "Updated Product"
        db.session.commit()
        assert product.name == "Updated Product"

def test_delete_product(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        product = Product.query.first()
        db.session.delete(product)
        db.session.commit()
        assert Product.query.count() == 0

def test_list_all_products(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        products = Product.query.all()
        assert len(products) > 0

def test_find_product_by_name(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        product = Product.query.filter_by(name="Test Product").first()
        assert product is not None

def test_find_product_by_category(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        product = Product.query.filter_by(category="Category 1").first()
        assert product is not None

def test_find_product_by_availability(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        product = Product.query.filter_by(availability=True).first()
        assert product is not None
