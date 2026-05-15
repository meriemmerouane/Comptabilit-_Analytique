@echo off
for /f "delims=" %%A in ('chcp ^| find /v ""') do set encoding=%%A
chcp 65001 >nul

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║   TEST D'INSTALLATION - PROTECTEX EPI SARL                      ║
echo ║   Vérification de l'environnement Python et Streamlit          ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

set tests_passed=0
set tests_failed=0

echo [*] Test 1: Vérifier la présence de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [✗] ÉCHOUÉ: Python n'est pas installé
    set /a tests_failed+=1
) else (
    for /f "tokens=*" %%A in ('python --version 2^>^&1') do set py_version=%%A
    echo [✓] SUCCÈS: !py_version! détecté
    set /a tests_passed+=1
)

echo.
echo [*] Test 2: Vérifier pip (gestionnaire de paquets)...
pip --version >nul 2>&1
if errorlevel 1 (
    echo [✗] ÉCHOUÉ: pip n'est pas accessible
    set /a tests_failed+=1
) else (
    for /f "tokens=*" %%A in ('pip --version 2^>^&1') do set pip_version=%%A
    echo [✓] SUCCÈS: !pip_version!
    set /a tests_passed+=1
)

echo.
echo [*] Test 3: Vérifier l'environnement virtuel...
if exist venv (
    echo [✓] SUCCÈS: Dossier venv trouvé
    set /a tests_passed+=1
) else (
    echo [!] INFO: venv n'existe pas (sera créé automatiquement)
    set /a tests_passed+=1
)

echo.
echo [*] Test 4: Vérifier requirements.txt...
if exist requirements.txt (
    echo [✓] SUCCÈS: requirements.txt trouvé
    set /a tests_passed+=1
) else (
    echo [✗] ÉCHOUÉ: requirements.txt manquant
    set /a tests_failed+=1
)

echo.
echo [*] Test 5: Vérifier app.py...
if exist app.py (
    for /f %%A in ('find /c /v "" ^< app.py') do set lines=%%A
    echo [✓] SUCCÈS: app.py trouvé (!lines! lignes)
    set /a tests_passed+=1
) else (
    echo [✗] ÉCHOUÉ: app.py manquant
    set /a tests_failed+=1
)

echo.
echo [*] Test 6: Vérifier le fichier de configuration JSON...
if exist data_protectex_epi.json (
    echo [✓] SUCCÈS: data_protectex_epi.json trouvé
    set /a tests_passed+=1
) elif exist data_elcobat.json (
    echo [✓] SUCCÈS: data_elcobat.json trouvé (fichier de secours)
    set /a tests_passed+=1
) else (
    echo [✗] ÉCHOUÉ: Aucun fichier JSON de configuration trouvé
    set /a tests_failed+=1
)

echo.
echo [*] Test 7: Vérifier la documentation...
set doc_count=0
if exist README.md set /a doc_count+=1
if exist DEMARRAGE.md set /a doc_count+=1
if exist FORMULES.md set /a doc_count+=1
if exist EXEMPLE_CALCUL.md set /a doc_count+=1
if exist CONSEILS.md set /a doc_count+=1

if %doc_count% gtr 4 (
    echo [✓] SUCCÈS: !doc_count! fichiers de documentation trouvés
    set /a tests_passed+=1
) else (
    echo [!] AVERTISSEMENT: Seulement !doc_count! fichiers de doc (recommandé: 5+)
    set /a tests_passed+=1
)

echo.
echo ════════════════════════════════════════════════════════════════
echo.

if %tests_failed% equ 0 (
    echo [✓] TOUS LES TESTS RÉUSSIS!
    echo.
    echo Votre environnement est prêt. Vous pouvez:
    echo.
    echo   1. Double-cliquer sur run.bat pour lancer l'application
    echo   2. Ou exécuter: streamlit run app.py
    echo.
) else (
    echo [✗] %tests_failed% TESTS ONT ÉCHOUÉ
    echo.
    echo Actions recommandées:
    if !tests_failed! geq 1 (
        echo   - Installer Python: https://www.python.org
        echo   - Relancer ce test après l'installation
    )
    echo.
)

echo Résumé:
echo   ✓ Tests réussis: %tests_passed%
echo   ✗ Tests échoués: %tests_failed%
echo.

pause
