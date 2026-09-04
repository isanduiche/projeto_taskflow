# Importar bibliotecas
from flask import Flask, render_template, request

# Criar objeto flask "Apelido - app"
app = Flask(__name__)

# Base FAKE
base_fake= []

# Base login
base_login= []

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
        categoria_atividade = request.form.getlist('form_categoria')
        prioridade_atividade = request.form.get('form_prio')
        dados = {
            'nome': nome_atividade,
            'descricao': descricao_atividade,
            'data': data_atividade,
            'categoria': categoria_atividade,
            'prioridade': prioridade_atividade
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
        senha = request.form.get('form_senha')
        dados_pessoas = {
            'usuario': usuario,
            'data': data,
            'senha': senha
        }
        base_login.append(dados_pessoas)
        return render_template('pessoa.html', dados_pessoas=base_login)
    return render_template('login.html')

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html', dados_pessoas=base_login)

# Iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
# Nada deve ser colocado abaixo


