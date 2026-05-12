# Script PowerShell pour lancer ELCO-BAT SARL
# ==============================================

# Couleurs
$Green = [System.ConsoleColor]::Green
$Yellow = [System.ConsoleColor]::Yellow
$Red = [System.ConsoleColor]::Red

Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor $Green
Write-Host "║  ELCO-BAT SARL - Outil de Calcul de Prix de Revient  ║" -ForegroundColor $Green
Write-Host "║  Méthode des sections homogènes                       ║" -ForegroundColor $Green
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor $Green
Write-Host ""

# Vérifier Python
Write-Host "[*] Vérification de Python..." -ForegroundColor $Yellow
$pythonCheck = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[✓] Python détecté: $pythonCheck" -ForegroundColor $Green
} else {
    Write-Host "[✗] ERREUR: Python n'est pas installé ou n'est pas dans le PATH" -ForegroundColor $Red
    Write-Host "   Veuillez installer Python 3.8+ depuis https://www.python.org" -ForegroundColor $Red
    Read-Host "Appuyez sur ENTER pour quitter"
    exit
}

Write-Host ""

# Vérifier/créer venv
if (-Not (Test-Path "venv")) {
    Write-Host "[*] Création de l'environnement virtuel..." -ForegroundColor $Yellow
    python -m venv venv
    Write-Host "[✓] Environnement virtuel créé" -ForegroundColor $Green
    
    Write-Host "[*] Activation de l'environnement virtuel..." -ForegroundColor $Yellow
    .\venv\Scripts\Activate.ps1
    
    Write-Host "[*] Installation des dépendances..." -ForegroundColor $Yellow
    pip install -r requirements.txt -q
    Write-Host "[✓] Dépendances installées" -ForegroundColor $Green
} else {
    Write-Host "[✓] Environnement virtuel trouvé" -ForegroundColor $Green
    Write-Host "[*] Activation de l'environnement virtuel..." -ForegroundColor $Yellow
    .\venv\Scripts\Activate.ps1
}

Write-Host ""
Write-Host "[*] ════════════════════════════════════════════════════" -ForegroundColor $Yellow
Write-Host "[*]          Démarrage de l'application..." -ForegroundColor $Yellow
Write-Host "[*] ════════════════════════════════════════════════════" -ForegroundColor $Yellow
Write-Host ""
Write-Host "📱 L'application s'ouvrira bientôt dans votre navigateur" -ForegroundColor $Green
Write-Host "   Adresse: http://localhost:8501" -ForegroundColor $Green
Write-Host ""
Write-Host "🛑 Pour arrêter le serveur:" -ForegroundColor $Yellow
Write-Host "   Appuyez sur Ctrl+C" -ForegroundColor $Yellow
Write-Host ""

streamlit run app.py

Write-Host ""
Write-Host "Application fermée." -ForegroundColor $Yellow
Read-Host "Appuyez sur ENTER pour quitter"
