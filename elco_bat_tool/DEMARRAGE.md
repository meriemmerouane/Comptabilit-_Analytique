# 🚀 DÉMARRAGE RAPIDE

## Installation (première utilisation)

### Étape 1: Ouvrir le dossier de l'application

Accédez au dossier:
```
c:\Users\ASUS\Desktop\GLOBALE\2CS_S2\tpcofi\elco_bat_tool
```

### Étape 2: Exécuter le fichier de lancement

**Sur Windows (recommandé):**
- Double-cliquez sur `run.bat`
- Attendez que l'application se charge

**Ou par terminal (PowerShell/CMD):**

```powershell
# Windows PowerShell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### Étape 3: L'application se lance

- Votre navigateur s'ouvrira automatiquement
- Adresse locale: `http://localhost:8501`

---

## 📖 Guide d'utilisation - Flux complet

### Module 1️⃣ - Paramétrage des charges

**Onglet "Charges indirectes":**
1. Vérifiez/modifiez les 7 charges indirectes
2. Le total s'affiche automatiquement
3. Un graphique en secteurs montre la distribution

**Onglet "Clés de répartition":**
1. Sélectionnez une charge (ex: "Loyer")
2. Ajustez les sliders par centre
3. Le total des clés doit être 100%
4. Consultez le tableau récapitulatif

**Onglet "Charges directes":**
1. Saisissez les charges directes de la commande
2. Vérifiez le total
3. Cet onglet peut être révisité dans Module 5

✅ **Résultat:** Configuration prête pour les calculs

---

### Module 2️⃣ - Répartition primaire

**Tableau de répartition:**
- Affiche la ventilation de chaque charge par centre
- Colonne "Total": somme par charge
- Ligne "Totaux colonnes": montant par centre

**Graphiques:**
- **"Par centre":** Barres montrant le total par centre
- **"Par charge":** Lignes montrant l'évolution des charges

✅ **Résultat:** Totaux périmaires calculés pour chaque centre

---

### Module 3️⃣ - Répartition secondaire

**Clés de répartition secondaire:**
1. Pour chaque centre auxiliaire (ADM, ENT):
   - Sliders pour distribution vers autres centres
   - Must sum to 100%

**Vidage automatique:**
- Affiche étape par étape comment les montants sont transférés
- Consolide dans les centres principaux

**Vérification:**
- Compare total avant/après
- Affiche ✅ ou ❌ selon la cohérence

✅ **Résultat:** Totaux finaux des 4 centres principaux

---

### Module 4️⃣ - Coûts d'UO

**Configuration:**
1. Entrez le nombre d'unités d'œuvre pour chaque centre
   - APPRO en kg
   - AT-D en heures machine
   - AT-ML en heures MOD
   - DIST en ensembles

**Calculs automatiques:**
- CUO = Total du centre ÷ NUO
- Tableau récapitulatif avec les 3 colonnes

**Graphiques:**
- Barres du total par centre
- Barres du CUO par centre

✅ **Résultat:** CUO prêt pour l'imputation

---

### Module 5️⃣ - Fiche de la commande

**Section A - Charges directes:**
1. Saisissez les montants des charges directes
   - Aluminium, vitrage, quincaillerie, MOD
2. Le total s'affiche

**Section B - Consommation par centre:**
1. Entrez les quantités consommées:
   - APPRO: kg utilisés
   - AT-D: heures travaillées
   - AT-ML: heures MOD utilisées
   - DIST: nombre d'ensembles

**Section C - Frais indirects:**
- Tableau automatique: Consommation × CUO
- Affiche le montant imputé par centre

**Prix de revient:**
- Additionne charges directes + frais indirects
- Affichage multimédia avec les montants clés

✅ **Résultat:** Prix de revient complet

---

### Module 6️⃣ - Aide à la décision (Devis)

**Paramètres d'entrée:**
1. **Prix de revient:** Automatiquement depuis Module 5
2. **Marge souhaitée (%):** Utilisez le slider (5 à 50%)
3. **Nombre d'unités:** Provient du Module 5

**Calculs:**
- Marge (DA) = Prix revient × Taux %
- Prix de vente = Prix revient + Marge
- Prix unitaire = Prix total ÷ Nombre d'unités

