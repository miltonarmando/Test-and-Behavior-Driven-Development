import pytest
from models import Product, db
from flask import jsonify

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

def test_read_product(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        response = app.test_client().get('/products/1')
        data = response.get_json()
        assert data['name'] == "Test Product"

def test_update_product(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        response = app.test_client().put('/products/1', json={"name": "Updated Product"})
        data = response.get_json()
        assert data['name'] == "Updated Product"

def test_delete_product(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        response = app.test_client().delete('/products/1')
        assert response.status_code == 204

def test_list_all_products(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        response = app.test_client().get('/products')
        data = response.get_json()
        assert len(data) > 0

def test_find_by_name(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        response = app.test_client().get('/products/search?name=Test Product')
        data = response.get_json()
        assert len(data) > 0

def test_find_by_category(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        response = app.test_client().get('/products/search?category=Category 1')
        data = response.get_json()
        assert len(data) > 0

def test_find_by_availability(app, new_product):
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        response = app.test_client().get('/products/search?availability=true')
        data = response.get_json()
        assert len(data) > 0
