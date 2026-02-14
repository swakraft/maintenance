#!/bin/bash
set -e

echo "=== Exécution des tests avec couverture ==="
python -m pytest --cov=src --cov-report=xml

echo ""
echo "=== Lancement de l'analyse Sonar ==="
sonar-scanner
