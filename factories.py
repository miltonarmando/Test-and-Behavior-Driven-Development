from faker import Faker

fake = Faker()

def create_fake_product():
    """Generate a fake product"""
    return {
        "id": fake.uuid4(),
        "name": fake.word(),
        "category": fake.word(),
        "price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        "availability": fake.boolean(),
    }
