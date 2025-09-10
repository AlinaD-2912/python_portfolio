from portfolio_structures import *;
from typing import List
from collections import namedtuple

print("\n\n ======================================  Step 5 ==========================================")

positions_problematiques = [
    Position('AAPL', 10, 0.0, '2023-01-15'),      # Prix d'achat = 0 !
    Position('INVALID', 5, 100.0, '2023-02-01'),  # Symbole inexistant
    Position('GOOGL', -10, 2500.0, '2023-03-01')  # Quantité négative !
]

def ErreurDonneesPortfolio (portfolio: Portfolio, position: Position):
    try:
        if position.purchase_price <= 0 :
            raise ErreurDonneesPortfolio("Prix d'achat invalide pour {position.symbol} : {position.purchase_price}")
        if position.quantity <=0 :
            raise  ErreurDonneesPortfolio("Quantité invalide pour {position.symbol} : {position.quantity}")
        if not position.symbol.isAlpha():
            raise ErreurDonneesPortfolio("Symbol invalide : {position.symbol} ")
        portfolio.add_position(position)
    except ErreurDonneesPortfolio as e:
        print("Erreur détecté: {e}")
    except Exception as e:
        print(f"Erreur imprévue est survenue: {e}")

portfolio = Portfolio("Test")

for pos in positions_problematiques:
    portfolio.add_position(pos)

print(portfolio.get_positions())



