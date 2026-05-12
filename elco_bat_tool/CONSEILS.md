# 📚 CONSEILS ET BONNES PRATIQUES

## ✅ Avant de démarrer l'application

### Système requis
- ✅ Windows 7+ / macOS 10.14+ / Linux
- ✅ Python 3.8 ou supérieur (si installation manuelle)
- ✅ Navigateur web moderne (Chrome, Firefox, Edge, Safari)
- ✅ Au moins 100 MB d'espace disque libre

### Installations recommandées
1. **Python 3.10+** (meilleure stabilité)
   - Télécharger: https://www.python.org
   - ⚠️ Cocher "Add Python to PATH" pendant l'installation

2. **Git** (si vous voulez cloner) - optionnel
   - Télécharger: https://git-scm.com

---

## 🎯 Architecture du flux de travail

```
┌─────────────────────────────────────────┐
│ MODULE 1: PARAMÉTRAGE DES CHARGES        │
│ ✓ Charges indirectes (7 éléments)        │
│ ✓ Clés de répartition (confirmées)       │
│ ✓ Charges directes (4 catégories)        │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ MODULE 2: RÉPARTITION PRIMAIRE           │
│ ✓ Tableau charges × centres              │
│ ✓ Totaux par centre                      │
│ ✓ Visualisations OK                      │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ MODULE 3: RÉPARTITION SECONDAIRE         │
│ ✓ Transfert ADM et ENT                   │
│ ✓ Cohérence vérifiée = 792,000 DA        │
│ ✓ Totaux finaux des 4 centres            │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ MODULE 4: CALCUL DES COÛTS D'UO          │
│ ✓ NUO paramétrés (kg, h, ens.)           │
│ ✓ CUO calculés automatiquement           │
│ ✓ Prêt pour imputation                   │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ MODULE 5: FICHE DE LA COMMANDE           │
│ ✓ Charges directes saisies               │
│ ✓ Consommation par centre                │
│ ✓ Prix de revient calculé                │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│ MODULE 6: AIDE À LA DÉCISION             │
│ ✓ Marge ajustée (5% à 50%)               │
│ ✓ Devis généré                           │
│ ✓ Résultat analytique affiché            │
│ ✓ Export en fichier TXT                  │
└─────────────────────────────────────────┘
```

---

## 🔍 Validation des données

### Clés de répartition

> "Les pourcentages doivent totalisent 100% par charge"

**Vérification dans Module 1:**
- Réglage: Les sliders permettent un contrôle fin (0.05 à 1.0)
- Validation: Message ✅ ou ⚠️ en fonction de la somme
- Action: Ajuster jusqu'à 100%

### Toujours vérifier

1. **Module 2 - Répartition primaire:**
   - Total de la ligne charges = 792,000 DA
   - Somme colonnes = 792,000 DA

2. **Module 3 - Répartition secondaire:**
   - Avant vidage = 792,000 DA
   - Après vidage = 792,000 DA
   - Différence: 0 DA (cohérent ✓)

3. **Module 4 - CUO:**
   - Chaque CUO > 0 (sinon: vérifier division)
   - NUO > 0 pour tous les centres

4. **Module 5 - Prix revient:**
   - Charges directes > 0 (sinon: vérifier saisie)
   - Frais indirects > 0 (sinon: vérifier Module 4)

5. **Module 6 - Devis:**
   - Marge choisie entre 5% et 50%
   - Prix de vente > Prix de revient
   - Taux de marge = Résultat ÷ CA × 100

---

## 💡 Conseils d'utilisation

### ✅ À FAIRE

1. **Lisez les graphiques**
   - Pie charts: Distribution relative
   - Barres: Comparaisons absolues
   - Lignes: Tendances

2. **Explorez les scénarios**
   - Marge 15%: Situation prudente
   - Marge 20%: Référence stable
   - Marge 25%: Meilleure couverture
   - Comparez les résultats

3. **Validez chaque étape**
   - Après Module 1: Clés confirmées?
   - Après Module 2: Totaux OK?
   - Après Module 3: Cohérence vérifiée?
   - Après Module 4: CUO réalistes?
   - Après Module 5: PR logique?
   - Après Module 6: Devis compétitif?

4. **Exportez vos résultats**
   - Module 6: Téléchargez le devis
   - Conservez dans vos dossiers
   - Référencez la date et le taux

### ❌ À ÉVITER

1. **Ne sauter pas les modules**
   - Chaque étape dépend de la précédente
   - Module 5 sans Module 4 = erreur
   - Module 6 sans Module 5 = impossible

2. **Ne pas modifier toutes clés à la fois**
   - Changez une charge à la fois
   - Validez chaque modification
   - Notez les changements

3. **Ne pas sous-estimer les frais indirects**
   - Ils représentent 12-13% du PR
   - Leur omission fausse complètement le devis

4. **Ne pas fixer une marge trop basse**
   - < 10%: Risque de perte
   - 10-15%: Marge minimale
   - 15-25%: Recommandé
   - 25+%: Possible sur éléments premium

---

## 🧮 Interprétation des résultats

### Cas 1: PR bas, marge confortable

```
PR:   1,000,000 DA  (80% du PV)
Marg:   250,000 DA  (20% du PV)
PV:   1,250,000 DA  ✅ RECOMMANDÉ
```
**Interprétation:** Production efficace, marge saine

