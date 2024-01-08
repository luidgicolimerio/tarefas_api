from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {
        'id':0,
        'responsável': 'Luidgi',
        'tarefa': 'Atualizar dev_api',
        'status': 'pendente'},
    {
        'id':1,
        'responsável': 'Colimerio',
        'tarefa': 'Desenvolver método GET',
        'status': 'concluido'},
]
@app.route('/tarefa/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def gerencia_tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = f'A Tarefa de ID {id} não existe.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        dados = dados['status']
        tarefas[id]['status'] = dados
        return jsonify(tarefas[id])
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Tarefa excluída com sucesso'})

@app.route('/tarefas', methods=['GET', 'POST'])
def lista_tarefas():
    if request.method == 'GET':
        return jsonify(tarefas)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])


if __name__ == '__main__':
    app.run(debug=True)