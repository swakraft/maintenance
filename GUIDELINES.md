# GUIDELINES

Ce document a pour but d'expliquer les bonnes pratiques d'évolution du projet en matière de qualité.

## Conventions de code

- **Langage** : Python 3.13
- **Nommage** : snake_case pour les fonctions et variables, PascalCase pour les classes.
- **Encapsulation** : les attributs des classes sont privés (préfixe `__`). L'accès se fait via des getters/setters explicites.
- **Typage** : les signatures de méthodes doivent inclure les type hints (paramètres et retour).

## Structure du projet

- Le code source est dans `src/models/`.
- Les tests sont dans `tests/`, avec un fichier par thématique (modèle, ajout/suppression, persistance).
- Les fichiers de données de test sont dans `tests/fixtures/`.
- Un fichier ne doit contenir qu'une seule classe.

## Tests

- **Tout nouveau code doit être couvert par des tests unitaires.**
- Les tests utilisent `pytest` et se lancent via `python -m pytest`.
- Chaque fonction de test ne vérifie qu'un seul comportement.
- Nommage des tests : `test_<comportement_testé>` (ex : `test_mark_as_done`).
- Les données de test (fixtures JSON) sont versionnées dans `tests/fixtures/`.
- Vérifier la couverture régulièrement avec `python -m pytest --cov=src`.

## Git et intégration continue

- La branche principale est `main`.
- Les modifications passent par des **pull requests** vers `main`.
- La pipeline CI exécute les tests automatiquement à chaque push et pull request sur `main` (voir `.github/workflows/tests.yml`).
- **Ne pas merger une PR si les tests échouent.**
- Les messages de commit sont concis et décrivent le "pourquoi" du changement.

## Documentation

- Le `README.md` décrit la structure du projet, le setup et les commandes utiles.
- Le diagramme de classes (`uml.md`) doit être mis à jour à chaque modification de l'architecture (ajout/suppression de classe ou de méthode publique).
- Ce fichier `GUIDELINES.md` doit être maintenu à jour au fil de l'évolution des pratiques.
