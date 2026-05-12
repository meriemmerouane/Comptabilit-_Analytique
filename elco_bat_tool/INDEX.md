# 📚 INDEX DE LA DOCUMENTATION

Bienvenue dans le dossier **ELCO-BAT SARL - Outil de Calcul du Prix de Revient**

## 🚀 PAR OÙ COMMENCER?

### Si vous êtes pressé (5 minutes)
1. **Lisez:** [`DEMARRAGE.md`](DEMARRAGE.md) - Guide rapide
2. **Exécutez:** Double-cliquez `run.bat`
3. **Explorez:** Les 6 modules dans l'application

### Si vous voulez tout comprendre (30 minutes)
1. **Lisez:** [`README.md`](README.md) - Documentation complète
2. **Suivez:** [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md) - Calculs détaillés
3. **Lancez:** `run.bat` ou `streamlit run app.py`

### Si vous avez des questions
1. **Consultez:** [`CONSEILS.md`](CONSEILS.md) - Bonnes pratiques
2. **Comprenez:** [`FORMULES.md`](FORMULES.md) - Fondements mathématiques
3. **Vérifiez:** [`RESUME.md`](RESUME.md) - Vue d'ensemble du projet

---

## 📄 FICHIERS DE DOCUMENTATION

### 📖 Documentation générale

| Fichier | Description | Durée de lecture | Niveau |
|---------|-------------|------------------|--------|
| [`README.md`](README.md) | Documentation complète du projet | 15 min | Intermédiaire |
| [`DEMARRAGE.md`](DEMARRAGE.md) | Guide de démarrage rapide | 10 min | Débutant |
| [`RESUME.md`](RESUME.md) | Vue d'ensemble du projet | 10 min | Débutant |

### 🧮 Documentation technique

| Fichier | Description | Durée de lecture | Niveau |
|---------|-------------|------------------|--------|
| [`FORMULES.md`](FORMULES.md) | Fondements mathématiques et formules | 20 min | Avancé |
| [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md) | Exemple complet pas à pas | 25 min | Intermédiaire |
| [`CONSEILS.md`](CONSEILS.md) | Bonnes pratiques et astuces | 15 min | Débutant |

### 📦 Fichiers de données

| Fichier | Description | Type |
|---------|-------------|------|
| [`data_elcobat.json`](data_elcobat.json) | Données ELCO-BAT en JSON | Configuration |
| [`requirements.txt`](requirements.txt) | Dépendances Python | Configuration |
| [`.streamlit/config.toml`](.streamlit/config.toml) | Configuration Streamlit | Configuration |

### 🔧 Fichiers d'application

| Fichier | Description | Exécutable |
|---------|-------------|-----------|
| [`app.py`](app.py) | Application Streamlit (380+ lignes) | `streamlit run` |
| [`run.bat`](run.bat) | Lancement automatique Windows | Oui (double-clic) |
| [`run.ps1`](run.ps1) | Lancement PowerShell | Oui |

---

## 🎯 PARCOURS D'APPRENTISSAGE RECOMMANDÉ

### Pour apprendre les concepts

```
1️⃣ README.md (overview général)
         ↓
2️⃣ DEMARRAGE.md (premiers pas)
         ↓
3️⃣ Lancer run.bat (expérimenter)
         ↓
4️⃣ EXEMPLE_CALCUL.md (comprendre en détail)
         ↓
5️⃣ FORMULES.md (fondements mathématiques)
         ↓
6️⃣ CONSEILS.md (bonnes pratiques)
         ↓
7️⃣ Utiliser l'application régulièrement
```

### Pour utiliser l'application

```
1️⃣ DEMARRAGE.md (guide rapide)
         ↓
2️⃣ run.bat (lancer)
         ↓
3️⃣ Module 1 (paramétrage)
         ↓
4️⃣ Module 2 (répartition primaire)
         ↓
5️⃣ Module 3 (répartition secondaire)
         ↓
6️⃣ Module 4 (coûts d'UO)
         ↓
7️⃣ Module 5 (fiche commande)
         ↓
8️⃣ Module 6 (devis et résultat)
```

