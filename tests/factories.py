import factory
from models import Product, db
from faker import Faker

fake = Faker()

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = db.session  # Use sua sessão de banco de dados aqui

    name = factory.LazyAttribute(lambda _: fake.word())
    category = factory.LazyAttribute(lambda _: fake.word())
    price = factory.LazyAttribute(lambda _: fake.random_number(digits=2))
    availability = factory.LazyAttribute(lambda _: fake.boolean())
