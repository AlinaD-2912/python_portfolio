# Étape 10 : Le Threading - Récupérer tous vos prix en parallèle

## 📊 Developer Story
Vous pouvez maintenant récupérer les vrais prix via API, mais c'est LENT ! Pour vos 7 actions (AAPL, GOOGL, MSFT, TSLA, NVDA, AMZN, META), vous devez attendre 7 appels API séquentiels (7 secondes). Vous voulez récupérer tous vos prix en parallèle pour connaître la valeur de votre portefeuille en 1 seconde !

## 🎯 Concept : Threading appliqué à votre Portfolio
Au lieu d'attendre chaque prix l'un après l'autre, vous lancez 7 requêtes simultanées. Pendant qu'AAPL se charge, GOOGL, MSFT et les autres se chargent aussi ! Votre portefeuille se met à jour ultra-rapidement.

## 🎯 Objectif
**Accélérez drastiquement la récupération des prix de votre portfolio complet.**

## 📝 Exercice
Créez `portfolio_threading.py` qui turbo-charge vos APIs :

### Fonction requise :
1. **`obtenir_prix_portfolio_rapide(portfolio)`** - utilise ThreadPoolExecutor pour récupérer tous vos prix en parallèle

## 📚 Ressources utiles
- https://docs.python.org/fr/3/library/threading.html
- https://www.geeksforgeeks.org/python/multithreading-python-set-1/

## ✅ Solution attendue
- **40-70 lignes** avec ThreadPoolExecutor
- Accélération spectaculaire : de 7s à ~1s
- Gestion d'erreurs thread-safe

