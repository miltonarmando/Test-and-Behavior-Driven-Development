import pytest
from app import app, db, Product

# Define a pytest fixture to set up and tear down the test environment
@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        with app.app_context():
            db.drop_all()

# Helper function to add a product to the test database
def add_product(name, category, price, availability):
    product = Product(name=name, category=category, price=price, availability=availability)
    db.session.add(product)
    db.session.commit()
    return product

# Test: List all products
def test_list_products(client):
    # Limpar o banco de dados antes de adicionar novos produtos
    Product.query.delete()
    db.session.commit()

    # Adicionar produtos
    add_product("Laptop", "Electronics", 1200.50, True)
    add_product("Desk", "Furniture", 250.75, False)

    # Verificar se os produtos foram listados corretamente
    response = client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]["name"] == "Laptop"
    assert data[1]["name"] == "Desk"


# Test: Search products by name
def test_search_products_by_name(client):
    add_product("Laptop", "Electronics", 1200.50, True)
    add_product("Desk", "Furniture", 250.75, False)

    response = client.get("/products/search?name=Laptop")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Laptop"

# Test: Search products by category
def test_search_products_by_category(client):
    add_product("Laptop", "Electronics", 1200.50, True)
    add_product("Desk", "Furniture", 250.75, False)

    response = client.get("/products/search?category=Furniture")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["category"] == "Furniture"

# Test: Search products by availability
def test_search_products_by_availability(client):
    add_product("Laptop", "Electronics", 1200.50, True)
    add_product("Desk", "Furniture", 250.75, False)

    response = client.get("/products/search?availability=true")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["availability"] is True

# Test: Create a new product
def test_create_product(client):
    product_data = {
        "name": "Phone",
        "category": "Electronics",
        "price": 699.99,
        "availability": True
    }
    response = client.post("/products", json=product_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Phone"

# Test: Update an existing product
def test_update_product(client):
    product = add_product("Laptop", "Electronics", 1200.50, True)

    update_data = {
        "name": "Gaming Laptop",
        "price": 1500.75
    }
    response = client.put(f"/products/{product.id}", json=update_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Gaming Laptop"
    assert data["price"] == 1500.75

# Test: Delete a product
def test_delete_product(client):
    product = add_product("Laptop", "Electronics", 1200.50, True)

    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204

    # Verify the product was deleted
    response = client.get("/products")
    data = response.get_json()
    assert len(data) == 0