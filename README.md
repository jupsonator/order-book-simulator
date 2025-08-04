\# Order Book Simulator



A lightweight, fully-functional limit order book simulator for cryptocurrency markets, written in Python.



\## Features



\- Supports both \*\*limit\*\* and \*\*market\*\* orders

\- Handles \*\*order matching\*\*, \*\*partial fills\*\*, and \*\*order cancellations\*\*

\- Maintains live \*\*order book state\*\* with best bid/ask and market depth

\- Visualises:

&nbsp; - Order book depth (bids vs asks)

&nbsp; - Trade history over time

\- Fully \*\*unit-tested\*\* using Python’s `unittest`

\- Designed with modular structure and extensibility in mind



\## Project Structure



order\_book\_simulator/

├── main.py # Entry point to run the simulator

├── order.py # Defines the Order class

├── order\_book.py # Implements the OrderBook logic

├── exchange.py # Wraps OrderBook into an exchange interface

├── visualise.py # Contains matplotlib-based plotting functions

└── tests/

&nbsp;          └── test\_order\_book.py # Unit tests for OrderBook functionality



\## Getting Started



\### 1. Install Dependencies



```bash

pip install matplotlib sortedcontainers



\### 2. Run the Simulation



'''bash

python main.py



This will:

\- Submit a few orders (limit and market)

\- Print trade results

\- Show the state of the order book

\- Optionally, visualise trades and book depth



To see the visual charts, call:

'''bash

from visualise import plot\_order\_book\_depth, plot\_trade\_history



plot\_order\_book\_depth(exchange.book)

plot\_trade\_history(exchange.book.get\_trades())



\### 3. Testing



Run the full suite of unit tests with:



python test\_order\_book.py



These tests cover:

\- Limit order addition

\- Market order matching

\- Partial fills

\- Cancellations

\- Order book state integrity



\## Visualisation



Plots are generated using matplotlib, and include:

A bar chart showing order book depth (bids vs asks)

A line plot of executed trade prices over time, with trade quantities annotated



\## Notes



All prices are assumed to be in USD

Time is recorded in UTC using datetime.utcnow()

Market orders execute against the best available price and do not rest on the book

Limit orders will rest if not fully filled



\## Future Ideas



Add support for stop-loss or iceberg orders

Stream live data using WebSockets or a mock feed

Build a front-end using Streamlit or Dash



\## Licence



This project is released under the MIT Licence.













