from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import Empresa, Funcionario, User, Servico, sistema
from . import db
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("homepage.html", user=current_user)

@views.route('/servicos')
def navegar():
    return render_template("servicos.html", user=current_user, sistema=sistema)

@views.route('/tela-inicial')
@login_required
def tela_inicial():
    if current_user.classe == 'Funcionário':
        template = "tela_inicial_func.html"
    else:
        template = "tela_inicial_emp.html"
        
    return render_template(template, user=current_user)

@views.route('/perfil-func')
@login_required
def perfil_func():
    return render_template("perfil_func.html", user=current_user)
    
@views.route('/perfil-emp')
@login_required
def perfil_emp():
    
    return render_template("perfil_emp.html", user=current_user)
    
@views.route('/editar-servicos',  methods=['GET', 'POST'])
@login_required
def editar_servicos():
    return render_template("editar_servicos.html", user=current_user)

@views.route('/parcerias')
@login_required
def parcerias():
    return render_template('parcerias.html', user=current_user)

@views.route('/servico', methods=['GET', 'POST'])
@login_required
def add_servico():
    if request.method == 'POST':
        nome = request.form.get('nome_servico')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        
        novo_servico = Servico(nome=nome, descricao=descricao, preco=preco, user_id=current_user.id,  sistema_id=sistema.id)
        db.session.add(novo_servico)
        db.session.commit()
        
        return redirect(url_for('views.editar_servicos'))

    return render_template("add_servico.html", user=current_user, sistema=sistema)

