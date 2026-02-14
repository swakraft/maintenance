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
sonar.sh          # Script local : tests + analyse SonarQube
sonar-project.properties.template  # Configuration SonarQube (template)
.github/workflows/tests.yml       # Pipeline CI : tests + Sonar automatique
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

### Automatique (CI)

L'analyse SonarQube est exécutée automatiquement par la pipeline GitHub Actions à chaque push ou pull request sur `main`. La pipeline lance les tests avec couverture, puis envoie les résultats à Sonar.

Secret à configurer dans GitHub (Settings > Secrets and variables > Actions) :

| Secret | Valeur |
|--------|--------|
| `SONAR_TOKEN` | Token d'authentification SonarQube |

### En local

Copiez le template et renseignez votre token :
```shell
cp sonar-project.properties.template sonar-project.properties
# Éditez sonar-project.properties pour renseigner sonar.token
```

Puis lancez les tests et l'analyse en une commande :
```shell
./sonar.sh
```

Prérequis : `sonar-scanner` doit être installé et accessible dans le PATH.

## Dépendances

- **pytest** : framework de tests
- **pytest-cov** : mesure de couverture de code
