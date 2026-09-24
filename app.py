# Importar bibliotecas
from flask import Flask, render_template, request, flash
from sqlalchemy.exc import SQLAlchemyError

from models import Pessoa, db_session

# Criar objeto flask "Apelido - app"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'corinthians'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atividades/criar', methods=['GET','POST'])
def criar_atividade():
    if request.method == 'POST':
        nome_atividade = request.form.get('form_nome')
        descricao_atividade = request.form.get('form_descricao')
        data_atividade = request.form.get('form_data')
        quantidade = request.form.get('form_quantidade')
        categoria_atividade = request.form.getlist('form_categoria')
        responsavel_atividade = request.form.get('form_responsavel')
        prioridade_atividade = request.form.get('form_prio')

        return render_template('listar_atividades.html')

    return render_template('criar_atividade.html')

@app.route('/atividades/listar')
def listar_atividades():
    return render_template('listar_atividades.html')

@app.route('/pessoa/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')

        return render_template('pessoa.html')
    return render_template('login.html')

@app.route('/pessoa/criar', methods=['GET', 'POST'])
def criar_pessoa():
    # Verifica o metodo, se for GET vai para a pagina do formulario
    if request.method == 'GET':
        return render_template('criar_pessoa.html')

    #Recebe os dados via Post
    nome_form = request.form.get('form_nome')
    email_form = request.form.get('form_email')
    senha_form = request.form.get('form_senha')
    print(f'nome: {nome_form}, email: {email_form}, senha: {senha_form}')

    if not nome_form:
        flash('Preencha o campo!', 'error')
        return render_template('criar_pessoa.html')

    try:
        # Cria uma nova pessoa e adiciona na base de dados
        nova_pessoa = Pessoa(nome=nome_form, email=email_form, senha=senha_form)

        # Inicializa a sessão com o banco de dados
        db_session.add(nova_pessoa)
        db_session.commit()
        return render_template('criar_pessoa.html')

    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao salvar pessoa no banco: {e}')
        flash('Erro ao salvar pessoa no banco!', 'error')
        return render_template('criar_pessoa.html')
    except Exception as e:
        db_session.rollback()
        print(f'Erro inesperado: {e}')
        flash('Erro inesperado!', 'error')
        return render_template('criar_pessoa.html')

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

@app.route('/recursos/solicitar', methods=['GET', 'POST'])
def solicitar_recursos():
    if request.method == 'POST':
        nome_recurso = request.form.get('form_recurso')
        nome = request.form.get('form_nome')
        data_recurso = request.form.get('form_data')
        descricao = request.form.get('form_descricao')
        return render_template('recursos.html')
    return render_template('solicitar_recursos.html')

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/categorias/localizar', methods=['GET', 'POST'])
def localizar_categorias():
    if request.method == 'POST':
        nome_categoria = request.form.get('form_nome_categoria')
        descricao_categoria = request.form.get('form_descricao')
        responsavel_categoria = request.form.get('form_responsavel')

        return render_template('categorias.html')
    return render_template('localizar_categorias.html')

@app.route('/categorias')
def categorias():
    return render_template('categorias.html')

# Iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
# Nada deve ser colocado abaixo


