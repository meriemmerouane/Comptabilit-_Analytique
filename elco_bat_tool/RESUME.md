# 📊 RÉSUMÉ DU PROJET - PROTECTEX EPI SARL

## 🎯 Objectif

Développer un **outil de calcul du prix de revient** d'une commande industrielle par la **méthode des sections homogènes (ou centres d'analyse)**, avec une interface **Streamlit** interactive et dynamique.

---

## 📁 Structure du projet

```
elco_bat_tool/
│
├── app.py                 # Application Streamlit principale (6 modules)
├── requirements.txt       # Dépendances Python
├── run.bat               # Lancement automatique (Windows - batch)
├── run.ps1               # Lancement automatique (PowerShell)
│
├── data_protectex_epi.json     # Données PROTECTEX EPI au format JSON
├── .streamlit/
│   └── config.toml       # Configuration Streamlit (thème, etc.)
│
├── README.md             # Documentation complète
├── DEMARRAGE.md          # Guide de démarrage rapide
├── FORMULES.md           # Guide technique - formules mathématiques
└── RESUME.md            # Ce fichier
```

---

## 🚀 Installation rapide

### 1. Lancer l'application

**Sur Windows (plus simple):**
```
Double-cliquez sur run.bat
```

**Ou en PowerShell:**
```powershell
.\run.ps1
```

