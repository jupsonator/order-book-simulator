import uuid
from datetime import datetime

class Order:
    def __init__(self, symbol, side, type_, price, quantity):
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.utcnow()
        self.symbol = symbol  # which stock e.g. AAPL
        self.side = side  # which of 'buy' or 'sell'
        self.type = type_  # which of 'market' or 'limit'
        self.price = price
        self.quantity = quantity  # how much is intended to be traded
        self.filled_qty = 0  # tracking how much of the order has been executed
        self.status = 'open'  # indicates if the order is active, awaiting execution, or been cancelled

    def remaining(self):
        return self.quantity - self.filled_qty

    def is_filled(self):
        return self.remaining() == 0

