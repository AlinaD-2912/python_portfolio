import csv
import decimal
import json
from collections import namedtuple
from typing import NamedTuple, Optional

from portfolio_loader import lire_portfolio_json, lire_portfolio_csv

# namedtuple : can access elements by index, lightweight objects with named fields
Position = namedtuple("Position", ["symbol", "quantity", "purchase_price", "purchase_date"])
Transaction = namedtuple("Transaction", ["date", "symbol", "quantity", "price", "type"])


class Portfolio(NamedTuple):
    symbol: str
    quantity: int
    price: decimal.Decimal
    date: str
    type: Optional[str] = None


def convertir_vers_positions(portfolio_dict) :
    # **d is dictionary unpacking  it passes each key/value in the dict as keyword arguments
    return [Position(**d) for d in portfolio_dict]

portfolio_dicts = lire_portfolio_csv("portfolio_sample.csv")
portfolio_dicts2 = lire_portfolio_json("portfolio_sample.json")

positions_csv = convertir_vers_positions(portfolio_dicts)
positions_json = convertir_vers_positions(portfolio_dicts2)


def afficher_positions(positions) :
    for pos in positions:
        # f - formatted string
        print(f"{pos.symbol} - {pos.quantity} at {pos.purchase_price} on {pos.purchase_date}")

positions = [
    Position("AAPL", 10, 150.0, "2023-01-15"),
    Position("GOOGL", 5, 2500.0, "2023-02-01"),
    Position("MSFT", 20, 300.0, "2023-01-20")

]
positions2 = [
    Position("AAPL", 10, 150.0, "2023-01-15"),
    Position("GOOGL", 5, 2500.0, "2023-02-01"),
    Position("MSFT", 20, 300.0, "2023-01-20")

]


print("\n==========  CSV Portfolio: ===========")
afficher_positions(positions_csv)

print("\n========== JSON Portfolio: ============")
afficher_positions(positions_json)