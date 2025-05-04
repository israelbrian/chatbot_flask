# função para gerar respostas do bot
def get_bot_response(user_message):
    # evitando problemas de case-sensitivity
    message = user_message.lower()

    # Respostas do bot baseadas em palavras-chave 
    if "oi" in message or "oie" in message or "ola" in message or "olá" in message:
        return "Fala, fã da FURIA! Sobre o que você quer saber?"
    elif "jogo" in message or "partida" in message:
        return "Nosso próximo jogo é dia 10 de maio! Prepara o coração! #GOFURIA!"
    elif "cs" in message or "counter" in message or "strike" in message:
        return "CS2 é nossa paixão! Quer saber a line-up atual?"
    elif "line" in message or "elenco" in message or "time" in message or "sim" in message or "jogadores" in message:
        return "Atualmente nossa line-up titular do time de Counter Strike 2 é composta por: Fallen, KSCERATO, yuurih, MOLODOY, YEKINDAR."
    elif "fut" in message or "soccer" in message:
        return "Sim, a FURIA também está no futebol!"
    elif "modalidade" in message or "e-sports" in message or "competi" in message:
        return "Atualmente nós competimos em vários jogos de e-sports, incluindo Counter-Strike 2, Rocket League, League of Legends, Valorant, Rainbow Six: Siege, Apex Legends e Kings League";
    elif "skin" in message:
        return "As skins da FURIA são incríveis! Você já viu a nossa coleção? Confira em: https://www.furia.gg/loja"
    elif "nao" in message or "não" in message or "no" in message:
        return "Entendi! Se precisar de algo, é só chamar!"
    elif "org" in message or "historia" in message or "trabalho" in message or "furia" in message:
        return "A FURIA foi eleita a melhor organização de eSports do Brasil por dois anos consecutivos (2020 e 2021) pelo Prêmio eSports Brasil. Além disso, a organização foi reconhecida como a quarta maior do mundo em 2022 por um levantamento do portal norte-americano Nerd Street. Em 2023, foi eleita a melhor organização de CS:GO do ano pelo Júri da Brasil Storm CS."
    else:
        return "Hmm... não entendi. Tente perguntar sobre os jogos ou o time! #GOFURIA";