**Analyse:**
- Taux de marge (%)
- Coefficient multiplicateur
- Graphique de composition (pie chart)
- Sensibilité prix/marge (courbe)

**Devis à exporter:**
- Format texte lisible
- Synthèse complète
- Bouton télécharger

✅ **Résultat:** Devis professionnel exportable

---

## 💾 Données ELCO-BAT par défaut

### Charges indirectes (total: 792,000 DA)
```
Loyer               180,000 DA
Électricité          96,000 DA
Entretien            72,000 DA
Salaires            240,000 DA
Amortissement       120,000 DA
Fournitures          24,000 DA
Transport            60,000 DA
```

### Centres d'analyse
```
AUXILIAIRES:
  • ADM (Administration)
  • ENT (Entretien)

PRINCIPAUX:
  • APPRO (Approvisionnement)
  • AT-D (Atelier Découpe)
  • AT-ML (Atelier Montage-Laquage)
  • DIST (Distribution)
```

### Unités d'œuvre (du mois)
```
APPRO   → 8,400 kg d'aluminium
AT-D    → 1,200 heures machine
AT-ML   → 2,400 heures MOD
DIST    → 720 ensembles
```

---

## 🎯 Résultats attendus

### Répartition primaire
```
ADM:   104,400 DA (charges admin)
ENT:    93,000 DA (entretien)
APPRO:  73,200 DA
AT-D:  207,600 DA
AT-ML: 204,600 DA
DIST:  109,200 DA
```

### Après répartition secondaire
```
APPRO:  99,204 DA
AT-D:  269,904 DA
AT-ML: 282,468 DA
DIST:  140,424 DA
TOTAL: 792,000 DA ✓
```

### Coûts d'UO
```
APPRO   11.81 DA/kg
AT-D   224.92 DA/h
AT-ML  117.70 DA/h
DIST   195.03 DA/ensemble
```

### Prix final (commande Boumerdès)
```
Charges directes:    1,071,600 DA
Frais indirects:       155,139 DA
─────────────────────────────
Prix de revient:     1,226,739 DA

Avec 20% de marge:     245,348 DA
─────────────────────────────
PRIX DE VENTE:       1,472,087 DA

Par ensemble:           12,267 DA/U
```

---

## 🔧 Dépannage

### L'application ne démarre pas

**Problème:** Python n'est pas installé
```
→ Téléchargez Python 3.8+ depuis python.org
→ Pendant l'installation, cochez "Add Python to PATH"
```

**Problème:** Module Streamlit introuvable
```
→ Activez l'environment virtuel: venv\Scripts\activate
→ Installez les dépendances: pip install -r requirements.txt
```

### Les données ne sont pas correctes

**→** Vérifiez les clés de répartition (doivent totaliser 100% par charge)
**→** Relancez l'application (Ctrl+C puis relancer)
**→** Les données se réinitialisent à chaque nouveau démarrage

### Modifier les données d'une autre entreprise

1. Ouvrez `data_elcobat.json`
2. Modificquez les valeurs JSON
3. Pour intégrer: modifiez `app.py` pour charger le JSON
4. Relancez l'application

---

## 📞 Raccourcis utiles

| Action | Touches/Boutons |
|--------|-----------------|
| Relancer l'application | Appuyez sur "R" |
| Arrêter le serveur | Ctrl + C (dans terminal) |
| Ouvrir developer tools | F12 (navigateur) |
| Réinitialiser le cache | Delete cookies du navigateur |

---

## 📝 Notes importantes

✅ **L'application sauvegarde vos modifications en session**
- Les données persistent pendant que vous naviguez
- Elles se réinitialisent si vous fermez l'onglet

✅ **Tous les calculs sont validés**
- Vérification automatique des clés (doit = 100%)
- Vérification de cohérence des totaux

✅ **Export du devis**
- Téléchargez depuis Module 6
- Format TXT lisible partout

---

**Bonne utilisation! 🚀**

Pour plus de détails techniques, consultez:
- `README.md` - Guide complet
- `FORMULES.md` - Détails mathématiques
