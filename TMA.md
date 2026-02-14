# Plan de Maintenance Applicative (TMA)

Ce document décrit l'organisation de la maintenance de l'application **Task Manager Light**.

---

## 1. Types de maintenance

### Maintenance corrective

Correction des anomalies constatées en production ou lors des tests.

| Priorité | Description | Délai de prise en charge | Délai de résolution |
|----------|-------------|--------------------------|---------------------|
| Critique | L'application est inutilisable (crash, perte de données) | Immédiat | 4h |
| Majeure | Fonctionnalité importante dégradée | 4h | 24h |
| Mineure | Défaut cosmétique ou gêne légère | 48h | 1 semaine |

### Maintenance évolutive

Ajout de nouvelles fonctionnalités ou modification de fonctionnalités existantes à la demande du client ou des utilisateurs.

Exemples pour Task Manager Light :
- Ajout de priorités sur les tâches
- Ajout de filtres (tâches terminées / en cours)
- Export des tâches dans un autre format (CSV, XML)

### Maintenance préventive

Actions anticipées pour éviter la dégradation du projet dans le temps.

- Mise à jour des dépendances (`pytest`, `pytest-cov`, Python)
- Amélioration de la couverture de tests sur le code existant
- Refactoring du code identifié comme fragile ou peu lisible
- Revue et mise à jour de la documentation

---

## 2. Processus de traitement d'une demande

```
1. Réception        → Demande enregistrée (ticket)
2. Qualification     → Type (corrective / évolutive / préventive) + priorité
3. Analyse d'impact  → Fichiers concernés, risques de régression, estimation de charge
4. Développement     → Implémentation sur une branche dédiée
5. Tests             → Tests unitaires + vérification de non-régression
6. Revue de code     → Pull request relue par un pair
7. Livraison         → Merge sur main après validation CI
8. Vérification      → Contrôle en conditions réelles
```

### Règles

- Toute modification passe par une **pull request** avec revue.
- Les tests doivent passer en CI avant le merge.
- La documentation (`README.md`, `uml.md`, `GUIDELINES.md`) est mise à jour si nécessaire.
- Le ticket est fermé uniquement après vérification post-livraison.

---

## 3. Gestion des demandes d'évolution

### Cycle de vie d'une demande

```
Soumise → Qualifiée → Planifiée → En cours → Livrée → Clôturée
                ↘ Rejetée (avec justification)
```

### Contenu attendu d'une demande

| Champ | Description |
|-------|-------------|
| Titre | Description courte de l'évolution |
| Contexte | Pourquoi cette évolution est nécessaire |
| Description fonctionnelle | Comportement attendu du point de vue utilisateur |
| Critères d'acceptation | Conditions vérifiables pour valider la livraison |
| Impact estimé | Fichiers/classes concernés, complexité pressentie |

### Critères de priorisation

1. **Valeur métier** : quel gain pour l'utilisateur ?
2. **Coût de développement** : estimation de la charge.
3. **Risque technique** : impact sur l'existant, probabilité de régression.

---

## 4. Indicateurs de suivi de la qualité

| Indicateur | Mesure | Objectif | Outil |
|------------|--------|----------|-------|
| Couverture de tests | % de lignes couvertes | > 80% | `pytest --cov=src` |
| Taux de réussite des tests | Tests passants / total | 100% | CI GitHub Actions |
| Nombre de bugs ouverts | Tickets correctifs non résolus | Tendance à la baisse | Suivi tickets |
| Délai moyen de résolution | Temps entre ouverture et clôture d'un bug | Conforme aux SLA (section 1) | Suivi tickets |
| Dette technique | Nombre de TODO/FIXME dans le code | Tendance à la baisse | `grep -r TODO src/` |
| Fréquence de mise à jour des dépendances | Dernière date de mise à jour | < 3 mois | `pip list --outdated` |

### Revue périodique

Une revue qualité est réalisée à intervalle régulier pour :
- Analyser les indicateurs ci-dessus
- Identifier les zones de code fragiles
- Planifier les actions de maintenance préventive
- Mettre à jour ce document si les pratiques évoluent

---

## 5. Procédure en cas de bug critique

Un bug est **critique** lorsque l'application est inutilisable ou qu'il y a un risque de perte de données.

### Étapes

```
1. DÉTECTER    → Le bug est constaté et signalé immédiatement
2. CONFIRMER   → Reproduire le bug, identifier les conditions déclenchantes
3. ISOLER      → Identifier le fichier et la méthode en cause
4. CORRIGER    → Développer le correctif sur une branche hotfix/<description>
5. TESTER      → Écrire un test qui reproduit le bug, vérifier qu'il passe après correction
6. LIVRER      → Pull request prioritaire, revue accélérée, merge sur main
7. VÉRIFIER    → Confirmer la correction en conditions réelles
8. DOCUMENTER  → Renseigner la cause racine et la solution dans le ticket
```

### Règles spécifiques

- **Le correctif ne doit contenir que la correction du bug**, aucune autre modification.
- Un **test de non-régression** reproduisant le bug est obligatoire avant de merger.
- La branche suit la convention `hotfix/<description-courte>`.
- En cas d'indisponibilité du relecteur habituel, un autre membre de l'équipe peut valider.
- Une **analyse post-incident** est réalisée pour identifier comment prévenir ce type de bug à l'avenir.
