import unittest
from order_book_simulator.order import Order
from order_book_simulator.order_book import OrderBook

class TestOrderBook(unittest.TestCase):  
    '''
    unittest can't be interchanged with another word and likewise for the .TestCase method
    unittest refers to Python's built-in unit testing system
    TestCase is a class in the unittest module. It contains a collection of test methods
    '''
    def setUp(self):
        self.book = OrderBook()

    def test_limit_order_addition(self):
        order = Order("BTC/USD", "buy", "limit", 10000, 1)
        self.book.add_order(order)
        bids, asks = self.book.get_best_bid_ask()
        self.assertEqual(bids[0], 10000)  
        '''
        .assertEqual(,) is an assertion method provided by unittest.TestCase which checks if two items are equal
        If the two items are not equal, the test fails
        '''
        self.assertEqual(asks, (None, None))

    def test_market_order_matching(self):
        sell = Order("BTC/USD", "sell", "limit", 10100, 1)
        self.book.add_order(sell)
        market_buy = Order("BTC/USD", "buy", "market", None, 1)
        trades = self.book.match_order(market_buy)
        self.assertEqual(len(trades), 1)
        self.assertEqual(trades[0]['price'], 10100)

    def test_partial_fill(self):
        sell = Order("BTC/USD", "sell", "limit", 10100, 1)
        self.book.add_order(sell)
        buy = Order("BTC/USD", "buy", "market", None, 2)
        trades = self.book.match_order(buy)
        self.assertEqual(len(trades), 1)
        self.assertEqual(buy.remaining(), 1)
        self.assertEqual(buy.status, 'partially_filled')

    def test_order_cancellation(self):
        order = Order("BTC/USD", "buy", "limit", 10000, 1)
        self.book.add_order(order)
        cancelled = self.book.cancel_order(order.id)
        self.assertTrue(cancelled)
        depth = self.book.get_depth()
        self.assertEqual(depth['bids'], [])

    def test_book_integrity_after_match(self):
        sell1 = Order("BTC/USD", "sell", "limit", 10100, 1)
        sell2 = Order("BTC/USD", "sell", "limit", 10200, 1)
        self.book.add_order(sell1)
        self.book.add_order(sell2)

        buy = Order("BTC/USD", "buy", "market", None, 1)
        self.book.match_order(buy)

        best_ask = self.book.get_best_bid_ask()[1]
        self.assertEqual(best_ask[0], 10200)  # Only sell2 remains

if __name__ == '__main__':
    unittest.main()
