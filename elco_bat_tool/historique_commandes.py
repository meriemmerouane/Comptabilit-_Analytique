import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd

# Chemin du fichier historique
HISTORIQUE_FILE = "commandes_historique.json"

def charger_historique() -> List[Dict]:
    """Charge l'historique des commandes depuis le fichier JSON"""
    if os.path.exists(HISTORIQUE_FILE):
        try:
            with open(HISTORIQUE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def sauvegarder_historique(commandes: List[Dict]) -> bool:
    """Sauvegarde l'historique des commandes dans le fichier JSON"""
    try:
        with open(HISTORIQUE_FILE, 'w', encoding='utf-8') as f:
            json.dump(commandes, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False

def ajouter_commande(
    client_nom: str,
    client_adresse: str,
    client_telephone: str,
    client_email: str,
    prix_revient: float,
    prix_vente: float,
    marge_montant: float,
    marge_pct: float,
    taux_marge: float,
    resultat: float,
    charges_directes: Dict,
    frais_indirects: float,
    consommation: Dict,
    capacites_residuelles: Dict,
    numero_devis: str = None
) -> Dict:
    """
    Ajoute une nouvelle commande à l'historique
    
    Retourne le dictionnaire de la commande ajoutée
    """
    
    commandes = charger_historique()
    
    # Générer un numéro unique s'il n'est pas fourni
    if not numero_devis:
        numero_devis = f"DEVIS-{datetime.now().strftime('%Y%m%d')}-{len(commandes)+1:04d}"
    
    nouvelle_commande = {
        'id': len(commandes) + 1,
        'numero_devis': numero_devis,
        'date_creation': datetime.now().isoformat(),
        'client': {
            'nom': client_nom,
            'adresse': client_adresse,
            'telephone': client_telephone,
            'email': client_email
        },
        'finances': {
            'charges_directes': charges_directes,
            'frais_indirects': frais_indirects,
            'prix_revient': prix_revient,
            'prix_vente': prix_vente,
            'marge_montant': marge_montant,
            'marge_pct': marge_pct,
            'taux_marge_marque': taux_marge,
            'resultat': resultat,  # KPI PRINCIPAL: Prix de vente - Coût de revient
            'coefficient': prix_vente / prix_revient if prix_revient > 0 else 0
        },
        'operationnel': {
            'consommation_par_centre': consommation,
            'capacites_residuelles': capacites_residuelles
        },
        'statut': 'Créée'
    }
    
    commandes.append(nouvelle_commande)
    sauvegarder_historique(commandes)
    
    return nouvelle_commande

def obtenir_commande(id_commande: int) -> Optional[Dict]:
    """Récupère une commande par son ID"""
    commandes = charger_historique()
    for cmd in commandes:
        if cmd['id'] == id_commande:
            return cmd
    return None

def supprimer_commande(id_commande: int) -> bool:
    """Supprime une commande de l'historique"""
    commandes = charger_historique()
    commandes = [cmd for cmd in commandes if cmd['id'] != id_commande]
    return sauvegarder_historique(commandes)

def obtenir_df_historique() -> pd.DataFrame:
    """Retourne un DataFrame avec l'historique pour affichage"""
    commandes = charger_historique()
    
    if not commandes:
        return pd.DataFrame()
    
    data = []
    for cmd in commandes:
        data.append({
            'ID': cmd['id'],
            'Numéro Devis': cmd['numero_devis'],
            'Date': cmd['date_creation'][:10],
            'Client': cmd['client']['nom'],
            'Prix Revient (DA)': cmd['finances']['prix_revient'],
            'Prix Vente (DA)': cmd['finances']['prix_vente'],
            'Marge (DA)': cmd['finances']['marge_montant'],
            'Marge %': f"{cmd['finances']['marge_pct']:.1f}%",
            'Résultat (DA)': cmd['finances']['resultat'],
            'Coefficient': f"{cmd['finances']['coefficient']:.2f}x",
            'Statut': cmd['statut']
        })
    
    return pd.DataFrame(data)

def calculer_kpis() -> Dict:
    """Calcule les KPIs globaux à partir de l'historique"""
    commandes = charger_historique()
    
    if not commandes:
        return {
            'nombre_devis': 0,
            'resultat_total': 0,
            'resultat_moyen': 0,
            'prix_vente_total': 0,
            'prix_revient_total': 0,
            'marge_moyenne': 0,
            'coefficient_moyen': 0,
            'taux_marge_moyen': 0,
            'meilleur_resultat': 0,
            'pire_resultat': 0
        }
    
    resultats = [cmd['finances']['resultat'] for cmd in commandes]
    prix_ventes = [cmd['finances']['prix_vente'] for cmd in commandes]
    prix_revenus = [cmd['finances']['prix_revient'] for cmd in commandes]
    marges = [cmd['finances']['marge_pct'] for cmd in commandes]
    coefficients = [cmd['finances']['coefficient'] for cmd in commandes]
    taux_marques = [cmd['finances']['taux_marge_marque'] for cmd in commandes]
    
    return {
        'nombre_devis': len(commandes),
        'resultat_total': sum(resultats),
        'resultat_moyen': sum(resultats) / len(resultats) if resultats else 0,
        'prix_vente_total': sum(prix_ventes),
        'prix_revient_total': sum(prix_revenus),
        'marge_moyenne': sum(marges) / len(marges) if marges else 0,
        'coefficient_moyen': sum(coefficients) / len(coefficients) if coefficients else 0,
        'taux_marge_moyen': sum(taux_marques) / len(taux_marques) if taux_marques else 0,
        'meilleur_resultat': max(resultats) if resultats else 0,
        'pire_resultat': min(resultats) if resultats else 0,
        'resultat_max_client': max([c['client']['nom'] for c in commandes], 
                                   key=lambda x: next(cmd['finances']['resultat'] for cmd in commandes if cmd['client']['nom'] == x),
                                   default='N/A') if commandes else 'N/A'
    }

def obtenir_analyse_clients() -> pd.DataFrame:
    """Retourne une analyse groupée par client"""
    commandes = charger_historique()
    
    if not commandes:
        return pd.DataFrame()
    
    clients_data = {}
    for cmd in commandes:
        client_nom = cmd['client']['nom']
        if client_nom not in clients_data:
            clients_data[client_nom] = {
                'nombre_commandes': 0,
                'resultat_total': 0,
                'resultat_moyen': 0,
                'prix_vente_total': 0,
                'prix_revient_total': 0,
                'marge_moyenne': 0
            }
        
        clients_data[client_nom]['nombre_commandes'] += 1
        clients_data[client_nom]['resultat_total'] += cmd['finances']['resultat']
        clients_data[client_nom]['prix_vente_total'] += cmd['finances']['prix_vente']
        clients_data[client_nom]['prix_revient_total'] += cmd['finances']['prix_revient']
        clients_data[client_nom]['marge_moyenne'] = (
            (clients_data[client_nom]['prix_vente_total'] - 
             clients_data[client_nom]['prix_revient_total']) / 
            clients_data[client_nom]['nombre_commandes']
        )
    
    # Calculer les moyennes
    for client in clients_data:
        clients_data[client]['resultat_moyen'] = (
            clients_data[client]['resultat_total'] / 
            clients_data[client]['nombre_commandes']
        )
    
    data_list = []
    for client_nom, stats in clients_data.items():
        data_list.append({
            'Client': client_nom,
            'Nb Commandes': stats['nombre_commandes'],
            'Résultat Total (DA)': stats['resultat_total'],
            'Résultat Moyen (DA)': stats['resultat_moyen'],
            'Marge Moyenne (DA)': stats['marge_moyenne'],
            'CA Total (DA)': stats['prix_vente_total']
        })
    
    return pd.DataFrame(data_list).sort_values('Résultat Total (DA)', ascending=False)

def obtenir_evolution_temporelle() -> pd.DataFrame:
    """Retourne l'évolution des KPIs dans le temps"""
    commandes = charger_historique()
    
    if not commandes:
        return pd.DataFrame()
    
    # Trier par date
    commandes_triees = sorted(commandes, key=lambda x: x['date_creation'])
    
    data = []
    cumul_resultat = 0
    cumul_prix_vente = 0
    cumul_prix_revient = 0
    
    for cmd in commandes_triees:
        cumul_resultat += cmd['finances']['resultat']
        cumul_prix_vente += cmd['finances']['prix_vente']
        cumul_prix_revient += cmd['finances']['prix_revient']
        
        data.append({
            'Date': cmd['date_creation'][:10],
            'Client': cmd['client']['nom'],
            'Résultat': cmd['finances']['resultat'],
            'Cumul Résultat': cumul_resultat,
            'Prix Vente': cmd['finances']['prix_vente'],
            'Prix Revient': cmd['finances']['prix_revient'],
            'Coefficient': cmd['finances']['coefficient']
        })
    
    return pd.DataFrame(data)

def exporter_csv(nom_fichier: str = None) -> str:
    """Exporte l'historique en CSV"""
    if not nom_fichier:
        nom_fichier = f"historique_commandes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    df = obtenir_df_historique()
    
    if df.empty:
        return None
    
    df.to_csv(nom_fichier, index=False, encoding='utf-8')
    return nom_fichier

def reinitialiser_historique():
    """Réinitialise l'historique (ATTENTION: action irréversible)"""
    return sauvegarder_historique([])
