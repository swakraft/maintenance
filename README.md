# Task Manager Light

Gestionnaire de tâches minimaliste en Python. Permet de créer, modifier, supprimer des tâches et de les persister au format JSON.
https://github.com/swakraft/maintenance

## Structure du projet

```
src/
  cli.py          # Client en ligne de commande (menu interactif)
  models/
    Task.py       # Modèle d'une tâche (nom, description, statut)
    TaskList.py   # Collection de tâches avec persistance JSON
tests/
  fixtures/       # Fichiers JSON de test
  test_task_model.py          # Tests unitaires du modèle Task
  test_appending_removing.py  # Tests ajout/suppression dans TaskList
  test_memory.py              # Tests de persistance (save/load)
tasks.json        # Fichier de données (liste de tâches)
sonar.sh          # Script : tests + analyse SonarQube
sonar-project.properties  # Configuration SonarQube
uml.md            # Diagramme de classes PlantUML
```

## Architecture

Voir le diagramme de classes dans [uml.md](uml.md).

- **Task** : représente une tâche avec un nom, une description et un statut (fait/non fait). Sérialisable en JSON. L'égalité entre deux tâches est déterminée par leur nom et leur description.
- **TaskList** : gère une collection de `Task`. Fournit la persistance vers/depuis un fichier JSON.

## Utilisation

```shell
python -m src.cli
```

## Setup

```shell
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Tests

Lancer tous les tests :
```shell
python -m pytest
```

Lancer un test précis :
```shell
python -m pytest tests/test_memory.py::test_load_from_empty_file
```

Lancer avec couverture :
```shell
python -m pytest --cov=src
```

Ou via l'onglet Test de VSCode (choisir pytest), puis "Exécuter les tests avec couverture".

## Analyse SonarQube

Configurez le fichier `sonar-project.properties.template`. Retirez le .template et fournissez un token.
Lancer les tests puis l'analyse Sonar en une commande :
```shell
./sonar.sh
```
Note : peut être chmod +x le fichier shell d'abord.

Prérequis : `sonar-scanner` doit être installé et accessible dans le PATH.

## Dépendances

- **pytest** : framework de tests
- **pytest-cov** : mesure de couverture de code
