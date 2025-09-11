# Étape 7 : Les Décorateurs - Surveiller automatiquement votre Portfolio

## 📊 Developer Story
Votre classe Portfolio fonctionne. Maintenant vous voulez surveiller combien de temps prennent vos calculs. Certaines opérations (comme calculer tous les rendements) pourraient être lentes, mais vous ne voulez pas modifier toutes vos méthodes Portfolio existantes.

## 🎯 Concept : Décorateurs appliqués aux méthodes financières
Un décorateur "enrobe" vos méthodes Portfolio pour y ajouter des fonctionnalités (du monitoring automatique avec @chronometer). Vous pouvez mesurer le temps d'exécution de `calculer_valeur_totale()`, `calculer_performance()`, etc., sans changer une ligne dans vos méthodes existantes.

## 🎯 Objectif
**Ajoutez du monitoring automatique à vos méthodes Portfolio sans les modifier.**

## 📝 Exercice
Créez `portfolio_decorators.py` avec décorateurs spécialisés :

### Décorateur requis :
1. **`@chronometer`** - mesure le temps d'exécution des méthodes portfolio

### Décorateurs optionnels :
2. **`@logger_portfolio`** - log les opérations dans un fichier
3. **`@cache_prix`** - cache les résultats pour éviter les recalculs -> très important en entreprise,notamment sur les gros volumes de données ou les opérations répétitives.

## ✅ Solution attendue
- Monitoring automatique sur vos calculs avec @chronometer
- Application sur vos méthodes Portfolio existantes

## 📚 Ressources utiles
- https://blog.stephane-robert.info/docs/developper/programmation/python/decorateur/
- https://www.programiz.com/python-programming/args-and-kwargs

## 🔄 Réflexion
Quoi décorer et quand ?
Trouvez quelles opérations sont les plus lentes sur votre portfolio pour optimiser intelligement

