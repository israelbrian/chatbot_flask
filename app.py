from flask import Flask, request, jsonify
from flask_cors import CORS
from responses import get_bot_response

app = Flask(__name__)
CORS(app)

# Rota para receber mensagens do usuário e retornar a resposta do bot
@app.route('/', methods=['POST'])
def chat():
    # extrai os dados JSON que vieram no corpo da requisição POST
    data = request.get_json()

    if not data or 'message' not in data:
        return jsonify({'error': 'Mensagem não encontrada'}), 400

    # Armazenamos a mensagem do usuário.
    user_message = data['message']
    """Chamamos a função get_bot_response() (importada do responses.py) 
    e passamos essa mensagem como argumento."""
    bot_reply = get_bot_response(user_message)
    # Retorna um JSON com a resposta do bot
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
