# 🏭 PROTECTEX EPI SARL - Outil de Calcul du Prix de Revient

Application Streamlit interactive pour le calcul du prix de revient d'une commande de vêtements professionnels (EPI) par la **méthode des sections homogènes**.

## 📋 Description

Cet outil permet de calculer précisément le prix de revient d'une commande de **tenues professionnelles (EPI)** en appliquant la méthode des sections homogènes, puis de proposer un devis avec marge.

## 🎯 Fonctionnalités

### Module 1 - Paramétrage des charges
- Saisie dynamique des charges indirectes
- Configuration des clés de répartition
- Identification des charges directes
- Visualisation avec graphiques en secteurs

### Module 2 - Répartition primaire
- Tableau de répartition par charges et centres
- Calcul automatique des ventilations
- Affichage des totaux par centre
- Graphiques de distribution

### Module 3 - Répartition secondaire
- Vidage des centres auxiliaires
- Transfert vers centres principaux
- Vérification de cohérence
- Totaux finaux garantis

### Module 4 - Coûts d'UO
- Configuration des unités d'œuvre
- Calcul automatique des CUO
- Tableaux détaillés par centre
- Analyses comparatives

### Module 5 - Fiche de la commande
- Charges directes de la commande
- Consommation par centre
- Imputation des frais indirects
- Fiche complète du prix de revient

### Module 6 - Aide à la décision
- Calcul du résultat analytique
- Simulation de marges
- Proposition de devis
- Graphiques d'analyse (composition, sensibilité)
- **Exportation du devis en fichier texte**

## 📊 Données par défaut (PROTECTEX EPI SARL)

La configuration par défaut est chargée automatiquement depuis `data_protectex_epi.json`.

**Charges indirectes (DA):**
- Loyer: 180,000
- Électricité / énergie: 96,000
- Entretien matériels: 72,000
- Salaires personnel indirect: 240,000
- Amortissement machines: 120,000
- Fournitures administratives: 24,000
- Transport / livraison: 60,000
- **Total: 792,000 DA**

**Centres d'analyse:**
- Auxiliaires: Administration (ADM), Entretien (ENT)
- Principaux: Approvisionnement (APPRO), Atelier Coupe (AT-D), Atelier Couture/Assemblage (AT-ML), Distribution / Finition (DIST)

**Unités d'œuvre:**
- APPRO: 12,000 mètres (tissus / fournitures)
- AT-D: 7,200 mètres coupés
- AT-ML: 2,400 heures MOD
- DIST: 1,800 tenues

## 🚀 Installation et utilisation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner ou télécharger le dossier**
```bash
cd "c:\Users\HP\Videos\Comptabilit-_Analytique\elco_bat_tool"
```

2. **Créer un environnement virtuel (recommandé)**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou source venv/bin/activate  # Linux/Mac
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

### Lancer l'application

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à `http://localhost:8501`

## 💡 Guide d'utilisation

### Flux de navigation recommandé

1. **Commencer par le Module 1** pour valider/modifier les données de base
2. **Passer au Module 2** pour voir la répartition primaire
3. **Continuer au Module 3** pour le vidage des auxiliaires
4. **Consulter Module 4** pour les coûts d'unités d'œuvre
5. **Remplir Module 5** avec les données de la commande spécifique
6. **Finir par Module 6** pour générer le devis

### Modification des données

- **Charges indirectes**: Modifiables directement dans Module 1
- **Clés de répartition**: Utiliser les sliders pour ajuster les pourcentages
- **Données de commande**: Entrer les valeurs spécifiques dans Module 5
- **Marge**: Ajuster le taux dans Module 6

## 📊 Résultats obtenus (données PROTECTEX)

**Prix de revient final (exemple par défaut): ≈ 1,454,835 DA**

Répartition:
- Charges directes: 1,200,000 DA
- Frais indirects imputés (commande): ≈ 254,835 DA

**Devis avec 20% de marge: ≈ 1,745,802 DA**
- Prix unitaire: ≈ 2,910 DA/tenue

## 🎨 Interface utilisateur

- **Navigation par modules** via la barre latérale
- **Onglets thématiques** pour chaque module
- **Graphiques interactifs** (Plotly) pour visualiser les données
- **Métriques en temps réel** pour les totaux clés
- **Validation automatique** des calculs

## 📥 Export

Possibilité de télécharger le devis en format texte depuis le Module 6.

## 📝 Notes techniques

- **Framework**: Streamlit (interface web légère)
- **Visualisation**: Plotly (graphiques interactifs)
- **Données**: Pandas (structure et calculs)
- **État**: Session Streamlit (persistance pendant la navigation)

## 🔒 Validation des données

- Vérification automatique de la cohérence des clés de répartition (total = 100%)
- Contrôle des totaux lors du vidage des centres auxiliaires
- Messages d'alerte en cas d'incohérence

## ⚙️ Personnalisation

Pour adapter l'outil à une autre entreprise:
1. Modifier les valeurs dans `st.session_state` au démarrage
2. Ajuster les noms des centres et charges selon vos besoins
3. Changer les clés de répartition selon votre structure

## 📞 Support

Pour toute question sur les calculs, consultez les méthodes décrites dans la documentation du projet.

---

**Développé pour PROTECTEX EPI SARL**
