from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# class Noticias(db.Model):
#     __tablename__ = 'noticias'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     titulo = db.Column(db.String(100), nullable=False)
#     descricao = db.Column(db.String(1000), nullable=False)
#     categoria = db.Column(db.String(100), nullable=False)
#     resumo = db.Column(db.String(120), nullable=False)
#     autor = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.String(6), nullable=False)
#     image_data = db.Column(db.String(6), nullable=False)

#     def __init__(self, titulo, descricao, categoria, resumo, autor, date, image_data):
#         self.titulo = titulo
#         self.descricao = descricao
#         self.categoria = categoria
#         self.resumo = resumo
#         self.autor = autor
#         self.date = date
#         self.image_data = image_data


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(102), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
