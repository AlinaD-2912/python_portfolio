from portfolio_calculs import *
from portfolio_structures import Portfolio, convertir_vers_positions
from portfolio_loader import lire_portfolio_csv
from portfolio_loader import *;

print("\n\n ======================================  Step 4 ==========================================")

portfolio_data = lire_portfolio_csv("portfolio_sample.csv")
prix_actuels_data = lire_portfolio_csv("portfolio_actual_prices_sample.csv")

portfolio_positions = convertir_vers_positions(portfolio_data)
prix_actuels_positions = convertir_vers_positions(prix_actuels_data)

def calculer_valeurs_positions(positions):
    return list(map(lambda_valeur_position, positions))


def calculer_gains_portfolio(positions_achat, positions_actuelles):
    """Calculate absolute gains for each position"""
    gains = []
    for pos_achat in positions_achat:
        pos_actuelle = recherche_par_symbole(positions_actuelles, pos_achat.symbol)
        if pos_actuelle:
            gain = lambda_gain_absolu(pos_achat, pos_actuelle)
            gains.append(gain)
        else:
            gains.append(0)  # No current price data available
    return gains



def calculer_rendements_portfolio(positions, prix_actuels_dict):
     return list(map(lambda_rendement_pourcent, positions, prix_actuels_dict))

