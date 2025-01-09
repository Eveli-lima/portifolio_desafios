from flask import Flask, render_template, request
# Flask cria uma aplicação web.
# render_template: Função usada para renderizar arquivos HTML (templates)
# request: Usado para acessar os dados enviados através de formulários.
from logic import comparar_idade  # Importando a função

# Instanciando o Flask:
app = Flask(__name__)

# Definir rota:
@app.route('/')
def home():
    return render_template('index.html')

# rota página de exercícios:
@app.route('/pag_exercicios', methods=['GET', 'POST'])
def comparar_idade_view(): # o sufixo view indica que a função é responsável por lidar com a exibição de uma página (ou "view" no contexto do Flask).
    mensagem = ''
    if request.method == 'POST':
        idade = int(request.form['idade'])
        mensagem = comparar_idade(idade)  # Usando a função importada
    return render_template('pag_exercicios.html', mensagem=mensagem)

# Rodando a aplicação:
# Esse bloco de código garante que o servidor Flask seja iniciado apenas quando o script for executado diretamente (e não importado como módulo).
if __name__ == '__main__':
    app.run(debug=True) #  O debug=True permite reiniciar automaticamente o servidor quando houver alterações no código e exibir erros detalhados.