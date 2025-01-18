import factory  # Import the factory library for generating fake data
from models import Product, db  # Import the Product model and database session
from faker import Faker  # Import Faker to generate fake data

fake = Faker()  # Initialize a Faker instance to generate fake data

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    # Meta class is used to define the model and database session to be used
    class Meta:
        model = Product  # Specify the model to generate instances of (Product)
        sqlalchemy_session = db.session  # Use the database session for interacting with the database

    # Define the attributes for the Product model
    name = factory.LazyAttribute(lambda _: fake.word())  # Generate a random word for the product name
    category = factory.LazyAttribute(lambda _: fake.word())  # Generate a random word for the category
    price = factory.LazyAttribute(lambda _: fake.random_number(digits=2))  # Generate a random 2-digit number for the price
    availability = factory.LazyAttribute(lambda _: fake.boolean())  # Generate a random boolean for availability
