from order_book import OrderBook
from order import Order

class Exchange:
    def __init__(self):
        self.book = OrderBook()  # We just use the .book method as a prefix to the methods in order_book.py

    def submit_order(self, symbol, side, type_, price, quantity):
        order = Order(symbol, side, type_, price, quantity)
        trades = self.book.match_order(order)
        return order, trades

    def cancel_order(self, order_id):
        return self.book.cancel_order(order_id)

    def print_book(self):
        bid, ask = self.book.get_best_bid_ask()
        depth = self.book.get_depth()
        print("Best Bid:", bid)
        print("Best Ask:", ask)
        print("Depth:", depth)

    def print_trades(self):
        for trade in self.book.get_trades():
            print(trade)