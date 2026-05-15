## 💾 Données PROTECTEX par défaut

### Charges indirectes (total: 792,000 DA)
```
Loyer                     180,000 DA
Électricité / énergie       96,000 DA
Entretien matériels         72,000 DA
Salaires personnel indirect 240,000 DA
Amortissement machines     120,000 DA
Fournitures administratives 24,000 DA
Transport / livraison       60,000 DA
```

### Centres d'analyse
```
AUXILIAIRES:
   • ADM (Administration)
   • ENT (Entretien)

PRINCIPAUX:
   • APPRO (Approvisionnement tissus/fournitures)
   • AT-D (Atelier Coupe)
   • AT-ML (Atelier Couture/Assemblage)
   • DIST (Distribution / Finition)
```

### Unités d'œuvre (du mois)
```
APPRO   → 12,000 mètres (tissus/fournitures)
AT-D    → 7,200 mètres coupés
AT-ML   → 2,400 heures MOD
DIST    → 1,800 tenues
```

---

## 🎯 Résultats attendus (exemple PROTECTEX)

### Répartition primaire (exemple)
```
ADM:   104,400 DA (charges admin)
ENT:    93,000 DA (entretien)
APPRO:  73,200 DA
AT-D:  207,600 DA
AT-ML: 204,600 DA
DIST:  109,200 DA
```

### Après répartition secondaire (valeurs PROTECTEX attendues)
```
APPRO:  ≈101,724 DA
AT-D:   ≈269,143 DA
AT-ML:  ≈277,401 DA
DIST:   ≈143,732 DA
TOTAL:  792,000 DA ✓
```

### Coûts d'UO (exemple PROTECTEX)
```
APPRO   ≈ 8.48 DA/mètre
AT-D    ≈ 37.38 DA/mètre coupé
AT-ML   ≈ 115.58 DA/h MOD
DIST    ≈ 79.85 DA/tenue
```

### Prix final (exemple PROTECTEX)
```
Charges directes:    1,200,000 DA
Frais indirects imputés: ≈ 254,835 DA
─────────────────────────────
Prix de revient:     ≈ 1,454,835 DA

Avec 20% de marge:     ≈ 290,967 DA
─────────────────────────────
PRIX DE VENTE:       ≈ 1,745,802 DA

Prix unitaire (600 tenues): ≈ 2,910 DA/tenue
```
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

## 💾 Données PROTECTEX EPI par défaut

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

1. Ouvrez `data_protectex_epi.json` (ou `data_elcobat.json` en secours)
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
