from order import Order
from order_book import OrderBook

def main():
    order1 = Order("BTC/USD", "buy", "limit", 10000, 2)
    order2 = Order("BTC/USD", "sell", "limit", 10100, 1)
    order3 = Order("BTC/USD", "buy", "market", None, 2)

    book = OrderBook()
    book.add_order(order1)
    book.add_order(order2)

    print("Best Bid/Ask:", book.get_best_bid_ask())
    print("Order Book Depth:", book.get_depth())

    trades = book.match_order(order3)

    if trades:
        print("\nTrades Executed:")
        for trade in trades:
            print(trade)

if __name__ == "__main__":
    main()
