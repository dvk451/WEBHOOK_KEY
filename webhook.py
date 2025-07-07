from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# === Configuration ===
secret_key = os.environ.get("WEBHOOK_KEY")  # security key for alerts

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)

    if data.get("key") != secret_key:
        return jsonify({"status": "unauthorized"}), 403

    action = data.get("action")
    symbol = data.get("symbol")
    quantity = data.get("quantity")

    if action == "buy":
        print(f"TradingView ALERT: BUY {quantity} of {symbol}")
        return jsonify({"status": "buy signal received"})

    elif action == "sell":
        print(f"TradingView ALERT: SELL {quantity} of {symbol}")
        return jsonify({"status": "sell signal received"})

    return jsonify({"status": "unknown action"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
