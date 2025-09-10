# Étape 8 : Les Expressions Régulières - Valider vos symboles d'actions

## 📊 Developer Story
Votre Portfolio est maintenant monitoré automatiquement. Vous voulez créer une interface utilisateur où les gens peuvent ajouter de nouvelles actions à leur portefeuille. Mais vous devez valider que les symboles saisis (AAPL, GOOGL, etc.) respectent le bon format avant de les ajouter à votre portfolio.

## 🎯 Concept : Regex appliqué aux symboles financiers
Les expressions régulières permettent de vérifier que les symboles d'actions respectent le format standard (1-5 lettres majuscules). Avec votre portfolio concret, vous pouvez tester sur vos vrais symboles : AAPL ✓, GOOGL ✓, apple ✗, TOOLONG ✗.

## 🎯 Objectif
**Validez tous les symboles d'actions avant de les ajouter à votre Portfolio.**

## 📝 Exercice
Créez `portfolio_validation.py` qui sécurise vos entrées :

### Fonctions requises :
1. **`valider_symbole_action(symbole)`** - vérifie le format des symboles (1-5 lettres majuscules)
2. **`valider_portfolio_complet(positions)`** - valide tous les symboles d'un portfolio
3. **`nettoyer_symbole(symbole_brut)`** - convertit en majuscules et supprime les espaces

### Tests avec des données invalides :
symboles_invalides = ['apple', 'goog', '123', 'TOOLONG', 'AA PL', '']

## ✅ Solution attendue
- patterns regex appropriés
- Validation complète de votre portfolio

## 🔄 Application concrète
Sécurisez l'ajout de nouvelles positions/transactions à votre portefeuille.

## Truc en plus
N'hésitez pas à faire des regex de vérification pour les dates et/ou les prix.

