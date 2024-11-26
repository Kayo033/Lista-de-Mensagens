from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simula um banco de dados em memória
mensagens = []

# 1. Criar mensagem (POST)


@app.route('/mensagens', methods=['POST'])
def criar_mensagem():
    data = request.get_json()
    nova_mensagem = {"id": len(mensagens) + 1, "texto": data.get("texto", "")}
    mensagens.append(nova_mensagem)
    return jsonify(nova_mensagem), 201

# 2. Ler todas as mensagens (GET)


@app.route('/mensagens', methods=['GET'])
def ler_mensagens():
    return jsonify(mensagens)

# 3. Atualizar mensagem (PUT)


@app.route('/mensagens/<int:id>', methods=['PUT'])
def atualizar_mensagem(id):
    data = request.get_json()
    for mensagem in mensagens:
        if mensagem["id"] == id:
            mensagem["texto"] = data.get("texto", mensagem["texto"])
            return jsonify(mensagem)
    return jsonify({"error": "Mensagem não encontrada"}), 404

# 4. Excluir mensagem (DELETE)


@app.route('/mensagens/<int:id>', methods=['DELETE'])
def excluir_mensagem(id):
    global mensagens
    mensagens = [msg for msg in mensagens if msg["id"] != id]
    return jsonify({"message": "Mensagem excluída com sucesso"}), 200


# Rodar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
