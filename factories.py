from faker import Faker

# Initialize the Faker object to generate fake data
fake = Faker()

def create_fake_product():
    """
    Generate a fake product with random attributes.
    
    Returns a dictionary with the following keys:
    - 'id': A unique identifier for the product (UUID)
    - 'name': A random product name (word)
    - 'category': A random product category (word)
    - 'price': A random price, rounded to two decimal places
    - 'availability': A random boolean indicating whether the product is available
    """
    return {
        # Generate a unique product ID using a UUID
        "id": fake.uuid4(),
        
        # Generate a random word for the product name
        "name": fake.word(),
        
        # Generate a random word for the product category
        "category": fake.word(),
        
        # Generate a random price with 3 digits before the decimal and 2 digits after
        "price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        
        # Generate a random boolean value indicating availability (True or False)
        "availability": fake.boolean(),
    }