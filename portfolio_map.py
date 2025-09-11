from portfolio_calculs import *
from portfolio_structures import Portfolio, convertir_vers_positions
from portfolio_loader import lire_portfolio_csv
from portfolio_loader import *;

print("\n\n ======================================  Step 4 ==========================================")

portfolio_data = lire_portfolio_csv("portfolio_sample.csv")
prix_actuels_data = lire_portfolio_csv("portfolio_actual_prices_sample.csv")

portfolio_positions = convertir_vers_positions(portfolio_data)
prix_actuels_positions = convertir_vers_positions(prix_actuels_data)

mon_portfolio = Portfolio("My Investment Portfolio")
for pos in portfolio_positions:
    mon_portfolio.add_position(pos)

afficher_positions(mon_portfolio.positions)


def calculer_valeurs_positions(positions):
    return list(map(lambda_valeur_position, positions))

valeurs_position = calculer_valeurs_positions(mon_portfolio.get_positions())
print("\nValeurs d'achat :", valeurs_position)

def calculer_gains_portfolio(positions, prix_actuels):
    return list(map(lambda_gain_absolu, positions, prix_actuels))

gain_portfolio = calculer_gains_portfolio(mon_portfolio.get_positions(), prix_actuels_positions)
print("Gains actuels :", gain_portfolio)


def calculer_rendements_portfolio(positions, prix_actuels_dict):
     return list(map(lambda_rendement_pourcent, positions, prix_actuels_dict))

rendements_portfolio = calculer_rendements_portfolio(mon_portfolio.get_positions(), prix_actuels_positions)
print("Rendements :", rendements_portfolio)


