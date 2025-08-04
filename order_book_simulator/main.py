from exchange import Exchange
from visualise import plot_order_book_depth, plot_trade_history
import random
from datetime import datetime, timedelta
import time

def main():
    exchange = Exchange()


    sides = ["buy", "sell"]
    types = ["limit", "market"]

    for _ in range(50):
        symbol = "BTC/USD"
        side = random.choice(sides)
        order_type = random.choices(types, weights=[0.8, 0.2])[0]  # mostly limit orders

        if order_type == "limit":
            price = random.randint(9900, 10100)
        else:
            price = None  # market order

        quantity = round(random.uniform(0.1, 1.5), 2)

        exchange.submit_order(symbol, side, order_type, price, quantity)
        time.sleep(0.01)




    print("\n--- SUBMIT LIMIT SELL (10100 x 1 BTC) ---")
    order1, _ = exchange.submit_order("BTC/USD", "sell", "limit", 10100, 1)

    print("\n--- SUBMIT LIMIT BUY (10000 x 2 BTC) ---")
    order2, _ = exchange.submit_order("BTC/USD", "buy", "limit", 10000, 2)

    print("\n--- SUBMIT MARKET BUY (2 BTC) ---")
    order3, trades = exchange.submit_order("BTC/USD", "buy", "market", None, 2)

    print("\nTrades Executed:")
    for trade in trades:
        print(trade)

    print("\nFinal Order Statuses:")
    print(order1)
    print(order2)
    print(order3)

    print("\n--- Current Order Book ---")
    exchange.print_book()

    print("\n--- All Trades ---")
    exchange.print_trades()

    plot_order_book_depth(exchange.book)
    plot_trade_history(exchange.book.get_trades())

if __name__ == "__main__":
    main()
