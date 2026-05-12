#!/usr/bin/env python3
"""
Test de validation de l'environnement Python
Vérifie que toutes les dépendances are correctement installées
"""

import sys
from pathlib import Path

def test_imports():
    """Teste l'import de tous les modules requis"""
    
    tests_passed = 0
    tests_failed = 0
    
    print("\n" + "="*60)
    print("  TEST D'INSTALLATION - Dépendances Python")
    print("="*60 + "\n")
    
    # Test 1: Streamlit
    print("[*] Test 1: Vérifier streamlit...")
    try:
        import streamlit
        version = streamlit.__version__
        print(f"[✓] SUCCÈS: Streamlit {version} installé")
        tests_passed += 1
    except ImportError as e:
        print(f"[✗] ÉCHOUÉ: {e}")
        tests_failed += 1
    
    # Test 2: Pandas
    print("\n[*] Test 2: Vérifier pandas...")
    try:
        import pandas
        version = pandas.__version__
        print(f"[✓] SUCCÈS: Pandas {version} installé")
        tests_passed += 1
    except ImportError as e:
        print(f"[✗] ÉCHOUÉ: {e}")
        tests_failed += 1
    
    # Test 3: NumPy
    print("\n[*] Test 3: Vérifier numpy...")
    try:
        import numpy
        version = numpy.__version__
        print(f"[✓] SUCCÈS: NumPy {version} installé")
        tests_passed += 1
    except ImportError as e:
        print(f"[✗] ÉCHOUÉ: {e}")
        tests_failed += 1
    
    # Test 4: Plotly
    print("\n[*] Test 4: Vérifier plotly...")
    try:
        import plotly
        version = plotly.__version__
        print(f"[✓] SUCCÈS: Plotly {version} installé")
        tests_passed += 1
    except ImportError as e:
        print(f"[✗] ÉCHOUÉ: {e}")
        tests_failed += 1
    
    # Test 5: Version Python
    print("\n[*] Test 5: Vérifier la version Python...")
    py_version = sys.version_info
    if py_version.major >= 3 and py_version.minor >= 8:
        print(f"[✓] SUCCÈS: Python {py_version.major}.{py_version.minor}.{py_version.micro} (compatible)")
        tests_passed += 1
    else:
        print(f"[✗] ÉCHOUÉ: Python {py_version.major}.{py_version.minor} (besoin 3.8+)")
        tests_failed += 1
    
    # Test 6: Fichiers de base
    print("\n[*] Test 6: Vérifier les fichiers de base...")
    base_dir = Path(__file__).parent
    required_files = ['app.py', 'data_elcobat.json', 'requirements.txt']
    
    files_ok = True
    for file in required_files:
        if (base_dir / file).exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} MANQUANT")
            files_ok = False
    
    if files_ok:
        tests_passed += 1
    else:
        tests_failed += 1
    
    # Test 7: Fonctionnalités Streamlit
    print("\n[*] Test 7: Tester les fonctionnalités Streamlit...")
    try:
        import streamlit as st
        # Vérifier que les éléments clés existent
        assert hasattr(st, 'set_page_config')
        assert hasattr(st, 'sidebar')
        assert hasattr(st, 'metric')
        assert hasattr(st, 'dataframe')
        print("[✓] SUCCÈS: API Streamlit disponible")
        tests_passed += 1
    except (ImportError, AssertionError) as e:
        print(f"[✗] ÉCHOUÉ: {e}")
        tests_failed += 1
    
    # Résumé
    print("\n" + "="*60)
    
    if tests_failed == 0:
        print("\n[✓] TOUS LES TESTS RÉUSSIS!")
        print("\nVotre environnement est correctement configuré.")
        print("Vous pouvez maintenant lancer l'application avec:")
        print("  • Double-cliquez sur run.bat")
        print("  • Ou: streamlit run app.py")
        print("\n")
        return 0
    else:
        print(f"\n[✗] {tests_failed} TEST(S) ONT ÉCHOUÉ")
        print(f"\nRésumé: {tests_passed} réussis, {tests_failed} échoués")
        print("\nVeuillez installer les dépendances manquantes:")
        print("  pip install -r requirements.txt")
        print("\n")
        return 1

def test_data_loading():
    """Test du chargement des données ELCO-BAT"""
    print("[*] Test 8: Charger les données ELCO-BAT...")
    try:
        import json
        base_dir = Path(__file__).parent
        with open(base_dir / 'data_elcobat.json', 'r') as f:
            data = json.load(f)
        
        # Vérifier les clés principales
        required_keys = ['entreprise', 'charges_indirectes', 'centres']
        for key in required_keys:
            assert key in data, f"Clé '{key}' manquante"
        
        print(f"[✓] SUCCÈS: Données chargées ({len(data)} sections)")
        return True
    except (IOError, json.JSONDecodeError, AssertionError) as e:
        print(f"[✗] ÉCHOUÉ: {e}")
        return False

if __name__ == "__main__":
    try:
        result = test_imports()
        
        if result == 0:
            # Tester aussi le chargement des données
            test_data_loading()
        
        sys.exit(result)
    
    except KeyboardInterrupt:
        print("\n\n[!] Test interrompu par l'utilisateur")
        sys.exit(1)
    
    except Exception as e:
        print(f"\n[✗] Erreur inattendue: {e}")
        sys.exit(1)
