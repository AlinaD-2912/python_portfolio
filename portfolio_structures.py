import csv
import decimal
import json
from collections import namedtuple
from typing import NamedTuple, Optional

def lire_portfolio_csv(nom_fichier):
    portfolio = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.DictReader(csvfile, delimiter=',')  # adjust delimiter if needed
        for line in lecteur_csv:
            position = {
                'symbol': line.get('symbol'),
                'quantity': int(line.get('quantity', 0)),
                'purchase_price': float(line.get('purchase_price', 0.0)),
                'purchase_date': line.get('purchase_date')
            }
            portfolio.append(position)
    return portfolio

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
    # **d is dictionary unpacking → it passes each key/value in the dict as keyword arguments
    return [Position(**d) for d in portfolio_dict]

portfolio_dicts = lire_portfolio_csv("portfolio_sample.csv")
positions = convertir_vers_positions(portfolio_dicts)


def afficher_positions(positions) :
    for pos in positions:
        # f - formatted string
        print(f"{pos.symbol} - {pos.quantity} at {pos.purchase_price} on {pos.purchase_date}")

positions = [
    Position("AAPL", 10, 150.0, "2023-01-15"),
    Position("GOOGL", 5, 2500.0, "2023-02-01"),
    Position("MSFT", 20, 300.0, "2023-01-20")

]
afficher_positions(positions)

