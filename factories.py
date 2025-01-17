from faker import Faker
import random

fake = Faker()

CATEGORIES = ["Electronics", "Clothing", "Books", "Toys"]
AVAILABILITY = [True, False]

def fake_product():
    """Gera um produto fictício"""
    return {
        "id": random.randint(1, 1000),
        "name": fake.unique.word().capitalize(),
        "category": random.choice(CATEGORIES),
        "price": round(random.uniform(10.0, 1000.0), 2),
        "available": random.choice(AVAILABILITY),
    }

# Exemplo de geração de produtos fictícios
if __name__ == "__main__":
    print([fake_product() for _ in range(5)])
