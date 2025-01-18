from flask import Flask, render_template  # Importa as funções Flask e render_template do Flask
from service.routes import routes_blueprint  # Importa o blueprint de rotas para modularizar o código
from models import Product, db  # Importa o modelo Product e o objeto db configurados para interagir com o banco de dados

# Criação da instância do Flask
app = Flask(__name__)

# Configurações do Flask para o ambiente de teste e banco de dados
app.config['TESTING'] = True  # Habilita o modo de testes
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"  # Configura a URI para o banco de dados SQLite
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Desabilita o rastreamento de modificações no banco de dados (para evitar warnings)

# Inicializa o banco de dados com a configuração do app
db.init_app(app)

# Registra o blueprint de rotas para modularizar o código
app.register_blueprint(routes_blueprint)

# Rota principal da aplicação, renderiza a página inicial
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o template 'index.html'

# Rota para listar todos os produtos
@app.route('/products')
def products():
    # Busca todos os produtos do banco de dados usando a consulta do SQLAlchemy
    products = Product.query.all()
    return render_template('products.html', products=products)  # Passa os produtos para o template 'products.html'

# Verifica se o script está sendo executado diretamente e, em caso afirmativo, inicia o app
if __name__ == "__main__":
    with app.app_context():  # Cria o contexto da aplicação para garantir que o banco de dados e as tabelas sejam criados
        db.create_all()  # Cria todas as tabelas no banco de dados
    app.run(debug=True)  # Inicia o servidor Flask no modo de depuração
