from typing import List

from portfolio_loader import *;
from collections import namedtuple
from portfolio_structures import convertir_vers_positions, Position;


class Portfolio:
    def __init__(self, positions=None):
        if positions is None:
            self.positions = []
        else:
            self.positions = positions

    def __str__(self):
        return "\n".join([f"{pos.symbol}: quantity = {pos.quantity}, price = {pos.purchase_price}, date: {pos.purchase_date}" for pos in self.positions])

    def __len__(self):
        return len(self.positions)




portfolio_data = lire_portfolio_csv("portfolio_sample.csv")
positions_csv = convertir_vers_positions(portfolio_data)

my_portfolio = Portfolio()

for pos in positions_csv:
    my_portfolio.positions.append(pos)

print("\nPortfolio :")
print(my_portfolio)
print("\nPortfolio length :")
print(len(my_portfolio))
print("\nPortfolio string:")
print(str(my_portfolio))
