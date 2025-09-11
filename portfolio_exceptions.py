from datetime import datetime

from portfolio_structures import *;
from typing import List
from collections import namedtuple

print("\n\n ======================================  Step 5 ==========================================")

positions_problematiques = [
    Position('AAPL', 10, 0.0, '2023-01-15'),      # Prix d'achat = 0 !
    Position('INVALID', 5, 100.0, '2023-02-01'),  # Symbole inexistant
    Position('GOOGL', -10, 2500.0, '2023-03-01'), # Quantité négative !
    Position('AMZN', 0.10, 2500.0, '2023-03-01'), # Quantité != type int
    Position(25, -10, 2500.0, '2023-03-01'),      # Symbole numérique
    Position('TSLA', -10, 2500.0, '2027-03-01'),   # Date future
    Position('MSFT', 10, -2500.0, '2027-03-01'),  # Prix negative
    Position('META', 10, 2500.0, '20270301')   # Date invalid format
]

class ErreurDonneesPortfolio(Exception):
    pass

def test_portfolio (portfolio: Portfolio, position: Position):
    valid_symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA', 'AMZN', 'META']
    try:
        # first test symbols
        if not isinstance(position.symbol, str):
            raise ErreurDonneesPortfolio(f"Le symbole doit être de type String : {position.symbol} ")
        if not position.symbol.isalpha():
            raise ErreurDonneesPortfolio(f"Symbol invalide : {position.symbol} ")
        if position.symbol not in valid_symbols:
            raise ErreurDonneesPortfolio(f"Symbole inconnu: {position.symbol}")
        # second quantity
        if not isinstance(position.quantity, int):
            raise ErreurDonneesPortfolio(f"La quantité doit être de type int {position.symbol} : {position.quantity} ")
        if position.quantity <=0 :
            raise  ErreurDonneesPortfolio(f"Quantité invalide pour {position.symbol} : {position.quantity}")
        # third price
        if not isinstance(position.purchase_price, float):
            raise ErreurDonneesPortfolio(f"Le prix doit être de type float : {position.symbol} ")
        if position.purchase_price <= 0 :
            raise ErreurDonneesPortfolio(f"Prix d'achat invalide pour {position.symbol} : {position.purchase_price}")
        # forth date
        try:
            purchase_date = datetime.strptime(position.purchase_date, "%Y-%m-%d").date()
        except ValueError:
            raise ErreurDonneesPortfolio(f"Format de date invalide: {position.purchase_date}")
        if purchase_date > datetime.today().date():
            raise ErreurDonneesPortfolio(f"La date d'achat ne peut pas être postérieure à la date d'aujourd'hui {position.symbol}  date : {position.purchase_date}")
        portfolio.add_position(position)

    except ErreurDonneesPortfolio as e:
        print(f"Erreur détecté: {e}")
    except Exception as e:
        print(f"Erreur imprévue est survenue: {e}")

portfolio = Portfolio("Test")

for pos in positions_problematiques:
    test_portfolio(portfolio, pos)

print(portfolio.get_positions())


print("\nPositions valides dans le portfolio:")
print(portfolio.get_positions())



def charger_portfolio_securise(fichier) -> Portfolio:
    safe_portfolio = Portfolio("SECURE_PORTFOLIO")
    try:
        with open(fichier, newline='', encoding='utf-8') as csvfile:
            lecteur_csv = csv.DictReader(csvfile, delimiter=',')
            for line in lecteur_csv:
                try:
                    position = Position(
                        symbol=line.get('symbol', ''),
                        quantity=int(line.get('quantity', 0)),
                        purchase_price=float(line.get('purchase_price', 0.0)),
                        purchase_date=line.get('purchase_date', '')
                    )
                    test_portfolio(safe_portfolio, position)
                except ErreurDonneesPortfolio as e:
                    print(f"Erreur détectée dans le fichier: {e}")
    except FileNotFoundError :
        print(f"Fichier non existent : {fichier}")
    except Exception as e:
        print(f"Erreur imprévue")
    return safe_portfolio

print("Result chargement_portfolio_securise")
p = charger_portfolio_securise("portfolio_sample.csv")
print("\nPositions valides dans le fichier:")
print(p.get_positions())


