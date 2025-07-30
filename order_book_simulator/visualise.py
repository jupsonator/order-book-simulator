import matplotlib.pyplot as plt
from order_book import OrderBook
from order import Order

def plot_order_book_depth(book):
    bids = book.buy
    asks = book.sell

    bid_prices = sorted(bids.keys(), reverse=True)
    ask_prices = sorted(asks.keys())

    bid_qtys = [sum(order.quantity - order.filled_qty for order in bids[p]) for p in bid_prices]
    ask_qtys = [sum(order.quantity - order.filled_qty for order in asks[p]) for p in ask_prices]

    plt.figure(figsize=(10, 5)) # Creates a figure to be drawn on
    plt.bar(bid_prices, bid_qtys, color='green', label='Bids') # Creates a bar chart
    plt.bar(ask_prices, ask_qtys, color='red', label='Asks') # Creates a bar chart
    plt.xlabel('Price')
    plt.ylabel('Quantity')
    plt.title('Order Book Depth')
    plt.legend() # Explains which colours are used for what
    plt.grid(True) # Adds a grid so it is easier to read
    plt.tight_layout() # Prevents labels overlapping
    plt.show() # Displays the figure


def plot_trade_history(trades):
    if not trades:
        print("No trades to plot.")
        return

    prices = [t['price'] for t in trades] # From the trade dictionary in order_book.py
    qtys = [t['quantity'] for t in trades]
    times = [t['timestamp'] for t in trades]

    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker='o', linestyle='-', color='blue', label='Trade Price')
    '''
    Creates a line graph
    o provides circular markers at each point
    linestyle - provides a solid line
    label = 'Trade Price' is the label for the legend
    '''
    for i, qty in enumerate(qtys):
        plt.annotate(f"{qty}", (times[i], prices[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Trade Execution History')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    # Visualise test from here
    book = OrderBook()
    book.add_order(Order("BTC/USD", "buy", "limit", 10000, 2))
    book.add_order(Order("BTC/USD", "buy", "limit", 9900, 1))
    book.add_order(Order("BTC/USD", "sell", "limit", 10100, 1))
    book.add_order(Order("BTC/USD", "sell", "limit", 10200, 3))

    
    plot_order_book_depth(book)

    market_order = Order("BTC/USD", "buy", "market", None, 2)
    book.match_order(market_order)

    plot_trade_history(book.trades)