from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Empresa, Funcionario, sistema
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('senha')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.senha, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.navegar'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        classe = request.form.get('classe')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        else:
            new_user = User(email=email, senha=generate_password_hash(
                            senha, method='sha256'), classe=classe)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            if classe == "Funcionário":
                return redirect(url_for('auth.registrar_func'))
            else:
                return redirect(url_for('auth.registrar_emp'))

    return render_template("registrar_user.html", user=current_user)


@auth.route('/registrar-func', methods=['GET', 'POST'])
@login_required
def registrar_func():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        cargo = request.form.get('cargo')
        cpf = request.form.get('cpf')
        
        novo_func = Funcionario(nome=nome, cargo=cargo, telefone=telefone, cpf=cpf, 
                                sistema_id=sistema.id, user_id=current_user.id)
        db.session.add(novo_func)
        db.session.commit()
        
        return redirect(url_for('views.navegar'))
        
    return render_template('registrar_func.html', user=current_user)

@auth.route('/registrar-emp', methods=['GET', 'POST'])
@login_required
def registrar_emp():
    if request.method == 'POST':
        cnpj = request.form.get('cnpj')
        nicho = request.form.get('nicho')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        

        nova_emp = Empresa(cnpj=cnpj, nicho=nicho, telefone=telefone, endereco=endereco,
                            cidade=cidade, estado=estado, cep=cep,  sistema_id=sistema.id,
                            user_id=current_user.id)
        db.session.add(nova_emp)
        db.session.commit()
        
        
        return redirect(url_for('views.navegar'))
        
    return render_template('registrar_emp.html', user=current_user)