from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhooks/events', methods=['POST'])
def events():
    data = request.json
    # Обработка данных события
    print(f"Received event: {data}")
    return jsonify({'status': 'ok'})

@app.route('/webhooks/messages', methods=['POST'])
def messages():
    data = request.json
    # Обработка входящих сообщений
    print(f"Received message: {data}")
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=5000)
