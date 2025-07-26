from sortedcontainers import SortedDict
from collections import deque

class OrderBook:
    def __init__(self):
        self.buy = SortedDict(lambda x: -x)  # Descending
        self.sell = SortedDict()             # Ascending
        self.order_map = {}  # order_id -> order (for cancellation)

    def add_order(self, order):  # Takes one argument from the order class
        book = self.buy if order.side == 'buy' else self.sell
        level = book.setdefault(order.price, deque())  
        '''
        Order price is used as a key of the book by the setdefault method.
        If the key exists, it returns the value (which is a deque of orders) associated with that order.price key.
        If the key doesn't exist, it inserts into the book the order.price as a new key.
        If the key doesn't exist, it also assigns deque() to that new key.
        If the key doesn't exist, it also returns this newly created and inserted deque object.
        Like how list() creates an empty list [], deque() creates an empty double-ended queue deque([]).
        level then is assigned to be equal to deque([]), which may or may not be empty.
        '''
        level.append(order)  # We append our new order to the level
        self.order_map[order.id] = order  
        # Initialised above as an empty dictionary. order.id is therefore the key, and order the value.

    def cancel_order(self, order_id):
        order = self.order_map.get(order_id) 
        if not order or order.status in ['filled', 'cancelled']:
            return False

        book = self.buy if order.side == 'buy' else self.sell
        level = book[order.price]  # Retrieves the specific deque where the order is located
        level.remove(order)  # Level removed from its deque within the order book
        
        if not level:  
            del book[order.price] 
        '''
        If level is now empty, there are no more orders at that price point.
        In which case, we have to delete the entire price level from the SortedDict.
        '''

        order.status = 'cancelled'  # Updates the order object
        del self.order_map[order_id]  # Removes the corresponding order object from the order map
        return True  

    def get_best_bid_ask(self):
        best_bid = (self.buy.peekitem(0) if self.buy else (None, None))
        best_ask = (self.sell.peekitem(0) if self.sell else (None, None))
        # .peekitem() returns a key-value pair at a specific index without removing it from the dictionary
        return best_bid, best_ask

    def get_depth(self, levels=5):


        def summarise(book, reverse=False):  
        '''
        Nested helper function for get_depth.
        Its job is to iterate through a given SortedDict and aggregate quantity at each price level.
        
        '''
            summary = []
            items = reversed(book.items()) if reverse else book.items()
            '''
            Conditional incase we want to not reverse the order (from summarise, default is reverse).
            book.items() returns from a SortedDict a key value pair (price, deque).

            '''
            for price, orders in list(items)[:levels]:  
            '''
            Recalling that the .items() method returns key value pairs.
            Levels attribute defined in the get_depth function.
            Slicing the list taking the first levels (e.g. 5) price levels.
            '''
                total_qty = sum(o.remaining() for o in orders)
                '''
                For all the orders at a given price, we call the remaining() method from orders.py
                '''
                summary.append((price, total_qty))
            return summary

        return {
            'bids': summarise(self.buy, reverse=True),
            'asks': summarise(self.sell)
        }



