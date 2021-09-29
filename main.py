import telebot

Chave_API = 'YOUR_KEY'

bot = telebot.TeleBot(Chave_API)


# se clicar na opção 1 ela retorna essa função
@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, 'Para ver o andamento da sua OS entre no site www.samsung.com')


# se clicar na opção 2 ela retorna essa função
@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Para fazer uma reclamação, mande um email para reclameaqui@reclame.com')


# se clicar na opção 3 ela retorna essa função
@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, 'Para falar com a Samsung é necessario ligar para o numero 4004-0000')





# Função para quando a pessoa mandar qualquer coisa
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Olá, escolha a opção desejada (clique no item)
    /opcao1 Ver o andamento da minha OS
    /opcao2 Fazer uma reclamação
    /opcao3 Falar com a Samsung
Responder qualquer outra coisa não irá funcionar, por gentileza clique nas opções."""
    bot.reply_to(mensagem, texto)




bot.polling()
