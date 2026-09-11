# Importar bibliotecas
from flask import Flask, render_template, request

# Criar objeto flask "Apelido - app"
app = Flask(__name__)

# Base FAKE
base_fake= []

# Base login
base_login= []

#Base Recursos
base_recursos= []

#Base categorias
base_categorias= []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atividades/criar', methods=['GET','POST'])
def criar_atividade():
    if request.method == 'POST':
        # Aqui é onde recebe os dados do formulário
        nome_atividade = request.form.get('form_nome')
        descricao_atividade = request.form.get('form_descricao')
        data_atividade = request.form.get('form_data')
        quantidade = request.form.get('form_quantidade')
        categoria_atividade = request.form.getlist('form_categoria')
        responsavel_atividade = request.form.get('form_responsavel')
        prioridade_atividade = request.form.get('form_prio')
        dados = {
            'nome': nome_atividade,
            'descricao': descricao_atividade,
            'data': data_atividade,
            'categoria': categoria_atividade,
            'prioridade': prioridade_atividade,
            'quantidade': quantidade,
            'responsavel_atividade': responsavel_atividade,
        }
        print(f'Dados cadastrados{dados}')
        base_fake.append(dados)
        print(f'base_fake {base_fake}')
        return render_template('listar_atividades.html', dados_atividades=base_fake)

    return render_template('criar_atividade.html')

@app.route('/atividades/listar')
def listar_atividades():
    return render_template('listar_atividades.html', dados_atividades=base_fake)

@app.route('/usuario/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('form_usuario')
        data = request.form.get('form_data')
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')
        dados_pessoas = {
            'usuario': usuario,
            'data': data,
            'senha': senha,
            'email': email,
        }
        base_login.append(dados_pessoas)
        return render_template('pessoa.html', dados_pessoas=base_login)
    return render_template('login.html')

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html', dados_pessoas=base_login)

@app.route('/recursos/solicitar', methods=['GET', 'POST'])
def solicitar_recursos():
    if request.method == 'POST':
        nome_recurso = request.form.get('form_recurso')
        nome = request.form.get('form_nome')
        data_recurso = request.form.get('form_data')
        descricao = request.form.get('form_descricao')
        dados_recursos = {
            'nome_recurso': nome_recurso,
            'nome': nome,
            'data_recurso': data_recurso,
            'descricao': descricao
        }
        base_recursos.append(dados_recursos)
        return render_template('recursos.html', dados_recursos=base_recursos)
    return render_template('solicitar_recursos.html', dados_recursos=base_recursos)

@app.route('/recursos')
def recursos():
    return render_template('recursos.html', dados_recursos=base_recursos)

@app.route('/categorias/localizar', methods=['GET', 'POST'])
def localizar_categorias():
    if request.method == 'POST':
        nome_categoria = request.form.get('form_nome_categoria')
        descricao_categoria = request.form.get('form_descricao')
        responsavel_categoria = request.form.get('form_responsavel')
        dados_categorias = {
            'nome_categoria': nome_categoria,
            'descricao_categoria': descricao_categoria,
            'responsavel_categoria': responsavel_categoria
        }
        base_categorias.append(dados_categorias)
        return render_template('categorias.html', base_categorias=base_categorias)
    return render_template('localizar_categorias.html', base_categorias=base_categorias)

@app.route('/categorias')
def categorias():
    return render_template('categorias.html', dados_categorias=base_categorias)

# Iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
# Nada deve ser colocado abaixo


