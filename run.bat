@echo off
title MongoDB → PostgreSQL - Import Automatisé

REM === Création de l'env virtuel ===
if not exist env (
    echo 🐍 Création de l'environnement virtuel Python...
    python -m venv env
    IF %ERRORLEVEL% NEQ 0 (
        echo ❌ Erreur : impossible de créer l'environnement virtuel.
        pause
        exit /b
    )
)

REM === Activation ===
call env\Scripts\activate.bat

echo [1/4] Lancement de PostgreSQL via Docker...
docker compose up -d
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Erreur Docker : impossible de démarrer PostgreSQL.
    pause
    exit /b
)

echo [2/4] Installation des dépendances Python...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Erreur pip : impossible d’installer les paquets.
    pause
    exit /b
)

echo [3/4] Lancement du transfert des données MongoDB → PostgreSQL...
python main.py
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Erreur pendant l'import des données.
    pause
    exit /b
)

echo [4/4] ✅ Import terminé ! Tu peux aller sur Power BI maintenant akhi fillah ❤️
pause
