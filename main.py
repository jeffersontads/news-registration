from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db
from app.models import User


class Noticias(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(1000), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    resumo = db.Column(db.String(120), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(6), nullable=False)
    image_data = db.Column(db.String(6), nullable=False)

    def __init__(self, titulo, descricao, categoria, resumo, autor, date, image_data):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.resumo = resumo
        self.autor = autor
        self.date = date
        self.image_data = image_data


@app.route('/')
def home():
    data_noticias = db.session.query(Noticias)
    return render_template('home.html', data=data_noticias)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('list'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/list', methods=['GET', 'POST'])
def list():
    data_noticias = db.session.query(Noticias)
    return render_template('/list.html', data=data_noticias)


@ app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        categoria = request.form['categoria']
        resumo = request.form['resumo']
        autor = request.form['autor']
        date = request.form['date']
        image_data = request.form['file']

        add_data = Noticias(titulo, descricao, categoria,
                            resumo, autor, date, image_data)

        db.session.add(add_data)
        db.session.commit()

        # flash("A notícia foi cadastrada corretamente.")

        return redirect(url_for('list'))

    return render_template('input.html')


@ app.route('/edit/<int:id>')
def edit_data(id):
    data_noticias = Noticias.query.get(id)
    return render_template('edit.html', data=data_noticias)


@ app.route('/process_edit', methods=['POST', 'GET'])
def process_edit():
    data_noticias = Noticias.query.get(request.form.get('id'))

    data_noticias.titulo = request.form['titulo']
    data_noticias.descricao = request.form['descricao']
    data_noticias.categoria = request.form['categoria']
    data_noticias.resumo = request.form['resumo']
    data_noticias.autor = request.form['autor']
    data_noticias.date = request.form['date']
    data_noticias.image_data = request.form['file']

    db.session.commit()

    # flash('Notícia editada com sucesso!!')

    return redirect(url_for('list'))


@ app.route('/delete/<int:id>')
def delete(id):
    data_noticias = Noticias.query.get(id)
    db.session.delete(data_noticias)
    db.session.commit()

    # flash('Notícia deletada com sucesso!')

    return redirect(url_for('list'))


@ app.route('/single-post/<int:id>')
def single_post(id):
    data_noticias = Noticias.query.get(id)
    return render_template('/single-post.html', data=data_noticias)


app.run(debug=True)
