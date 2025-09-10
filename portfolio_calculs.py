from portfolio_loader import lire_portfolio_csv
from portfolio_structures import *;
from portfolio_loader import *;

portfolio_data = lire_portfolio_csv("portfolio_sample.csv")
actual_prices_data = lire_portfolio_csv("portfolio_actual_prices_sample.csv")

portfolio_positions = convertir_vers_positions(portfolio_data)
actual_prices_positions = convertir_vers_positions(actual_prices_data)

print("\n\n ======================================  Step 3 ==========================================")


lambda_valeur_position = lambda pos: pos.quantity * pos.purchase_price

positionExemple = Position("AAPL", 10, 150, "2023-01-15")
print(f"\nValue of the position {positionExemple.symbol}: {lambda_valeur_position(positionExemple)}")

positionPrixAchat = Position("AAPL", 10, 150, "2023-01-15")
positionPrixVente = Position("AAPL", 10, 175, "2023-01-15")

lambda_gain_absolu = lambda pos_achat, pos_actuel: (pos_actuel.purchase_price - pos_achat.purchase_price) * pos_achat.quantity

print(f"Absolute gain for {positionPrixAchat.symbol}: {lambda_gain_absolu(positionPrixAchat, positionPrixVente)}")

lambda_rendement_pourcent = lambda pos_achat, pos_actuel: ((pos_actuel.purchase_price - pos_achat.purchase_price) / pos_achat.purchase_price) * 100

print(f"Percentage return for {positionPrixAchat.symbol}: {lambda_rendement_pourcent(positionPrixAchat, positionPrixVente):.2f}%")



lambda_gain_absolu_portfolio = lambda pos_achat: (
    lambda_gain_absolu(pos_achat, recherche_par_symbole(actual_prices_positions, pos_achat.symbol))
    if recherche_par_symbole(actual_prices_positions, pos_achat.symbol) else 0
)

lambda_rendement_pourcent_portfolio = lambda pos_achat: (
    lambda_rendement_pourcent(pos_achat, recherche_par_symbole(actual_prices_positions, pos_achat.symbol))
    if recherche_par_symbole(actual_prices_positions, pos_achat.symbol) else 0
)

