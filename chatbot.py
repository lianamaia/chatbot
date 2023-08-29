import random
import datetime

responses = {
    "oi": ["Olá!", "Oi!", "Oi, como posso ajudar?"],
    "como você está": ["Estou bem, obrigado!", "Estou aqui para ajudar!", "Estou ótimo!"],
    "adeus": ["Até logo!", "Tchau!", "Até mais!"],
    "ajuda": ["Posso ajudar você? É só perguntar!", "Claro, estou aqui para ajudar!", "Estou pronta para responder suas perguntas!"],
    "qual seu nome": ["Meu nome é ChatBot!", "Eu sou o ChatBot, um assistente virtual.", "Sou o ChatBot, estou aqui para ajudar!"],
    "que horas são": ["A hora atual é: "],
}

def chatbot_response(message):
    message = message.lower()  # Converter para minúsculas para comparação

    if message in responses:
        if message == "que horas são":
            current_time = datetime.datetime.now().strftime("%H:%M")
            return responses[message][0] + current_time
        else:
            return random.choice(responses[message])
    else:
        return "Desculpe, não entendi o que você disse."

print("Olá! Eu sou um chatbot simples. Digite 'adeus' para sair.")

while True:
    user_input = input("Você: ")
    
    if user_input.lower() == "adeus":
        print("Chatbot: Até logo!")
        break
    
    response = chatbot_response(user_input)
    print("Chatbot:", response)
