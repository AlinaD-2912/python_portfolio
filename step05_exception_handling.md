# Étape 5 : La Gestion d'Exceptions - Sécuriser vos calculs portfolio

## 📊 Developer Story
Maintenant que vous traitez des données portfolio réelles (fichiers CSV, calculs financiers, map sur plusieurs actions), vous vous rendez compte que plein de choses peuvent mal se passer : fichier portfolio corrompu, prix manquants, divisions par zéro dans vos calculs de rendement. Vous voulez que votre application continue de fonctionner même avec des données imparfaites.

## 🎯 Concept : Exceptions appliquées aux données financières
La gestion d'exceptions devient concrète quand vous avez de vraies opérations qui peuvent échouer. Avec votre portfolio réel, vous pouvez maintenant gérer des cas d'erreur réalistes : que faire si le prix d'achat AAPL est 0 ? Si le fichier portfolio est corrompu ? Si une action n'a pas de prix actuel ?

## 📚 Ressources utiles
- [Documentation Python sur la gestion d'exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Complete guide exception and error handling ](https://www.datacamp.com/tutorial/exception-handling-python)

## 🎯 Objectif
**Sécurisez toutes vos opérations portfolio contre les erreurs de données réelles.**

## 📝 Exercice
Créez `portfolio_exceptions.py` qui sécurise vos opérations :

### Éléments requis (miiiiiinimum):
1. **`ErreurDonneesPortfolio`** - exception personnalisée pour les erreurs portfolio
2. **`charger_portfolio_securise(fichier)`** - version sécurisée du chargement
3. **`calculer_gains_securise(positions, prix_actuels)`** - version sécurisée des calculs

### Elements requis pour un minimum de proffessionalisme
Sécurisez maintenant toutes vos fonctions des étapes 1-4 !
En réalité, il y a plein d'exceptions à gérer. Avec les nombres notamment, il y a toujours des exceptions (comme la ZeroDivisionError). Et plein d'autres...
4. Gérer les erreurs et exceptions de la manière la complète possible mais surtout, souvenez-vous de continuer à les gérer (notamment plus tard lorsque vous ferez intervenir un élément extérieur à votre programme, comme une API)

### Tests avec données problématiques :
```python
# Testez avec des données corrompues
positions_problematiques = [
    Position('AAPL', 10, 0.0, '2023-01-15'),      # Prix d'achat = 0 !
    Position('INVALID', 5, 100.0, '2023-02-01'),  # Symbole inexistant
    Position('GOOGL', -10, 2500.0, '2023-03-01')  # Quantité négative !
]
```

## ✅ Solution attendue
- Une gestion robuste des erreurs
- Tests avec vos données portfolio corrompues
- Messages d'erreur utiles pour chaque cas


