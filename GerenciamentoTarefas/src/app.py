# Flask: o framework que faz você se sentir um gênio por colocar um site no ar em 5 linhas
from flask import Flask, render_template, request, redirect, url_for
# Importando a galera do banco de dados
from database import criar_tabela, listar_tarefas, adicionar_tarefa, atualizar_tarefa, deletar_tarefa

app = Flask(__name__)

# Cria a tabela ao iniciar o app
criar_tabela()

# Página inicial — mostra a lista de tarefas, ou seja, sua lista de promessas não cumpridas
@app.route('/')
def index():
    tarefas = listar_tarefas()
    return render_template('index.html', tarefas=tarefas)

# Rota para adicionar uma nova tarefa
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        descricao = request.form['descricao']
        adicionar_tarefa(descricao)
        return redirect(url_for('index'))
    return render_template('adicionar.html')

# Rota para editar o status da tarefa
@app.route('/editar/<int:id_tarefa>', methods=['GET', 'POST'])
def editar(id_tarefa):
    if request.method == 'POST':
        concluida = 1 if 'concluida' in request.form else 0
        atualizar_tarefa(id_tarefa, concluida)
        return redirect(url_for('index'))
    tarefas = listar_tarefas()
    tarefa = next((t for t in tarefas if t[0] == id_tarefa), None)
    return render_template('editar.html', tarefa=tarefa)

# Rota para deletar uma tarefa.
@app.route('/deletar/<int:id_tarefa>')
def deletar(id_tarefa):
    deletar_tarefa(id_tarefa)
    return redirect(url_for('index'))

# Roda o app se esse arquivo for o principal.
if __name__ == '__main__':
    app.run(debug=True)