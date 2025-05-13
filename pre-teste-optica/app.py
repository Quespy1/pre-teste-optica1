from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://respostas_optica_user:KrYB0q6DcNFu4lCrx2t2wmnYL4Kh4RBO@dpg-d0hmj7buibrs739t58i0-a/respostas_optica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pergunta1 = db.Column(db.Text, nullable=False)
    pergunta2 = db.Column(db.Text, nullable=False)
    pergunta3 = db.Column(db.Text, nullable=False)
    pergunta4 = db.Column(db.Text, nullable=False)
    pergunta5 = db.Column(db.Text, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
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
    return render_template('formulario.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
