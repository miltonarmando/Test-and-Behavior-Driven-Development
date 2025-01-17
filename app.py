from flask import Flask, render_template
from service.routes import routes_blueprint # Apenas importa o blueprint
from models import Product, db  # Certifique-se de que db e Product estão configurados corretamente

app = Flask(__name__)
app.config['TESTING'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(routes_blueprint)  # Registra o blueprint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    # Busca todos os produtos do banco de dados
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Garante que o banco de dados e as tabelas sejam criados
    app.run(debug=True)
