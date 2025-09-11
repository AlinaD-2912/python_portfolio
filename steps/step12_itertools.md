# Étape 12 : Itertools - Optimiser vos stratégies d'investissement

## 📊 Developer Story
Votre générateur produit maintenant l'évolution temporelle de votre portfolio. Vous voulez ajouter une fonctionnalité d'optimisation : tester automatiquement différentes dates d'achat/vente pour vos actions (AAPL, GOOGL, etc.) afin de découvrir quelles auraient été les meilleures stratégies pour maximiser votre portefeuille.

## 🎯 Concept : Itertools pour l'analyse combinatoire financière
Avec itertools, vous pouvez tester toutes les combinaisons possibles de dates d'achat/vente pour chacune de vos 7 actions. Par exemple, pour AAPL : tester tous les couples (date_achat, date_vente) pour trouver la stratégie optimale.

## 🎯 Objectif
**Trouvez automatiquement les meilleures stratégies d'achat/vente pour chacune de vos 7 actions.**

## 📝 Exercice
Créez `portfolio_strategies.py` qui optimise vos investissements :

### Fonction requise :
1. **`analyser_strategies_portfolio(portfolio, dates_analyse)`** - utilise `itertools.combinations()` pour tester toutes les stratégies possibles


## ✅ Solution attendue
- **50-80 lignes** utilisant itertools.combinations()
- Analyse des 7 actions de votre portfolio
- Découverte des stratégies optimales pour maximiser votre portfolio
