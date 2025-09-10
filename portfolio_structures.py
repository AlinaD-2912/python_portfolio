import csv
import decimal
import json
from collections import namedtuple
from typing import NamedTuple, Optional, List, Any

from portfolio_loader import lire_portfolio_json, lire_portfolio_csv

print("\n\n ======================================  Step 2 ==========================================")

# namedtuple : can access elements by index, lightweight objects with named fields
Position = namedtuple("Position", ["symbol", "quantity", "purchase_price", "purchase_date"])
Transaction = namedtuple("Transaction", ["date", "symbol", "quantity", "price", "type"])


class Portfolio:
    def __init__(self, name: str):
        self.name = name
        self.positions: List[Position] = []

    def add_position(self, position: Position):
        self.positions.append(position)

    def get_positions(self) -> List[Position]:
        return self.positions


def convertir_vers_positions(portfolio_data: Any) -> List[Position]:
    positions = []
    # If it's a dict with 'positions' key, extract the positions data
    if isinstance(portfolio_data, dict) and 'positions' in portfolio_data:
        data_positions = portfolio_data['positions']
    else:
        # Otherwise assume it's already the positions data
        data_positions = portfolio_data

    # Convert each position data to Position namedtuple
    for pos_data in data_positions:
        position = Position(
            symbol=pos_data['symbol'],
            quantity=int(pos_data['quantity']),
            purchase_price=float(pos_data['purchase_price']),
            purchase_date=pos_data['purchase_date']
        )
        positions.append(position)

    return positions


def afficher_positions(positions: List[Position]):
    for pos in positions:
        # f - formatted string
        print(f"{pos.symbol} - {pos.quantity} at {pos.purchase_price} on {pos.purchase_date}")


# Load data and convert to positions
portfolio_dicts = lire_portfolio_csv("portfolio_sample.csv")
portfolio_dicts2 = lire_portfolio_json("portfolio_sample.json")

positions_csv = convertir_vers_positions(portfolio_dicts)
positions_json = convertir_vers_positions(portfolio_dicts2)

# Create Portfolio instances
portfolio_csv = Portfolio("CSV Portfolio")
portfolio_json = Portfolio("JSON Portfolio")

# Add positions to portfolios
for pos in positions_csv:
    portfolio_csv.add_position(pos)

for pos in positions_json:
    portfolio_json.add_position(pos)

# Test positions (for demonstration)
test_positions = [
    Position("AAPL", 10, 150.0, "2023-01-15"),
    Position("GOOGL", 5, 2500.0, "2023-02-01"),
    Position("MSFT", 20, 300.0, "2023-01-20")
]

print("\n==========  CSV Portfolio: ===========")
afficher_positions(portfolio_csv.get_positions())

print("\n========== JSON Portfolio: ============")
afficher_positions(portfolio_json.get_positions())

print("\n========== Test Positions: ============")
afficher_positions(test_positions)