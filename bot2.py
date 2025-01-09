from binance.client import Client
from telegram import Bot
import pandas as pd
import time

# Configurações da API da Binance
API_KEY = "WGppsqHCM893qJD9IeAx20SzEw5Ewdb1IzUBzS0r9gHZRiAP8LPbtK3l1RWqwQKZ"
API_SECRET = "QrPiz5LYJS20oRJZb3JX7W5Ts7Bd7WrZ36PlG389JaHrfxHv0Th0Jd0uTZd345cB"

# Token do bot do Telegram e chat_id
TELEGRAM_TOKEN = "7433321732:AAEFuPHV7nTsMEsCnglkYWGbCvJNoxiKe1g"
CHAT_ID = "SEU_CHAT_ID_AQUI"  # Substitua pelo seu chat_id

client = Client(API_KEY, API_SECRET)

# Função para enviar alertas via Telegram
def enviar_alerta(mensagem):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=mensagem)

# Teste de notificação
def teste_notificacao():
    mensagem = "Teste de notificação do bot: Sistema funcionando!"
    enviar_alerta(mensagem)
    print(f"Mensagem enviada: {mensagem}")

# Função para calcular o RSI
def calculate_rsi(data, period=14):
    close_prices = pd.Series([float(kline[4]) for kline in data])  # Preços de fechamento
    delta = close_prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(0).tolist()  # Retorna o RSI como lista

# Função para buscar dados de mercado
def get_market_data(symbol, interval, limit=100):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    return klines

# Função principal do bot
def run_bot():
    # Enviar notificação de teste assim que o bot iniciar
    teste_notificacao()

    while True:
        try:
            # Aqui você pode colocar o código para monitorar o mercado
            print("Monitorando o mercado...")
            time.sleep(60)  # Aguarda 1 minuto
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(60)  # Aguarda 1 minuto antes de tentar novamente

if __name__ == "__main__":
    run_bot()
