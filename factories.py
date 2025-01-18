from faker import Faker  # Importa a biblioteca Faker para gerar dados falsos
import random  # Importa a biblioteca random para gerar valores aleatórios

fake = Faker()  # Cria uma instância do Faker para gerar dados aleatórios

# Lista de categorias para os produtos fictícios
CATEGORIES = ["Electronics", "Clothing", "Books", "Toys"]
# Lista de estados de disponibilidade dos produtos (disponível ou não)
AVAILABILITY = [True, False]

def fake_product():
    """Gera um produto fictício"""
    # Gera um dicionário representando um produto com atributos aleatórios
    return {
        "id": random.randint(1, 1000),  # Gera um ID aleatório para o produto
        "name": fake.unique.word().capitalize(),  # Gera um nome único e capitalizado para o produto
        "category": random.choice(CATEGORIES),  # Escolhe uma categoria aleatória da lista CATEGORIES
        "price": round(random.uniform(10.0, 1000.0), 2),  # Gera um preço aleatório entre 10 e 1000, com duas casas decimais
        "available": random.choice(AVAILABILITY),  # Escolhe aleatoriamente se o produto está disponível ou não
    }

# Exemplo de geração de produtos fictícios
if __name__ == "__main__":
    # Gera uma lista com 5 produtos fictícios e imprime no console
    print([fake_product() for _ in range(5)])
