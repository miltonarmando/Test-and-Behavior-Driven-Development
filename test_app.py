import pytest
from app import app, db, Product

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_product(client):
    response = client.post("/products", json={
        "name": "Product1",
        "category": "Category1",
        "price": 99.99,
        "availability": True
    })
    assert response.status_code == 201

def test_read_product(client):
    product = Product(name="Test", category="Category", price=10.0, availability=True)
    db.session.add(product)
    db.session.commit()
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200
    assert response.json["name"] == "Test"

def test_update_product(client):
    product = Product(name="Test", category="Category", price=10.0, availability=True)
    db.session.add(product)
    db.session.commit()
    response = client.put(f"/products/{product.id}", json={"name": "UpdatedName"})
    assert response.status_code == 200
    assert response.json["name"] == "UpdatedName"

def test_delete_product(client):
    product = Product(name="Test", category="Category", price=10.0, availability=True)
    db.session.add(product)
    db.session.commit()
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204

def test_list_products(client):
    db.session.add_all([
        Product(name="Product1", category="Category1", price=10.0, availability=True),
        Product(name="Product2", category="Category2", price=20.0, availability=False),
    ])
    db.session.commit()
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json) == 2
