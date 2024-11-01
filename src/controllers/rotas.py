from flask import Blueprint, render_template, request,jsonify, redirect, url_for, flash
import requests
from models.models import db, Usuario

#defina uma variavel para receber o Blueprint(), seus parametros sao: 
# ('nome do Blueprint', import_name), __name__ é obrigatorio
app = Blueprint('rotas_do_terreo', __name__)

# rodar no xamp por enquanto
# src/models/api.php
PHP_API_URL = 'http://localhost/api.php'  # URL da sua API PHP


# rota teste para listar todas as rotas existentes
@app.route('/rotas', methods=['GET'])
@app.route("/rotas/", methods=['GET'])
def home():
    
    rotas = {
        "rotas":{
            "inicio":{
                "1":"http://127.0.0.1:5000/",
                "2":"http://127.0.0.1:5000/inicio",
                "3":"http://127.0.0.1:5000/inicio/",
            },
            "cadastro":{
                "1":"http://127.0.0.1:5000/cadastro",
            },
            "login":{
                "1":"http://127.0.0.1:5000/login/",
            },
            "terreo / entrada":{
                "1":"http://127.0.0.1:5000/terreo",
                "2":"http://127.0.0.1:5000/terreo/",
                "3":"http://127.0.0.1:5000/entrada/",
                "4":"http://127.0.0.1:5000/entrada/terreo/",
            },
            "entrada-biblioteca":{
                "1":"http://127.0.0.1:5000/entrada/biblioteca/",
            },
            "entrada-cantina":{
                "1":"http://127.0.0.1:5000/entrada/cantina/",
            },
            "entrada-educart":{
                "1":"http://127.0.0.1:5000/entrada/educart",
            },
            "entrada-elevador-bibliotexa":{
                "1":"http://127.0.0.1:5000/entrada/elevador/biblioteca/",
            },
            "entrada-elevador-sala-mat":{
                "1":"http://127.0.0.1:5000/entrada/elevador/sala-mat/",
            },
            "entrada-escada-biblioteca":{
                "1":"http://127.0.0.1:5000/entrada/escada/biblioteca/",
            },
            "entrada-escada-educart":{
                "1":"http://127.0.0.1:5000/entrada/escada/educart/",
            },
            "entrada-escada-sala-mat":{
                "1":"http://127.0.0.1:5000/entrada/escada/sala-mat/",
            },
            "entrada-laboratorio":{
                "1":"http://127.0.0.1:5000/entrada/laboratorio/",
            },
            "entrada-sala-mat":{
                "1":"http://127.0.0.1:5000/entrada/sala-mat/",
            },
            "entrada-secretaria":{
                "1":"http://127.0.0.1:5000/entrada/secretaria/",
            },
            "primeiro-andar":{
                "1":"http://127.0.0.1:5000/primeiro_andar",
                "2":"http://127.0.0.1:5000/primeiro_andar/",
                "3":"http://127.0.0.1:5000/primeiro-andar",
                "4":"http://127.0.0.1:5000/primeiro-andar/",
            },
            "segundo-andar":{
                "1":"http://127.0.0.1:5000/segundo_andar",
                "2":"http://127.0.0.1:5000/segundo_andar/",
                "3":"http://127.0.0.1:5000/segundo-andar",
                "4":"http://127.0.0.1:5000/segundo-andar/",
            },
            "terceiro-andar":{
                "1":"http://127.0.0.1:5000/terceiro_andar",
                "2":"http://127.0.0.1:5000/terceiro_andar/",
                "3":"http://127.0.0.1:5000/terceiro-andar",
                "4":"http://127.0.0.1:5000/terceiro-andar/",
            },
            "pagina-pdf":{
                "1":"http://127.0.0.1:5000/pagina-pdf",
                "2":"http://127.0.0.1:5000/pagina-pdf/",
            },
            "destino":{
                "1":"http://127.0.0.1:5000/destino",
                "2":"http://127.0.0.1:5000/destino/",
                "3":"http://127.0.0.1:5000/definir_destino",
                "4":"http://127.0.0.1:5000/definir_destino/",
            },
    }
}
    return rotas

# todas as rotas para requsts da api estao aqui
# so funciona se o xamp estiver configurado 
# -------------------------------------------------------------------

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get(PHP_API_URL)
    return jsonify(response.json())

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    response = requests.post(PHP_API_URL, json=data)
    return jsonify(response.json())

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    data['id'] = user_id
    response = requests.put(PHP_API_URL, json=data)
    return jsonify(response.json())

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    response = requests.delete(PHP_API_URL, json={'id': user_id})
    return jsonify(response.json())

