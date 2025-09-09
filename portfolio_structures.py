import csv
import json
from collections import namedtuple


def lire_portfolio_csv(nom_fichier):
    portfolio = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')  # or delimiter=';' depending on your file
        for row in reader:
            portfolio.append(row)
    return portfolio

# namedtuple : can access elements by index, lightweight objects with named fields
Position = namedtuple("Position", ["symbol", "quantity", "price", "type"])
Transaction = namedtuple( "Transaction", 'date', 'symbol', 'quantity', 'price', 'type' )
Portfolio = namedtuple("Portfolio", 'symbol', 'quantity', 'price', 'date', 'type')


def convertir_vers_positions(portfolio_dict) :
    for pos in map(Position._make, csv.reader(open(portfolio_dict["portfolio_sample.csv"]), delimiter=',')) :
        print(pos.symbol, pos.quantity, pos.price, pos.type)


def afficher_positions(positions) :
    for position in positions :
        print(position)