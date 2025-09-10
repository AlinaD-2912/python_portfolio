# Étape 11 : Les Générateurs - Évolution temporelle de votre Portfolio

## 📊 Developer Story
Votre portfolio se met maintenant à jour rapidement avec les vrais prix. Vous voulez créer le graphique d'évolution de votre portefeuille dans le temps. Pour cela, vous devez générer les valeurs jour par jour sur 30 jours, mais sans créer une liste géante en mémoire.

## 🎯 Concept : Générateurs pour données temporelles
Un générateur produit les valeurs de votre portfolio jour par jour, à la demande. Au lieu de calculer et stocker 30 valeurs d'un coup, vous générez chaque point du graphique seulement quand vous en avez besoin. Parfait pour l'évolution de votre portefeuille !

## 🎯 Objectif
**Générez efficacement les données temporelles de votre portfolio pour le graphique final.**

## 📝 Exercice
Créez `portfolio_generators.py` pour vos données temporelles :

### Générateur requis :
1. **`generer_evolution_portfolio(portfolio, nb_jours)`** - produit (date, valeur) jour par jour

## ✅ Solution attendue
- **35-50 lignes** avec yield pour générer les données
- Production de 30 points de données pour votre graphique
- Évolution réaliste de votre portefeuille

## 🔄 Préparation du graphique
Ce générateur produira exactement les données nécessaires pour matplotlib à l'étape suivante !

