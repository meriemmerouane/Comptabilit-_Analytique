# TABLEAU DE BORD ELCO-BAT - Guide des Nouvelles Fonctionnalités

## Vue d'Ensemble

L'application ELCO-BAT a été enrichie de deux fonctionnalités majeures :

1. **Système d'Historisation des Commandes**
2. **KPI Résultat - Tableau de Bord Analytique**

---

## 1. KPI "RÉSULTAT" - La Clé de la Rentabilité

### Qu'est-ce que le Résultat?

**Résultat = Prix de Vente - Coût de Revient**

C'est la **différence entre ce que vous facturez au client et ce que la commande vous coûte réellement**.

### Où le voir?

- **Module Devis** : KPI "Résultat" affiché en bas du calcul
- **Tableau de Bord** : Toutes les analyses portent sur ce KPI

### Exemple
```
Coût de revient : 100,000 DA
Prix de vente : 125,000 DA
─────────────────────────
Résultat : 25,000 DA

Cela signifie que vous gagnez 25,000 DA sur cette commande
```

### Interprétation

| Résultat | Signification | Action |
|----------|---------------|--------|
| Positif | Vous gagnez de l'argent | Bon! Valider la commande |
| Zéro | Vous couvrez juste les coûts | Trop juste, augmenter le prix |
| Négatif | Vous perdez de l'argent | REFUSER cette commande! |

---

## 2. SYSTÈME D'HISTORISATION

### Comment Enregistrer une Commande?

1. **Créez un Devis** via le module "Devis"
2. **Remplissez tous les paramètres** (charges, marges, client)
3. **Cliquez sur le bouton** "Enregistrer et Historiser cette Commande"
4. La commande est sauvegardée automatiquement en JSON

### Données Enregistrées

Chaque commande sauvegarde:
- **Informations client** (nom, adresse, email, téléphone)
- **Finances** (coûts, prix, marge, **résultat**)
- **Opérationnel** (consommation par centre, capacités résiduelles)
- **Métadonnées** (date, numéro de devis, statut)

---

## 3. TABLEAU DE BORD - Analyses Complètes

Le nouveau module **"Tableau de Bord"** offre 4 onglets:

### Onglet 1: KPIs Globaux

Affiche les indicateurs clés agrégés de toutes vos commandes:

- **Nombre de Devis** : Combien de devis ont-vous créés?
- **Résultat Total** : Combien gagnez-vous globalement?
- **Résultat Moyen** : Rentabilité moyenne par commande
- **CA Total** : Chiffre d'affaires total
- **Coût Total** : Total des coûts
- **Marge Moyenne** : Votre marge moyenne en %
- **Coefficient Moyen** : Multiplicateur moyen prix/coût
- **Meilleur/Pire Résultat** : Min/Max pour repérer les anomalies

### Onglet 2: Historique des Commandes

Table complète de toutes vos commandes avec:
- Numéro devis
- Date
- Client
- Prix revient & vente
- Résultat obtenu
- Statut

**Actions disponibles:**
- Exporter en CSV pour Excel/Sheets
- Réinitialiser (attention: irréversible!)

### Onglet 3: Analyses Temporelles

Visualise l'évolution de vos KPIs:

1. **Cumul du Résultat** (courbe) : Voir votre profit croître dans le temps
2. **Résultat par Commande** (bar chart) : Identifier les commandes problématiques
3. **Tableau chronologique** : Détail jour par jour

Utilité: **Voir si votre rentabilité s'améliore avec le temps**

### Onglet 4: Analyse par Client

Groupe vos commandes par client:
- Nombre de commandes par client
- Résultat total et moyen par client
- CA total
- Graphiques de distribution

Utilité: **Identifier vos meilleurs clients et les relations non rentables**

---

## 4. EXEMPLE DE WORKFLOW

### Scenario: Vous recevez 3 demandes de devis

#### Étape 1: Calculer les 3 devis

1. **Devis Client A** 
   - Coût revient: 150,000 DA
   - Prix vente: 180,000 DA
   - **Résultat: 30,000 DA**
   - → Enregistrer

