from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7980845539:AAECIVEOli6GAKDUlAYXHYdp3dhRtZFvALY'
CHAT_ID = '477994153'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', '📡 Сигнал з TradingView отримано')
    text = f"📈 Сигнал з TradingView:\n\n{message}"
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    requests.post(url, json={'chat_id': CHAT_ID, 'text': text})
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