### Cas 2: PR élevé, marge nécessaire

```
PR:   1,226,739 DA  (83% du PV)
Marg:   245,348 DA  (17% du PV)
PV:   1,472,087 DA  ⚠️ À NÉGOCIER
```
**Interprétation:** Coûts à optimiser

### Cas 3: PR très élevé, marge faible

```
PR:   1,150,000 DA  (90% du PV)
Marg:   127,778 DA  (10% du PV)
PV:   1,277,778 DA  ❌ À RÉVISER
```
**Interprétation:** Marche très serrée, non viable

---

## 📊 Ratios à surveiller

| Ratio | Excellent | Bon | Acceptable | Faible |
|-------|-----------|-----|-----------|--------|
| Marge % | > 25% | 20-25% | 15-20% | < 15% |
| CD / PR | < 70% | 70-80% | 80-85% | > 85% |
| FI / PR | 10-15% | 15-20% | 20-25% | > 25% |
| PV / PR | 1.25x+ | 1.20-1.25x | 1.15-1.20x | < 1.15x |

**Où:**
- CD = Charges directes
- FI = Frais indirects
- PR = Prix revient
- PV = Prix de vente

---

## 🔄 Ajustements recommandés

### Si la marge est trop basse (<15%)

**Actions:**
1. ✓ Réduire les charges directes (négocier fournisseurs)
2. ✓ Optimiser les clés de répartition (réduire FI)
3. ✓ Augmenter le prix de vente (si marché permet)
4. ✓ Augmenter les volumes (économies d'échelle)

### Si la marge est trop haute (>30%)

**Actions:**
1. ✓ Réviser pour apprendre (marges géantes = doute)
2. ✓ Étudier la compétition (prix du marché?)
3. ✓ Vérifier les charges omises (frais de vente?)
4. ✓ Considérer une réduction pour volume

---

## 🎓 Concepts clés à comprendre

### Distinction charges/centres

```
Charges (QUOI)
  ├─ Directes (tracé à la commande)
  │   └─ Alum, vitrage, MOD
  └─ Indirectes (partagées)
      └─ Loyer, électricité, salaires

Centres (OÙ)
  ├─ Auxiliaires (supports)
  │   └─ ADM, ENT
  └─ Principaux (productifs)
      └─ APPRO, AT-D, AT-ML, DIST
```

### Unité d'œuvre (COMMENT MESURER)

```
APPRO   → kg (matière)
AT-D    → h (machines)
AT-ML   → h (hommes)
DIST    → ens (produits)
```

### Clés de répartition (COMMENT RÉPARTIR)

```
Clé = Pourcentage de la charge 
      attribué au centre

Exemple:
  Loyer AT-D = 30%
  = L'atelier occupe 30% de la surface
```

---

## 🚀 Cas d'usage avancés

### Cas 1: Commandes variables

**Scénario:** Même commande, quantités différentes

```
APPRO   1,000 kg   →  11.81 DA/kg = 11,810 DA
APPRO   2,000 kg   →  11.81 DA/kg = 23,620 DA
(FI change, CD change, PR change, marge = %)
```

**✓ L'outil recalcule automatiquement**

### Cas 2: Client spécial (marge réduite)

**Scénario:** Client fidèle demande réduction

```
Marge standard      20%  → PV = 1,472,087 DA
Marge négociée     15%  → PV = 1,410,851 DA
Différence         -61,236 DA
```

**✓ Décision transparent grâce aux simulations**

### Cas 3: Optimisation de coûts

**Scénario:** Comment réduire le PR?

```
Modifier clés        → FI réduits
Changer fournisseur  → CD réduits
Améliorer efficacité → CUO baissent
Augmenter volumes    → Économies d'échelle
```

**✓ Testé instantanément dans l'outil**

---

## 📞 Aide-mémoire rapide

### Module 1
- Clés totalisent 100%? ✓
- Charges modifiables? ✓

### Module 2
- Total = 792,000? ✓
- Graphiques clairs? ✓

### Module 3
- Avant = Après? ✓
- 4 centres principaux? ✓

### Module 4
- CUO > 0 tous? ✓
- NUO > 0 tous? ✓

### Module 5
- CD + FI = PR? ✓
- PR = 1,226,739? ✓

### Module 6
- Marge 5-50%? ✓
- Export OK? ✓

---

## 🎯 Objectifs de maîtrise

Après avoir utilisé l'outil, vous devez comprendre:

- [ ] La distinction charges directes/indirectes
- [ ] Comment fonctionnent les clés de répartition
- [ ] Le rôle des centres auxiliaires/principaux
- [ ] Le concept d'unité d'œuvre
- [ ] La formule CUO = Total ÷ NUO
- [ ] L'imputation des coûts à un produit
- [ ] Le calcul du prix de revient
- [ ] La relation marge/prix de vente
- [ ] L'interprétation du résultat analytique
- [ ] La sensibilité aux variations de paramètres

---

## 📞 Contact/Support

Pour toute question:
1. Consultez `README.md` (complet)
2. Lisez `FORMULES.md` (mathématiques)
3. Suivez `EXEMPLE_CALCUL.md` (détails pas à pas)
4. Relancez `DEMARRAGE.md` (démarrage)

---

**Bonne utilisation! 🚀**
