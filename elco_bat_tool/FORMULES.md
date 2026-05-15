# 📐 Guide Technique - Formules et Calculs

## Aperçu de la méthode des sections homogènes

La méthode des sections homogènes (ou centres d'analyse) permet de calculer le prix de revient d'une production en répartissant les charges indirectes selon une structure organisée.

## Étapes du calcul

### Étape 1: Distinction des charges

**Charges incorporables:**
- Matières premières
- Main-d'œuvre directe
- Charges d'exploitation générales

**Charges non incorporables:**
- Charges exceptionnelles
- Éléments sans lien direct

**Charges directes:** Affectables directement au produit
**Charges indirectes:** Nécessitent une répartition

### Étape 2: Répartition primaire

$$\text{Charge imputée au centre} = \text{Charge totale} \times \text{Clé de répartition}$$

**Exemple:**
```
Loyer = 180,000 DA
Clé AT-D = 30%
Loyer imputé à AT-D = 180,000 × 0.30 = 54,000 DA
```

### Étape 3: Répartition secondaire

Vidage des centres auxiliaires vers les centres principaux.

$$\text{Montant transféré} = \text{Total du centre auxiliaire} \times \text{Clé secondaire}$$

**Exemple:**
```
ADM total = 104,400 DA
Clé vers AT-D = 25%
Montant transféré = 104,400 × 0.25 = 26,100 DA
```

### Étape 4: Coût de l'unité d'œuvre (CUO)

$$CUO = \frac{\text{Total du centre principal}}{\text{Nombre d'unités d'œuvre}}$$

**Exemple:**
```
Total AT-D = 269,904 DA
Nombre d'heures machine = 1,200
CUO AT-D = 269,904 ÷ 1,200 = 224.92 DA/h
```

### Étape 5: Imputation à la commande

$$\text{Frais imputés} = \text{CUO} \times \text{Consommation de la commande}$$

**Exemple:**
```
CUO AT-D = 224.92 DA/h
Consommation commande = 240 h
Frais imputés = 224.92 × 240 = 53,981 DA
```

### Étape 6: Prix de revient

$$\text{Prix de revient} = \text{Charges directes} + \sum \text{Frais indirects imputés}$$

**Composition (exemple PROTECTEX):**
- Charges directes: 1,200,000 DA
  - Tissu principal: 840,000 DA
  - Fournitures de couture: 72,000 DA
  - Bandes réfléchissantes / renforts: 96,000 DA
  - MOD directe (couture): 192,000 DA

- Frais indirects: ≈254,835 DA
  - APPRO: ≈25,431 DA
  - AT-D: ≈112,144 DA
  - AT-ML: ≈69,350 DA
  - DIST: ≈47,892 DA

**Total: ≈1,454,835 DA**

### Étape 7: Devis avec marge

$$\text{Prix de vente} = \text{Prix de revient} + \text{Marge}$$

$$\text{Marge} = \text{Prix de revient} \times \text{Taux de marge (\%)}$$

**Exemple (marge 20%):**
```
Marge = 1,226,739 × 20% = 245,348 DA
Prix de vente = 1,226,739 + 245,348 = 1,472,087 DA
```

### Étape 8: Résultat analytique

$$\text{Résultat analytique} = \text{Chiffre d'affaires} - \text{Prix de revient}$$

$$\text{Taux de marge} = \frac{\text{Résultat}}{\text{Chiffre d'affaires}} \times 100$$

**Exemple:**
```
CA = 1,472,087 DA
Prix de revient = 1,226,739 DA
Résultat = 1,472,087 - 1,226,739 = 245,348 DA
Taux = 245,348 ÷ 1,472,087 × 100 = 16.66%
```

## Centres d'analyse (PROTECTEX EPI SARL)

### Centres auxiliaires
- **ADM (Administration):** Frais administratifs, gestion
- **ENT (Entretien):** Maintenance, réparation

### Centres principaux
- **APPRO (Approvisionnement):** Achats, stockage
- **AT-D (Atelier Découpe):** Opérations de découpe
- **AT-ML (Atelier Montage):** Assemblage, finitions
- **DIST (Distribution):** Expédition, livraison

## Unités d'œuvre proposées

| Centre | Unité d'œuvre | NUO du mois |
|--------|---------------|------------|
| APPRO | mètres de tissus/fournitures | 12,000 m |
| AT-D | mètres coupés | 7,200 m |
| AT-ML | Heure MOD | 2,400 HMOD |
| DIST | Nombre de tenues | 1,800 tenues |

## Indices de contrôle

### Vérification répartition primaire
```
Somme des charges indirectes = Somme des totaux par centre
792,000 DA = 792,000 DA ✓
```

### Vérification répartition secondaire
```
Total centres principaux = Total charges indirectes
99,204 + 269,904 + 282,468 + 140,424 = 792,000 DA ✓
```

### Vérification imputation
```
Somme des frais imputés = Total du centre
1,800 × 11.81 + 240 × 224.92 + 480 × 117.70 + 120 × 195.03
= 21,258 + 53,981 + 56,496 + 23,404 = 155,139 DA ✓
```

## Formules Excel équivalentes

### Répartition primaire
```excel
=Charge_Totale*Clé_de_répartition
```

### CUO
```excel
=Total_Centre_Principal/NUO
```

### Frais imputés
```excel
=CUO*Consommation_Commande
```

### Prix de revient
```excel
=SOMME(Charges_Directes)+SOMME(Frais_Indirects)
```

### Prix de vente
```excel
=Prix_Revient*(1+Taux_Marge)
```

### Résultat analytique
```excel
=Prix_Vente-Prix_Revient
```

## Cas de sensibilité

### Impact d'une augmentation de 10% des charges

| Paramètre | Avant | Après | Variation |
|-----------|-------|-------|-----------|
| Total charges | 792,000 | 871,200 | +79,200 |
| Prix revient | 1,226,739 | 1,305,939 | +79,200 |
| Prix de vente (20%) | 1,472,087 | 1,567,127 | +95,040 |
| Marge bénéficiaire | 245,348 | 261,188 | +15,840 |

### Impact d'une variation du taux de marge

| Marge (%) | Prix de vente | Résultat |
|-----------|---------------|----------|
| 10% | 1,349,413 | 122,674 |
| 15% | 1,410,851 | 184,112 |
| 20% | 1,472,087 | 245,348 |
| 25% | 1,533,424 | 306,685 |
| 30% | 1,594,761 | 368,022 |

## Utilisation de l'outil

L'application Streamlit automatise tous ces calculs et permet de:
- Modifier en temps réel les paramètres
- Visualiser les impacts immédiatement
- Générer des devis multiples
- Exporter les résultats

---

**Document technique - PROTECTEX EPI SARL**
