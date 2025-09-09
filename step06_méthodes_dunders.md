# Étape 6 : Classe Portfolio - Les méthodes dunder ou méthodes magiques

## 📊 Developer Story
Vous avez maintenant toutes les briques de base : chargement de données, structures namedtuple, calculs lambda, traitement map, gestion d'erreurs. Il est temps de tout organiser dans une classe Portfolio professionnelle qui encapsule votre portefeuille de 47 000€ et toutes ses opérations.

## 🎯 Concept : Classe avec dunder methods (dunder = double underscore)
Une classe Portfolio avec des méthodes dunder (`__str__`, `__len__`, etc.) vous permet de manipuler votre portfolio comme un objet Python naturel. Vous pouvez faire `print(mon_portfolio)`, `len(mon_portfolio)`, et toutes les opérations deviennent intuitives.

## 🎯 Objectif
**Créez une classe Portfolio complète qui encapsule toutes vos opérations précédentes.**

## 📝 Exercice
Créez `portfolio_class.py` avec votre classe principale :

### Méthodes magiques requises :
1. **`__init__(self, positions)`** - initialise avec vos positions réelles
2. **`__str__(self)`** - affichage lisible du portfolio
3. **`__len__(self)`** - nombre de positions
4. (optionnel) **Quelles autres méthodes dunder seraient pertinentes ?**

### Méthodes métier requises :
4. **`calculer_valeur_totale()`** - utilise vos lambdas et map des étapes précédentes
5. **`obtenir_position(self, symbol)`** - trouve une position par symbole
6. **`calculer_performance(self, prix_actuels)`** - performance globale

## 📚 Ressources utiles
- https://www.geeksforgeeks.org/python/dunder-magic-methods-python/
- https://www.pythonmorsels.com/every-dunder-method/
- https://www.geeksforgeeks.org/python/namedtuple-in-python/ Regardez cette ressource et notamment la fin avec les méthodes dunder des namedtuple. Pour lier cette nouvelle connaissance avec les namedtuple vus précedemment

## ✅ Solution attendue
- **60-100 lignes** utilisant tous vos outils précédents
Posez-vous et repensez à l'objectif final (gérer un portfolio d'actions). 
Réfléchissez à la strucure de vos données et faites un point d'étape sur :
- qu'est-ce que j'ai fait jusque là ; 
- qu'est-ce qui est désormais en trop / redondant dans mon programme
- qu'est-ce qu'il manque à mon programme ?

PS : vous pouvez sûrement apporter des modifications et/ou renommer votre méthode afficher_portfolio créée précedemment