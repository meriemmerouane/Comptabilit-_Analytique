@echo off
REM Script de lancement de l'application ELCO-BAT SARL
REM ====================================================

cls
echo.
echo  ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
echo  *  ELCO-BAT SARL - Outil de Calcul de Prix de Revient    *
echo  *  Méthode des sections homogènes                         *
echo  ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installé ou n'est pas dans le PATH
    echo Veuillez installer Python 3.8+ depuis https://www.python.org
    pause
    exit /b 1
)

echo [✓] Python détecté
echo.

REM Vérifier si venv existe, sinon le créer
if not exist venv (
    echo [*] Création de l'environnement virtuel...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [✓] Environnement virtuel créé
    echo [*] Installation des dépendances...
    pip install -r requirements.txt
    echo [✓] Dépendances installées
) else (
    echo [✓] Environnement virtuel trouvé
    call venv\Scripts\activate.bat
)

echo.
echo [*] Démarrage de l'application...
echo [*] L'application s'ouvrira bientôt dans votre navigateur
echo [*] Appuyez sur CTRL+C pour arrêter le serveur
echo.

streamlit run app.py

pause
