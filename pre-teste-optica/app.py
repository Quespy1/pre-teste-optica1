from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///respostas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo da tabela
class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pergunta1 = db.Column(db.Text, nullable=False)
    pergunta2 = db.Column(db.Text, nullable=False)
    pergunta3 = db.Column(db.Text, nullable=False)
    pergunta4 = db.Column(db.Text, nullable=False)
    pergunta5 = db.Column(db.Text, nullable=False)

# Página do formulário
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            nova_resposta = Resposta(
                pergunta1=request.form['pergunta1'],
                pergunta2=request.form['pergunta2'],
                pergunta3=request.form['pergunta3'],
                pergunta4=request.form['pergunta4'],
                pergunta5=request.form['pergunta5']
            )
            db.session.add(nova_resposta)
            db.session.commit()
            return 'Obrigado por participar!'
        except Exception as e:
            return f'Ocorreu um erro: {e}'
    return render_template('formulario.html')

# Rota opcional para inicializar o banco (use apenas uma vez)
@app.route('/init-db')
def init_db():
    with app.app_context():
        db.create_all()
    return 'Banco de dados inicializado com sucesso!'

# Inicializador local
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
