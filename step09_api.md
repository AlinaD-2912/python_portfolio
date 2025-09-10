# Étape 9 : Récupération de Données API - Obtenir les vrais prix de votre Portfolio

## 📊 Developer Story
Votre Portfolio est maintenant validé et sécurisé. Jusqu'à présent, vous avez utilisé des prix actuels simulés pour vos 7 actions. Il est temps de récupérer les VRAIS prix actuels d'AAPL, GOOGL, MSFT, TSLA, NVDA, AMZN, META depuis une API financière pour connaître la vraie valeur de votre portefeuille.

## 🎯 Concept : APIs appliquées à votre Portfolio réel
Au lieu de prix inventés, vous allez récupérer les cours de bourse actuels via une API. Vous découvrirez vos vrais gains/pertes actuels.

## 🎯 Objectif
**Récupérez les vrais prix actuels de toutes vos actions pour calculer votre performance réelle.**

## 📝 Exercice
Créez `portfolio_api.py` qui connecte votre Portfolio au monde réel :

### Fonctions requises :
1. **`obtenir_prix_action(symbole)`** - récupère le prix actuel d'une action via API
2. **`obtenir_prix_portfolio(portfolio)`** - récupère les prix de toutes vos positions
3. **`calculer_performance_reelle(portfolio)`** - vos vrais gains/pertes actuels

## ✅ Solution attendue
- **50-80 lignes** avec gestion d'erreurs robuste
- Récupération des prix de vos 7 actions réelles
- Calcul des pertes / rendements du portfolio avec les vrais prix

## 🔍 APIs recommandées
- **Alpha Vantage** (gratuite, 5 appels/min)
- **yfinance** (module Python, simple)


