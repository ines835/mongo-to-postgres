@echo off
title MongoDB → PostgreSQL - Import Automatisé

echo [1/3] Lancement de PostgreSQL via Docker...
docker compose up -d
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Erreur Docker : impossible de démarrer PostgreSQL.
    pause
    exit /b
)

echo [2/3] Installation des dépendances Python...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Erreur pip : impossible d’installer les paquets.
    pause
    exit /b
)

echo [3/3] Lancement du transfert des données MongoDB → PostgreSQL...
python main.py
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Erreur pendant l'import des données.
    pause
    exit /b
)

echo ✅ Import terminé ! tu peux aller sur power bi maintenant akhi fillah <3 
pause