### Pour dépanner

```
Problème à l'installation?
  └─ DEMARRAGE.md → Section "Dépannage"
  
Calcul incorrect?
  └─ EXEMPLE_CALCUL.md → Valider étape par étape
  
Marge suspecte?
  └─ CONSEILS.md → Section "Interprétation des résultats"
  
Formula mathématique?
  └─ FORMULES.md → Détails complets
```

---

## 📋 LES 6 MODULES EXPLIQUÉS

### 🔧 Module 1 - Paramétrage des charges
- **Fichier:** [`app.py`](app.py) (lignes 70-130)
- **Documentation:** [`DEMARRAGE.md`](DEMARRAGE.md#module-1--paramétrage-des-charges) + [`README.md`](README.md#module-1---paramétrage-des-charges)
- **Formules:** [`FORMULES.md`](FORMULES.md#étape-1-distinction-des-charges)
- **Exemple:** [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md#étape-1-répartition-primaire)

### 📊 Module 2 - Répartition primaire
- **Fichier:** [`app.py`](app.py) (lignes 131-180)
- **Documentation:** [`DEMARRAGE.md`](DEMARRAGE.md#module-2--répartition-primaire) + [`README.md`](README.md#module-2---répartition-primaire)
- **Formules:** [`FORMULES.md`](FORMULES.md#étape-2-répartition-primaire)
- **Exemple:** [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md#étape-1-répartition-primaire)

### 🔄 Module 3 - Répartition secondaire
- **Fichier:** [`app.py`](app.py) (lignes 181-250)
- **Documentation:** [`DEMARRAGE.md`](DEMARRAGE.md#module-3--répartition-secondaire) + [`README.md`](README.md#module-3---répartition-secondaire)
- **Formules:** [`FORMULES.md`](FORMULES.md#étape-3-répartition-secondaire)
- **Exemple:** [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md#étape-2-répartition-secondaire)

### 📈 Module 4 - Coûts d'UO
- **Fichier:** [`app.py`](app.py) (lignes 251-320)
- **Documentation:** [`DEMARRAGE.md`](DEMARRAGE.md#module-4--calcul-des-coûts-duo) + [`README.md`](README.md#module-4---calcul-des-coûts-duo)
- **Formules:** [`FORMULES.md`](FORMULES.md#étape-4-coût-de-lunité-dœuvre-cuo)
- **Exemple:** [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md#étape-3-calcul-des-coûts-dunité-dœuvre)

### 🛒 Module 5 - Fiche de la commande
- **Fichier:** [`app.py`](app.py) (lignes 321-410)
- **Documentation:** [`DEMARRAGE.md`](DEMARRAGE.md#module-5--fiche-de-la-commande) + [`README.md`](README.md#module-5---fiche-de-la-commande)
- **Formules:** [`FORMULES.md`](FORMULES.md#étape-5-imputation-à-la-commande)
- **Exemple:** [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md#étape-6-imputation-des-frais-indirects-à-la-commande)

### 💰 Module 6 - Aide à la décision
- **Fichier:** [`app.py`](app.py) (lignes 411-520)
- **Documentation:** [`DEMARRAGE.md`](DEMARRAGE.md#module-6--aide-à-la-décision-devis) + [`README.md`](README.md#module-6---aide-à-la-décision)
- **Formules:** [`FORMULES.md`](FORMULES.md#étape-7-devis-avec-marge)
- **Exemple:** [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md#étape-8-devis-avec-marge)

---

## 🎓 VOCABULAIRE CLÉS

### Charges
- **Charges directes:** Affectables directement au produit (aluminium, MOD)
- **Charges indirectes:** Partagées entre plusieurs productions (loyer, électricité)
- **Charges incorporables:** Incluses dans le coût de production (toutes sauf exceptionnelles)

### Centres
- **Centres auxiliaires:** Soutiennent les opérations (ADM, ENT)
- **Centres principaux:** Générent la production (APPRO, AT-D, AT-ML, DIST)

### Coûts
- **CUO (Coût de l'Unité d'Œuvre):** Coût par unité dans un centre
- **Prix de revient:** Coût total de production
- **Frais indirects imputés:** Part des FI allouée au produit
- **Résultat analytique:** Profit = PV - PR

### Marges
- **Marge bénéficiaire:** Différence entre PV et PR
- **Taux de marge:** Marge ÷ PV × 100%
- **Coefficient:** PV ÷ PR

---

## 🔗 LIENS RAPIDES

### Installation
- Windows: Lisez [`DEMARRAGE.md`](DEMARRAGE.md#installation-première-utilisation)
- Linux/Mac: Lisez [`README.md`](README.md#installation-et-utilisation)

### Utilisation
- Guide complet: [`README.md`](README.md)
- Démarrage rapide: [`DEMARRAGE.md`](DEMARRAGE.md)
- Guide pas à pas: [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md)

### Référence technique
- Formules: [`FORMULES.md`](FORMULES.md)
- Bonnes pratiques: [`CONSEILS.md`](CONSEILS.md)
- Vue d'ensemble: [`RESUME.md`](RESUME.md)

---

## 📊 DONNÉES ELCO-BAT SARL

**Fichier source:** [`data_elcobat.json`](data_elcobat.json)

**Charges indirectes totales:** 792,000 DA

**Résultat exemple (120 ensembles):**
- Prix de revient: 1,226,739 DA
- Avec 20% marge: 1,472,087 DA
- Résultat analytique: 245,348 DA

---

## ✅ VÉRIFIER VOTRE COMPRÉHENSION

Posez-vous ces questions:

- [ ] Pouvez-vous expliquer la différence charges directes/indirectes?
- [ ] Savez-vous ce qu'est une clé de répartition?
- [ ] Comprenez-vous le rôle des centres auxiliaires?
- [ ] Connaissez-vous la formule CUO?
- [ ] Pouvez-vous calculer un prix de revient manuellement?
- [ ] Savez-vous interpréter un résultat analytique?
- [ ] Connaissez-vous les marges recommandées?
- [ ] Pouvez-vous utiliser l'outil pour générer 3 devis?

**Si vous avez répondu "oui" à 6+, vous maîtrisez le sujet! 🎓**

---

## 🚀 PROCHAINES ÉTAPES

1. **Démarrez l'application:** [`DEMARRAGE.md`](DEMARRAGE.md)
2. **Explorez chaque module:** 6 modules à expérimenter
3. **Générez des devis:** Module 6 - essayez différentes marges
4. **Comprenez les formules:** [`FORMULES.md`](FORMULES.md)
5. **Appliquez à vos données:** Importez dans `app.py`

---

## 📞 SUPPORT

| Question | Réponse |
|----------|--------|
| Où lancer l'app? | Double-cliquez `run.bat` |
| Erreur Python? | Lisez [`DEMARRAGE.md#dépannage`](DEMARRAGE.md#-dépannage) |
| Comprendre par étapes? | Consultez [`EXEMPLE_CALCUL.md`](EXEMPLE_CALCUL.md) |
| Formule mathématique? | Voir [`FORMULES.md`](FORMULES.md) |
| Bonne pratique? | Lire [`CONSEILS.md`](CONSEILS.md) |
| Vue complète du projet? | Voir [`README.md`](README.md) |

---

## 🎯 RÉSUMÉ EN UNE PHRASE

**Utilisez cet outil pour calculer précisément le prix de revient d'une commande industrielle par la méthode des sections homogènes, générer des devis compétitifs, et prendre des décisions tarifaires éclairées.**

---

**Bonne utilisation! 🚀 Commencez par [`DEMARRAGE.md`](DEMARRAGE.md)**
