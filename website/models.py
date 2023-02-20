from . import db
from flask_login import UserMixin


class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    descricao = db.Column(db.String(10000))
    preco = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sistema_id = db.Column(db.Integer, db.ForeignKey('sistema.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    classe = db.Column(db.String(150))
    servicos = db.relationship('Servico')
    
class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cargo = db.Column(db.String(150))
    cpf = db.Column(db.String(150))
    telefone = db.Column(db.String(150))
    sistema_id = db.Column(db.Integer, db.ForeignKey('sistema.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(150))
    nicho = db.Column(db.String(150))
    telefone = db.Column(db.String(150))
    endereco = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    estado = db.Column(db.String(150))
    cep = db.Column(db.String(150))
    sistema_id = db.Column(db.Integer, db.ForeignKey('sistema.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     
class Sistema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servicos_disponiveis = db.relationship('Servico')
    funcionarios_cadastrados = db.relationship('Funcionario')
    empresas_cadastradas = db.relationship('Empresa')

sistema = Sistema()