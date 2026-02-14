# Utilisation du CLI

## Lancer l'application

```shell
python -m src.cli
```

Un menu interactif s'affiche. Entrez le numéro de l'action souhaitée.

## Actions disponibles

### 1. Lister les tâches

Affiche toutes les tâches avec leur statut :

```
  1. [✓] Faire les courses - Acheter du pain
  2. [ ] Réviser Python - Chapitre 3
```

### 2. Ajouter une tâche

Vous serez invité à saisir un **nom** puis une **description**.

### 3. Marquer une tâche comme terminée

Affiche la liste puis demande le **numéro** de la tâche à marquer comme terminée.

### 4. Marquer une tâche comme non terminée

Même fonctionnement que l'action 3, mais remet la tâche en cours.

### 5. Supprimer une tâche

Affiche la liste puis demande le **numéro** de la tâche à supprimer.

### 6. Sauvegarder

Enregistre les tâches dans le fichier `tasks.json`.

### 7. Charger

Charge les tâches depuis le fichier `tasks.json`. Remplace la liste en mémoire.

### 8. Quitter

Ferme l'application. **Les modifications non sauvegardées sont perdues** — pensez à sauvegarder avant de quitter.
