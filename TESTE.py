from telegram import Bot

TELEGRAM_TOKEN = "7676787815:AAHLOCqbmuQgJN8NDgxvsgnyoH_nMhWCbyM"
CHAT_ID = "1722310941"  # Chat ID obtido do getUpdates

def enviar_alerta(mensagem):
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=mensagem)
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Teste o envio
enviar_alerta("Teste de alerta do bot!")
