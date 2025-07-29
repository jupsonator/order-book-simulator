from exchange import Exchange

def main():
    exchange = Exchange()

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

if __name__ == "__main__":
    main()
