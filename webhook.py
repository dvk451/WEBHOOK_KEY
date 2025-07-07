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

emaHTF = request.security(syminfo.tickerid, "60", ta.ema(close, 50))
trendConfirm = close > emaHTF  // Use only if price is above HTF trend

buySignal := buySignal and trendConfirm
reversalBuy = ta.crossover(close, lowerBB) and rsi < 40
reversalSell = ta.crossunder(close, upperBB) and rsi > 60

if reversalBuy
    strategy.entry("Reversal Buy", strategy.long)
    strategy.exit("TP/SL Reversal", from_entry="Reversal Buy", profit=takeProfitPerc * 0.01, loss=stopLossPerc * 0.01)

if reversalSell
    strategy.entry("Reversal Sell", strategy.short)
    strategy.exit("TP/SL Reversal", from_entry="Reversal Sell", profit=takeProfitPerc * 0.01, loss=stopLossPerc * 0.01)

alertcondition(reversalBuy, title="Reversal Buy Alert", message="Reversal Buy Triggered!")
alertcondition(reversalSell, title="Reversal Sell Alert", message="Reversal Sell Triggered!")