2. **Devis Client B**
   - Coût revient: 100,000 DA
   - Prix vente: 105,000 DA
   - **Résultat: 5,000 DA** Trop faible!
   - → Augmenter le prix ou refuser

3. **Devis Client C**
   - Coût revient: 80,000 DA
   - Prix vente: 85,000 DA
   - **Résultat: 5,000 DA**
   - → Refuser (utilisation capacité trop importante)

#### Étape 2: Consulter le Tableau de Bord

- **KPIs Globaux**: Voir que vous avez gagné 30,000 DA
- **Historique**: Tableau de 1 seule commande acceptée
- **Analyses**: Confirmez votre stratégie

---

## 5. CAS D'USAGE PRATIQUES

### Cas 1: Améliorer la Rentabilité
**Question**: "Pourquoi mes devis du mois A sont moins rentables?"

**Solution**:
1. Allez au Tableau de Bord → Analyses Temporelles
2. Voyez le "Cumul du Résultat" s'aplatir en mois A
3. Vérifiez l'onglet "Résultat par Commande"
4. Identifiez les commandes problématiques
5. Rengociez les prix ou les coûts

### Cas 2: Gérer la Capacité
**Question**: "Je peux accepter cette commande?"

**Solution**:
1. Calculez le devis (cela montre l'utilisation des ressources)
2. Le module Devis vous montre: "Taux d'utilisation moyen: X%"
3. Si < 80%, vous avez de la capacité
4. Si > 90%, attention à la surcharge!

### Cas 3: Analyser les Clients
**Question**: "Quel est mon meilleur client?"

**Solution**:
1. Tableau de Bord → Analyse par Client
2. Colonne "Résultat Total (DA)" en ordre décroissant
3. Voyez qui vous apporte le plus de profit

---

## 6. FICHIER D'HISTORIQUE

Les données sont sauvegardées dans: **`commandes_historique.json`**

Format JSON:
```json
{
  "id": 1,
  "numero_devis": "DEVIS-20240422-0001",
  "date_creation": "2024-04-22T10:30:00",
  "client": {
    "nom": "Entreprise XYZ",
    "adresse": "123 Rue de la Paix",
    "telephone": "+213 21 23 45 67",
    "email": "contact@xyz.com"
  },
  "finances": {
    "charges_directes": {...},
    "frais_indirects": 45000,
    "prix_revient": 150000,
    "prix_vente": 180000,
    "marge_montant": 30000,
    "resultat": 30000,
    "coefficient": 1.2
  },
  "operationnel": {
    "consommation_par_centre": {...},
    "capacites_residuelles": {...}
  },
  "statut": "Créée"
}
```

---

## 7. FORMULES UTILISÉES

### Résultat
```
Résultat = Prix de Vente - Coût de Revient
```

### Marge
```
Marge (%) = (Prix de Vente - Coût de Revient) / Coût de Revient × 100
```

### Taux de Marque
```
Taux de Marque (%) = Résultat / Prix de Vente × 100
```

### Coefficient
```
Coefficient = Prix de Vente / Coût de Revient
```

---

## FAQ

**Q: Pourquoi le résultat est négatif?**
R: Votre prix de vente est inférieur au coût. Il faut augmenter le prix ou refuser.

**Q: Où vont les données d'historique?**
R: Fichier `commandes_historique.json` dans le dossier de l'app.

**Q: Puis-je supprimer une commande?**
R: Oui, mais c'est manuel. Vous pouvez réinitialiser tout l'historique (onglet 2).

**Q: Les données sont-elles sauvegardées automatiquement?**
R: Oui, quand vous cliquez sur "Enregistrer et Historiser".

**Q: Puis-je exporter les données?**
R: Oui, en CSV pour utiliser dans Excel/Sheets.

---

## Prochaines Améliorations Suggérées

- Sauvegarde en base de données (au lieu de JSON)
- Alertes si capacité > 90%
- Prédictions de rentabilité par client
- Graphiques avancés (Pareto, box plots)
- Export PDF du tableau de bord

---

**Version 2.0 - Avril 2024**
**Auteur**: ELCO-BAT SARL
