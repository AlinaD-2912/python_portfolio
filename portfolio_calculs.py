from portfolio_loader import lire_portfolio_csv

portfolio = lire_portfolio_csv("portfolio_sample.csv")
actual_prices = lire_portfolio_csv("portfolio_actual_prices_sample.csv")

def valeur_position(position) :
    return (lambda pos: pos["quantity"] * pos["purchase_price"])(position)

position = {
    "symbol": "AAPL",
    "quantity": 10,
    "purchase_price": 150.0,
    "purchase_date": "2023-01-15"
}

result = valeur_position(position)
print("\nValue of the position :" , result)

def gain_absolu (actual_prices) :
    price_search = {p["symbol"]: p["purchase_price"] for p in actual_prices}

    return lambda pos: (price_search[pos["symbol"]] - pos["purchase_price"]) * pos["quantity"]


calcul_gain_absolu = gain_absolu(actual_prices)
print("\nGain of the position :" )
for pos in portfolio:
    g = calcul_gain_absolu(pos)
    if g >0:
        print(f"{pos["symbol"]} : + {g} €")
    else :
        print(f"{pos["symbol"]} : = {g} €")


def rendement_pourcent(actual_prices) :
    price_search = {p["symbol"]: p["purchase_price"] for p in actual_prices}
    return lambda pos: ( (price_search[pos["symbol"]] - pos["purchase_price"]) / pos["purchase_price"] ) * 100 if pos["purchase_price"] > 0 else 0

calcul_gain_pourcent = rendement_pourcent(actual_prices)
print("\nGain of the position in %:" )
for pos in portfolio:
    g = calcul_gain_pourcent(pos)
    if g > 0 :
        print(f"{pos["symbol"]} : + {g} %")
    else :
        print(f"{pos["symbol"]} : {g} %")

def poids_portfolio(position, actual_prices) :
    price_search = {p["symbol"]: p["purchase_price"] for p in actual_prices}
    return (lambda pos: ((price_search[pos["symbol"]] - pos["purchase_price"]) / pos["purchase_price"]) * 100)(position)

result2 = poids_portfolio(position, actual_prices)
print("\nValue of the position in % :" , result2)

