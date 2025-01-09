from telegram import Bot

# Substitua pelo token do BotFather
TELEGRAM_TOKEN = "7676787815:AAHLOCqbmuQgJN8NDgxvsgnyoH_nMhWCbyM"
CHAT_ID = "1722310941"  # Chat ID obtido do getUpdates

def enviar_alerta(mensagem):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=mensagem)

# Teste o envio
enviar_alerta("Teste de alerta do bot!")