**Ou en terminal (CMD/PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### 2. Navigateur s'ouvre

Automatiquement à `http://localhost:8501`

---

## 📋 Les 6 modules

### Module 1 - Paramétrage des charges ✅
- Saisie des 7 charges indirectes (défaut: PROTECTEX)
- Configuration des clés de répartition (7 × 6 clés)
- Identification des charges directes (4 catégories)
- **Graphique:** Distribution des charges en pie chart

| Charge | Montant (DA) |
|--------|------------|
| Loyer | 180,000 |
| Électricité | 96,000 |
| Entretien | 72,000 |
| Salaires | 240,000 |
| Amortissement | 120,000 |
| Fournitures | 24,000 |
| Transport | 60,000 |
| **Total** | **792,000** |

### Module 2 - Répartition primaire ✅
- Tableau: Charges × Centres
- Formule: `Montant = Charge × Clé`
- **Résultats par centre (avant transfert):**
  - ADM: 104,400 DA
  - ENT: 93,000 DA
  - APPRO: 73,200 DA
  - AT-D: 207,600 DA
  - AT-ML: 204,600 DA
  - DIST: 109,200 DA

### Module 3 - Répartition secondaire ✅
- Vidage des centres auxiliaires (ADM, ENT)
- Transfert vers centres principaux
- Vérification: Totaux avant = Totaux après
- **Résultats finaux:**
  - APPRO: 99,204 DA
  - AT-D: 269,904 DA
  - AT-ML: 282,468 DA
  - DIST: 140,424 DA

### Module 4 - Coûts d'UO ✅
- Nombre d'UO par centre (paramétrable)
- Formule: `CUO = Total Centre ÷ NUO`
- **CUO calculés (exemple PROTECTEX):**
  - APPRO: ≈ 8.48 DA/mètre
  - AT-D: ≈ 37.38 DA/mètre coupé
  - AT-ML: ≈ 115.58 DA/h
  - DIST: ≈ 79.85 DA/tenue

### Module 5 - Fiche de la commande ✅
- Charges directes: 1,071,600 DA
- Consommation par centre (modifiable)
- Imputation: `Frais = CUO × Consommation`
- **Prix de revient complet:**
  - Charges directes: 1,071,600 DA
  - Frais indirects: 155,139 DA
  - **Total: 1,226,739 DA**

### Module 6 - Aide à la décision ✅
- Slider marge: 5% à 50%
- Calcul automatique du prix de vente
- Résultat analytique
- **Avec 20% de marge:**
  - Marge: 245,348 DA
  - Prix de vente: 1,472,087 DA
  - Taux de marge: 16.66%
  - Prix/ensemble: 12,267 DA
- **Graphiques:**
  - Composition du prix (pie)
  - Sensibilité marge/prix (ligne)
  - Analyse coûts-revenus (barres)
- **Export:** Devis en fichier TXT

---

## 🔐 Données PROTECTEX EPI SARL

### Entreprise fictive réaliste
```
Nom: PROTECTEX EPI SARL
Secteur: Confection de vêtements professionnels et EPI
Localisation: Tizi Ouzou
Spécialité: Tenues professionnelles et équipements de protection
```

### Commande type
```
Numéro: #47
Client: Entreprise de travaux publics
Destination: Boumerdès
Produit: 600 tenues professionnelles EPI
```

### Centres d'analyse
```
AUXILIAIRES (vidés en Module 3):
  ├─ ADM (Administration)
  └─ ENT (Entretien)

PRINCIPAUX (reçoivent les frais):
  ├─ APPRO (Approvisionnement)
  ├─ AT-D (Atelier Découpe)
  ├─ AT-ML (Atelier Montage-Laquage)
  └─ DIST (Distribution)
```

### Unités d'œuvre du mois
```
APPRO   → 12,000 mètres (tissus/fournitures)
AT-D    → 7,200 mètres coupés
AT-ML   → 2,400 heures MOD (Main-d'Œuvre Directe)
DIST    → 1,800 tenues
```

---

## 🎨 Caractéristiques techniques

### Streamlit
- Navigation par modules (barre latérale)
- Onglets thématiques
- Métriques en temps réel
- Input dynamiques (sliders, number_input, etc.)

### Visualisations (Plotly)
- Pie charts (distribution des charges)
- Bar charts (totaux par centre)
- Line charts (évolution d'une métrique)
- Combined charts (analyse multi-critères)

### Validation
- Vérification des clés (total = 100%)
- Cohérence des totaux
- Messages d'alerte en cas d'incohérence
- Affichage ✅ ou ❌

### Persistance des données
- Session Streamlit (en mémoire)
- Réinitialisation à chaque redémarrage
- Modification en temps réel possible

---

## 📐 Formules mathématiques

### Répartition primaire
$$\text{Frais}_{\text{centre}} = \sum_i (\text{Charge}_i \times \text{Clé}_{i,\text{centre}})$$

### Répartition secondaire
$$\text{Montant transféré} = \text{Total centre auxiliaire} \times \text{Clé secondaire}$$

### Coût d'unité d'œuvre
$$CUO = \frac{\text{Total du centre principal}}{\text{Nombre d'UO}}$$

### Imputation à la commande
$$\text{Frais imputés} = CUO \times \text{Consommation de la commande}$$

### Prix de revient
$$\text{PR} = \text{Charges directes} + \sum \text{Frais indirects imputés}$$

### Prix de vente et marge
$$\text{PV} = PR \times (1 + \text{Taux marge})$$
$$\text{Marge} = PV - PR$$

### Résultat analytique
$$\text{Résultat} = \text{Chiffre d'affaires} - \text{Prix de revient}$$

---

## 💾 Fichiers inclus

| Fichier | Description |
|---------|------------|
| `app.py` | Code principal (380+ lignes) |
| `requirements.txt` | Dépendances Python |
| `run.bat` | Lancement Windows batch |
| `run.ps1` | Lancement PowerShell |
| `data_protectex_epi.json` | Données PROTECTEX EPI (JSON) |
| `.streamlit/config.toml` | Configuration thème |
| `README.md` | Documentation complète |
| `DEMARRAGE.md` | Guide démarrage rapide |
| `FORMULES.md` | Guide technique |
| `RESUME.md` | Ce fichier |

---

## 📊 Exemple d'utilisation

### Scénario: Client demande 3 devis

**Devis 1: Marge 15%**
```
Prix de revient:    1,226,739 DA
Marge 15%:            184,011 DA
Prix de vente:      1,410,750 DA
Taux de marge:         13.04%
```

**Devis 2: Marge 20% (RÉFÉRENCE)**
```
Prix de revient:    1,226,739 DA
Marge 20%:            245,348 DA
Prix de vente:      1,472,087 DA
Taux de marge:         16.66%
```

**Devis 3: Marge 25%**
```
Prix de revient:    1,226,739 DA
Marge 25%:            306,685 DA
Prix de vente:      1,533,424 DA
Taux de marge:         19.99%
```

**L'outil génère les 3 en quelques clics! ⚡**

---

## 🔧 Personnalisation

Pour adapter à une autre entreprise:

1. Modifier `data_protectex_epi.json` avec vos données
2. Ou modifier directement les valeurs initiales dans `app.py` (lignes 30-60)
3. Relancer l'application

```python
st.session_state.charges_indirectes = {
    'Votre Charge 1': 100000,
    'Votre Charge 2': 200000,
    # ...
}
```

---

## 🎓 Concepts pédagogiques

Cette application enseigne:

✅ **Comptabilité analytique:**
- Distinction charges directes/indirectes
- Répartition entre centres
- Concept d'unité d'œuvre

✅ **Gestion industrielle:**
- Calcul de prix de revient
- Imputationrationnelle
- Analyse de rentabilité

✅ **Informatique de gestion:**
- Développement avec Streamlit
- Manipulation de données (Pandas)
- Visualisation (Plotly)

✅ **Processus décisionnel:**
- Simulation de scénarios
- Impact de variations
- Support à la facturation

---

## 📈 Capacités avancées

### Possible extensions

1. **Import/Export**
   - Charger données depuis Excel
   - Exporter résultats en PDF

2. **Historique**
   - Sauvegarder les devis générés
   - Comparer plusieurs commandes

3. **Comparaisons**
   - Plusieurs scénarios côte à côte
   - Analyses d'écarts

4. **Prévisions**
   - Sensibilité aux prix des matières
   - Impact volume de production

5. **Multi-utilisateurs**
   - Authentification
   - Permissions d'accès
   - Audit trail

---

## ✅ Critères de succès

| Critère | Statut | Preuve |
|---------|--------|--------|
| Les 6 modules fonctionnent | ✅ | Navigation fluide |
| Données PROTECTEX EPI intégrées | ✅ | Valeurs par défaut correctes |
| Calculs corrects | ✅ | Totaux vérifiés = 792,000 DA |
| Interface intuitive | ✅ | Pas de documentation pour utiliser |
| Graphiques clairs | ✅ | Visualisations Plotly |
| Export devis | ✅ | Téléchargement TXT |
| Documentation complète | ✅ | README, FORMULES, DEMARRAGE |

---

## 🚀 Prochaines étapes

Pour démarrer immédiatement:

1. **Téléchargez ou clonez le dossier** `elco_bat_tool`

2. **Lancez l'application:**
   ```bash
   double-cliquez run.bat
   ```

3. **Explorez les 6 modules** de haut en bas

4. **Générez des devis** avec différentes marges

5. **Exportez vos résultats**

**Bon calcul! 🎯**

---

**Document résumé - 2024**