# -------------------------------------------------------------------
@app.route("/", methods=['GET'])
@app.route("/inicio", methods=['GET'])
@app.route("/inicio/", methods=['GET'])
def index():
	return render_template('/inicio/inicio.html')

@app.route('/cadastro', methods=['GET','POST'])
@app.route('/cadastro/', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Verifica se o email já está em uso
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash('Este email já está em uso. Tente novamente.', 'error')
            return redirect(url_for('cadastro'))

        
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('/cadastro/cadastro.html')

# -------------------------------------------------------------------


@app.route("/login", methods=['GET','POST'])
@app.route("/login/", methods=['GET','POST'])
def login():
    return render_template("/login/login.html")

# -------------------------------------------------------------------

# rota da entrada que mostra o terreo completo 'sem rotas definidas'
@app.route("/terreo", methods=['GET'])
@app.route("/terreo/", methods=['GET'])
@app.route("/entrada/", methods=['GET'])
@app.route("/entrada/terreo/", methods=['GET'])
def entrada_terreo():
    return render_template("/terreoo/terreo.html")


# rota da entrada para a biblioteca
@app.route('/entrada/biblioteca/', methods=['GET'])
def entrada_bilbioteca():
    return render_template('/terreoo/entrada_biblioteca.html')


# rota da entrada para a cantina
@app.route('/entrada/cantina/', methods=['GET'])
def entrada_cantina():
    return render_template("/terreoo/entrada_cantina.html")


# rota da entrada para o educart
@app.route("/entrada/educart/", methods=['GET'])
def entrada_educart():
    return render_template("/terreoo/entrada_educard.html")


# rora da entrada para o elevador biblioteca
@app.route("/entrada/elevador/biblioteca/", methods=['GET'])
def entrada_elevador_biblioteca():
    return render_template("/terreoo/entrada_elev_bib.html")


# rota da entrada do elevador sala matricula
@app.route("/entrada/elevador/sala-mat/", methods=['GET'])
def entrada_elevado_matricula():
    return render_template("/terreoo/entrada_elev_mat.html")


# rota da entrada escada biblioteca
@app.route("/entrada/escada/biblioteca/", methods=['GET'])
def entrada_escada_biblioteca():
    return render_template("/terreoo/entrada_esc_bib.html")


# rota  entrada da escada educard
@app.route("/entrada/escada/educart/", methods=['GET'])
def entrada_escada_educart():
    return render_template("/terreoo/entrada_esc_educart.html")

# rota entrada da escada da sala de matriculas
@app.route("/entrada/escada/sala-mat/", methods=['GET'])
def entrada_escada_matricula():
    return render_template("/terreoo/entrada_esc_sala_mat.html")


# rota entrada laboratorio
@app.route("/entrada/laboratorio/", methods=['GET'])
def entrada_laboratorio():
    return render_template("/terreoo/entrada_laboratorio.html")


# rota entrada sala de matricula
@app.route("/entrada/sala-mat/", methods=['GET'])
def entrada_sala_matricula():
    return render_template("/terreoo/entrada_sala_mat.html")


# rota entrada para secretaria
@app.route("/entrada/secretaria/", methods=['GET'])
def entrada_secretari():
    return render_template("/terreoo/entrada_secretaria.html")

#------------------------------------------------------------
@app.route("/primeiro_andar", methods=['GET'])
@app.route("/primeiro_andar/", methods=['GET'])
@app.route("/primeiro-andar", methods=['GET'])
@app.route("/primeiro-andar/", methods=['GET'])
def andar_1():
    return render_template("/andar-1/andar-1.html")


@app.route("/segundo_andar", methods=['GET'])
@app.route("/segundo_andar/", methods=['GET'])
@app.route("/segundo-andar", methods=['GET'])
@app.route("/segundo-andar/", methods=['GET'])
def andar_2():
    return render_template("/andar-2/andar-2.html")



@app.route("/terceiro_andar", methods=['GET'])
@app.route("/terceiro_andar/", methods=['GET'])
@app.route("/terceiro-andar", methods=['GET'])
@app.route("/terceiro-andar/", methods=['GET'])
def andar_3():
    return render_template("/andar-3/andar-3.html")


#-------------------------------------------------------------



@app.route("/pagina-pdf", methods=['GET','POST'])
@app.route("/pagina-pdf/", methods=['GET','POST'])
def pag_pdf():
    return render_template("pagina_pdf/pag_pdf.html")

#-------------------------------------------------------------

@app.route("/destino", methods=['GET'])
@app.route("/destino/", methods=['GET'])
@app.route("/definir_destino", methods=['GET'])
@app.route("/definir_destino/", methods=['GET'])
def definir_destino():
    return render_template("destino/definir_destino.html")



@app.route("/teste/", methods=['GET'])
def teste():
    return render_template('testee/teste.html')
