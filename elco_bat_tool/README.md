# 🏭 ELCO-BAT SARL - Outil de Calcul du Prix de Revient

Application Streamlit interactive pour le calcul du prix de revient d'une commande industrielle par la **méthode des sections homogènes**.

## 📋 Description

Cet outil permet de calculer précisément le prix de revient d'une commande de **120 ensembles de menuiserie aluminium** en appliquant la méthode des sections homogènes, puis de proposer un devis avec marge.

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

## 📊 Données par défaut (ELCO-BAT SARL)

**Charges indirectes (DA):**
- Loyer: 180,000
- Électricité: 96,000
- Entretien: 72,000
- Salaires: 240,000
- Amortissement: 120,000
- Fournitures: 24,000
- Transport: 60,000
- **Total: 792,000 DA**

**Centres d'analyse:**
- Auxiliaires: Administration (ADM), Entretien (ENT)
- Principaux: Approvisionnement (APPRO), Atelier Découpe (AT-D), Atelier Montage-Laquage (AT-ML), Distribution (DIST)

**Unités d'œuvre:**
- APPRO: 8,400 kg
- AT-D: 1,200 heures machine
- AT-ML: 2,400 heures MOD
- DIST: 720 ensembles

## 🚀 Installation et utilisation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner ou télécharger le dossier**
```bash
cd "c:\Users\ASUS\Desktop\GLOBALE\2CS_S2\tpcofi\elco_bat_tool"
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

## 📊 Résultats obtenus (données ELCO-BAT)

**Prix de revient final: 1,226,739 DA**

Répartition:
- Charges directes: 1,071,600 DA
- Frais indirects: 155,139 DA

**Devis avec 20% de marge: 1,472,087 DA**
- Prix unitaire: 12,267 DA/ensemble

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

Pour toute question sur les calculs, consultez les méthodes décrites dans le document ELCO-BAT SARL.

---

**Développé avec ❤️ pour ELCO-BAT SARL**
