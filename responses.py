def get_bot_response(user_message):
    message = user_message.lower()

    if "olá" in message or "oi" in message:
        return "Olá! Como posso ajudar você hoje?"
    elif "horário" in message:
        return "Estamos abertos de segunda a sexta, das 8h às 18h."
    elif "obrigado" in message:
        return "De nada! Se precisar de mais alguma coisa, é só chamar."
    else:
        return "Desculpe, não entendi. Pode reformular a pergunta?"