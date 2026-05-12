import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from pdf_generator import creer_pdf_devis
from historique_commandes import (
    ajouter_commande, charger_historique, obtenir_df_historique,
    calculer_kpis, obtenir_analyse_clients, obtenir_evolution_temporelle,
    exporter_csv, obtenir_commande
)

# Configuration de la page
st.set_page_config(
    page_title="ELCO-BAT - Calcul du Prix de Revient",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Professionnel - Comptabilité
st.markdown("""
    <style>
    /* Variables de couleurs professionnelles */
    :root {
        --primary: #1F3A93;
        --secondary: #2A4BA5;
        --accent: #d4a574;
        --success: #2d5016;
        --danger: #8b3a3a;
        --light-bg: #f5f5f5;
        --border: #ddd;
        --kpi-blue: #1F3A93;
        --kpi-green: #27AE60;
        --kpi-orange: #E67E22;
        --kpi-purple: #8E44AD;
        --kpi-red: #C0392B;
    }
    
    /* Police professionnelle */
    * {
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    
    /* Sidebar personnalisée */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1F3A93 0%, #2A4BA5 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: white !important;
    }
    
    [data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"] > * {
        padding: 0 15px;
    }
    
    /* En-tête principal */
    .main-header {
        background: linear-gradient(to right, #1F3A93, #2A4BA5);
        color: white;
        padding: 30px;
        border-radius: 0;
        margin: -35px -40px 30px -40px;
    }
    
    /* Cartes de section */
    .section-card {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* Tableau professionnel */
    .dataframe {
        border-collapse: collapse;
    }
    
    /* Métriques */
    .metric-box {
        background: #f9f9f9;
        border-left: 4px solid #1F3A93;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    
    .metric-blue {
        border-left-color: #1F3A93 !important;
    }
    
    .metric-green {
        border-left-color: #27AE60 !important;
    }
    
    .metric-orange {
        border-left-color: #E67E22 !important;
    }
    
    .metric-purple {
        border-left-color: #8E44AD !important;
    }
    
    .metric-red {
        border-left-color: #C0392B !important;
    }
    
    .metric-label {
        color: #666;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .metric-value {
        color: #1F3A93;
        font-size: 24px;
        font-weight: bold;
    }
    
    /* Boutons */
    button {
        border-radius: 4px;
        border: none;
        padding: 8px 16px;
        font-weight: 600;
    }
    
    /* Onglets */
    .tabs-container {
        border-bottom: 2px solid #ddd;
        margin-bottom: 20px;
    }
    
    /* Validation */
    .validation-success {
        background: #f0f8f0;
        border: 1px solid #2d5016;
        color: #2d5016;
        padding: 12px;
        border-radius: 4px;
        margin: 10px 0;
    }
    
    .validation-error {
        background: #f8f0f0;
        border: 1px solid #8b3a3a;
        color: #8b3a3a;
        padding: 12px;
        border-radius: 4px;
        margin: 10px 0;
    }
    
    /* Tableau de données */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
    }
    
    th {
        background: #f5f5f5;
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
        font-weight: 600;
        color: #1F3A93;
    }
    
    td {
        border: 1px solid #ddd;
        padding: 12px;
    }
    
    tr:hover {
        background: #fafafa;
    }
    </style>
""", unsafe_allow_html=True)

# Initialiser les données en session
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    
    st.session_state.charges_indirectes = {
        'Loyer': 180000,
        'Électricité': 96000,
        'Entretien': 72000,
        'Salaires': 240000,
        'Amortissement': 120000,
        'Fournitures': 24000,
        'Transport': 60000
    }
    
    st.session_state.centres = {
        'ADM': 'Auxiliaire',
        'ENT': 'Auxiliaire',
        'APPRO': 'Principal',
        'AT-D': 'Principal',
        'AT-ML': 'Principal',
        'DIST': 'Principal'
    }
    
    st.session_state.cles_repartition = {
        'Loyer': {'ADM': 0.10, 'ENT': 0.05, 'APPRO': 0.10, 'AT-D': 0.30, 'AT-ML': 0.35, 'DIST': 0.10},
        'Électricité': {'ADM': 0.05, 'ENT': 0.05, 'APPRO': 0.05, 'AT-D': 0.40, 'AT-ML': 0.40, 'DIST': 0.05},
        'Entretien': {'ADM': 0.0, 'ENT': 0.60, 'APPRO': 0.05, 'AT-D': 0.15, 'AT-ML': 0.15, 'DIST': 0.05},
        'Salaires': {'ADM': 0.30, 'ENT': 0.10, 'APPRO': 0.15, 'AT-D': 0.20, 'AT-ML': 0.15, 'DIST': 0.10},
        'Amortissement': {'ADM': 0.0, 'ENT': 0.10, 'APPRO': 0.0, 'AT-D': 0.45, 'AT-ML': 0.45, 'DIST': 0.0},
        'Fournitures': {'ADM': 0.40, 'ENT': 0.0, 'APPRO': 0.20, 'AT-D': 0.10, 'AT-ML': 0.10, 'DIST': 0.20},
        'Transport': {'ADM': 0.0, 'ENT': 0.0, 'APPRO': 0.10, 'AT-D': 0.0, 'AT-ML': 0.0, 'DIST': 0.90}
    }
    
    st.session_state.repart_secondaire = {
        'ADM': {'ENT': 0.10, 'APPRO': 0.15, 'AT-D': 0.25, 'AT-ML': 0.30, 'DIST': 0.20},
        'ENT': {'APPRO': 0.10, 'AT-D': 0.35, 'AT-ML': 0.45, 'DIST': 0.10}
    }
    
    st.session_state.charges_directes = {
        'Aluminium': 756000,
        'Vitrage': 108000,
        'Quincaillerie': 54000,
        'MOD': 153600
    }
    
    st.session_state.unites_oeuvre = {
        'APPRO': 8400,
        'AT-D': 1200,
        'AT-ML': 2400,
        'DIST': 720
    }
    
    st.session_state.consommation_command = {
        'APPRO': 1800,
        'AT-D': 240,
        'AT-ML': 480,
        'DIST': 120
    }
    
    # Informations du client
    st.session_state.client_info = {
        'nom': '',
        'adresse': '',
        'telephone': '',
        'email': '',
        'lieu_livraison': 'Boumerdès'
    }

# En-tête principal
st.markdown("""
<div class="main-header">
    <h1>ELCO-BAT SARL</h1>
    <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">Calcul du Prix de Revient - Méthode des Sections Homogènes</p>
</div>
""", unsafe_allow_html=True)

# Navigation
with st.sidebar:
    st.markdown("---")
    
    module = st.radio(
        "Sélectionner un module:",
        [
            "Paramétrage",
            "Répartition Primaire",
            "Répartition Secondaire",
            "Coûts d'UO",
            "Fiche de Commande",
            "Devis",
            "Tableau de Bord"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 15px; color: white;">
        <strong>ELCO-BAT SARL</strong><br>
        <small>Menuiserie Aluminium</small><br>
        <small>Tizi Ouzou</small>
    </div>
    """, unsafe_allow_html=True)

# ==================== MODULE 1 ====================
if module == "Paramétrage":
    st.title("Paramétrage des Charges")
    
    tab1, tab2, tab3 = st.tabs(["Charges Indirectes", "Clés de Répartition", "Charges Directes"])
    
    with tab1:
        st.subheader("Charges Indirectes Mensuelles")
        
        # Section pour ajouter une nouvelle charge indirecte
        st.markdown("**Ajouter une Charge Indirecte**")
        col_add1, col_add2, col_add3 = st.columns(3)
        
        with col_add1:
            nouvelle_charge_ind = st.text_input("Nom de la charge:", placeholder="Ex: Assurance", key="new_charge_indirect")
        
        with col_add2:
            montant_charge_ind = st.number_input("Montant (DA):", value=0, step=1000, min_value=0, key="amount_charge_indirect")
        
        with col_add3:
            st.write("")
            if st.button("Ajouter", use_container_width=True, key="btn_add_indirect_charge"):
                if nouvelle_charge_ind and montant_charge_ind > 0:
                    if nouvelle_charge_ind not in st.session_state.charges_indirectes:
                        st.session_state.charges_indirectes[nouvelle_charge_ind] = montant_charge_ind
                        
                        # Ajouter aussi les clés de répartition avec des valeurs par défaut
                        centres = list(st.session_state.centres.keys())
                        st.session_state.cles_repartition[nouvelle_charge_ind] = {centre: 1.0/len(centres) for centre in centres}
                        
                        st.success(f"Charge '{nouvelle_charge_ind}' ajoutée")
                    else:
                        st.warning("Cette charge existe déjà!")
                else:
                    st.error("Veuillez remplir tous les champs!")
        
        st.markdown("---")
        
        # Section pour éditer les charges existantes
        st.markdown("**Éditer les Charges Existantes**")
        
        charges_data = {}
        charges_ind_list = list(st.session_state.charges_indirectes.items())
        
        if charges_ind_list:
            for charge, amount in charges_ind_list:
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    charges_data[charge] = st.number_input(
                        f"{charge}",
                        value=amount,
                        step=1000,
                        format="%d",
                        key=f"ci_{charge}",
                        label_visibility="collapsed"
                    )
                
                with col2:
                    st.write(f"{charge}")
        else:
            st.info("Aucune charge indirecte. Ajoutez-en une ci-dessus.")
        
        st.session_state.charges_indirectes = charges_data
        
        # Résumé
        total = sum(charges_data.values())
        cols = st.columns(3)
        
        with cols[0]:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">Nombre de Charges</div>
                <div class="metric-value">{len(charges_data)}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">Montant Total</div>
                <div class="metric-value">{total:,.0f} DA</div>
            </div>
            """, unsafe_allow_html=True)
        
        with cols[2]:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">Moyenne</div>
                <div class="metric-value">{total/len(charges_data):,.0f} DA</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Tableau
        st.markdown("**Récapitulatif des Charges**")
        df_charges = pd.DataFrame({
            'Désignation': charges_data.keys(),
            'Montant (DA)': charges_data.values()
        })
        st.dataframe(df_charges, use_container_width=True)
    
    with tab2:
        st.subheader("Clés de Répartition Primaire")
        
        charge_selected = st.selectbox("Sélectionner une charge:", list(st.session_state.cles_repartition.keys()))
        
        centres_aux = [c for c in st.session_state.centres if st.session_state.centres[c] == 'Auxiliaire']
        centres_prin = [c for c in st.session_state.centres if st.session_state.centres[c] == 'Principal']
        
        cles_updated = st.session_state.cles_repartition[charge_selected].copy()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Centres Auxiliaires**")
            for centre in centres_aux:
                cles_updated[centre] = st.slider(
                    centre,
                    0.0, 1.0,
                    st.session_state.cles_repartition[charge_selected][centre],
                    0.05
                )
        
        with col2:
            st.markdown("**Centres Principaux (1/2)**")
            for centre in centres_prin[:2]:
                cles_updated[centre] = st.slider(
                    centre,
                    0.0, 1.0,
                    st.session_state.cles_repartition[charge_selected][centre],
                    0.05
                )
        
        with col3:
            st.markdown("**Centres Principaux (2/2)**")
            for centre in centres_prin[2:]:
                cles_updated[centre] = st.slider(
                    centre,
                    0.0, 1.0,
                    st.session_state.cles_repartition[charge_selected][centre],
                    0.05
                )
        
        total_cles = sum(cles_updated.values())
        
        if abs(total_cles - 1.0) < 0.001:
            st.markdown(f"""
            <div class="validation-success">
                Total des clés: {total_cles:.1%} ✓
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="validation-error">
                Total des clés: {total_cles:.1%} (doit être 100%)
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state.cles_repartition[charge_selected] = cles_updated
    
    with tab3:
        st.subheader("Charges Directes de la Commande")
        
        # Section pour ajouter une nouvelle charge directe
        st.markdown("**Ajouter une Charge Directe**")
        col_add1, col_add2, col_add3 = st.columns(3)
        
        with col_add1:
            nouvelle_charge_dir = st.text_input("Nom de la charge:", placeholder="Ex: Transport", key="new_charge_direct")
        
        with col_add2:
            montant_charge_dir = st.number_input("Montant (DA):", value=0, step=1000, min_value=0, key="amount_charge_direct")
        
        with col_add3:
            st.write("")
            if st.button("Ajouter", use_container_width=True, key="btn_add_direct_charge"):
                if nouvelle_charge_dir and montant_charge_dir > 0:
                    if nouvelle_charge_dir not in st.session_state.charges_directes:
                        st.session_state.charges_directes[nouvelle_charge_dir] = montant_charge_dir
                        st.success(f"Charge '{nouvelle_charge_dir}' ajoutée")
                    else:
                        st.warning("Cette charge existe déjà!")
                else:
                    st.error("Veuillez remplir tous les champs!")
        
        st.markdown("---")
        
        # Section pour éditer les charges existantes
        st.markdown("**Éditer les Charges Existantes**")
        
        charges_directes = {}
        charges_dir_list = list(st.session_state.charges_directes.items())
        
        if charges_dir_list:
            for charge, amount in charges_dir_list:
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    charges_directes[charge] = st.number_input(
                        f"{charge}",
                        value=amount,
                        step=1000,
                        format="%d",
                        key=f"cd_{charge}",
                        label_visibility="collapsed"
                    )
                
                with col2:
                    st.write(f"{charge}")
        else:
            st.info("Aucune charge directe. Ajoutez-en une ci-dessus.")
        
        st.session_state.charges_directes = charges_directes
        
        total_cd = sum(charges_directes.values())
        st.markdown(f"""
        <div class="metric-box metric-blue">
            <div class="metric-label">Total Charges Directes</div>
            <div class="metric-value">{total_cd:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)

# ==================== MODULE 2 ====================
elif module == "Répartition Primaire":
    st.title("Répartition Primaire des Charges")
    
    centres = list(st.session_state.centres.keys())
    charges = list(st.session_state.charges_indirectes.keys())
    
    repartition_primaire = {}
    for centre in centres:
        repartition_primaire[centre] = 0
        for charge in charges:
            montant = st.session_state.charges_indirectes[charge]
            # Sécurité: vérifier si la charge a des clés de répartition
            if charge not in st.session_state.cles_repartition:
                # Initialiser avec répartition égale par défaut
                st.session_state.cles_repartition[charge] = {centre: 1.0/len(centres) for centre in centres}
            cle = st.session_state.cles_repartition[charge][centre]
            repartition_primaire[centre] += montant * cle
    
    data_repartition = {}
    for charge in charges:
        data_repartition[charge] = {}
        # Sécurité: vérifier si la charge a des clés de répartition
        if charge not in st.session_state.cles_repartition:
            st.session_state.cles_repartition[charge] = {centre: 1.0/len(centres) for centre in centres}
        for centre in centres:
            montant = st.session_state.charges_indirectes[charge]
            cle = st.session_state.cles_repartition[charge][centre]
            data_repartition[charge][centre] = montant * cle
    
    df_repartition = pd.DataFrame(data_repartition).T
    df_repartition['Total'] = df_repartition.sum(axis=1)
    
    st.subheader("Tableau de Répartition Primaire")
    st.dataframe(df_repartition, use_container_width=True)
    
    # Totaux par centre
    st.subheader("Totaux par Centre (avant transfert)")
    
    col1, col2 = st.columns(2)
    
    centres_aux = [c for c in centres if st.session_state.centres[c] == 'Auxiliaire']
    centres_prin = [c for c in centres if st.session_state.centres[c] == 'Principal']
    
    with col1:
        st.markdown("**Centres Auxiliaires**")
        for centre in centres_aux:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">{centre}</div>
                <div class="metric-value">{repartition_primaire[centre]:,.0f} DA</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Centres Principaux**")
        for centre in centres_prin:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">{centre}</div>
                <div class="metric-value">{repartition_primaire[centre]:,.0f} DA</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Graphique
    fig = px.bar(
        x=list(repartition_primaire.keys()),
        y=list(repartition_primaire.values()),
        title="Répartition Primaire par Centre",
        labels={'x': 'Centre', 'y': 'Montant (DA)'}
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.session_state.repartition_primaire = repartition_primaire

# ==================== MODULE 3 ====================
elif module == "Répartition Secondaire":
    st.title("Répartition Secondaire (Vidage des Centres Auxiliaires)")
    
    if 'repartition_primaire' not in st.session_state:
        st.warning("Veuillez d'abord compléter le Module 2")
        st.stop()
    
    repartition_primaire = st.session_state.repartition_primaire.copy()
    repartition_secondaire = repartition_primaire.copy()
    
    centres_aux = [c for c, t in st.session_state.centres.items() if t == 'Auxiliaire']
    centres_prin = [c for c, t in st.session_state.centres.items() if t == 'Principal']
    
    st.subheader("Configuration de la Répartition Secondaire")
    
    repart_sec_updated = {}
    for centre_aux in centres_aux:
        st.markdown(f"**{centre_aux} - Répartition**")
        repart_sec_updated[centre_aux] = {}
        
        col1, col2 = st.columns(2)
        
        with col1:
            for centre_dest in centres_aux:
                if centre_dest != centre_aux:
                    repart_sec_updated[centre_aux][centre_dest] = st.slider(
                        f"{centre_aux} → {centre_dest}",
                        0.0, 1.0,
                        st.session_state.repart_secondaire[centre_aux].get(centre_dest, 0.0),
                        0.05
                    )
        
        with col2:
            for centre_dest in centres_prin:
                repart_sec_updated[centre_aux][centre_dest] = st.slider(
                    f"{centre_aux} → {centre_dest}",
                    0.0, 1.0,
                    st.session_state.repart_secondaire[centre_aux].get(centre_dest, 0.0),
                    0.05
                )
        
        st.markdown("---")
    
    st.session_state.repart_secondaire = repart_sec_updated
    
    # Calcul du vidage
    st.subheader("Vidage des Centres Auxiliaires")
    
    for centre_aux in centres_aux:
        montant_aux = repartition_secondaire[centre_aux]
        with st.expander(f"{centre_aux}: {montant_aux:,.0f} DA"):
            for centre_dest, cle in repart_sec_updated[centre_aux].items():
                montant_transfer = montant_aux * cle
                repartition_secondaire[centre_dest] += montant_transfer
                st.write(f"→ {centre_dest}: {cle:.0%} × {montant_aux:,.0f} = {montant_transfer:,.0f} DA")
        repartition_secondaire[centre_aux] = 0
    
    # Résultats finaux
    st.subheader("Totaux Finaux des Centres Principaux")
    
    col1, col2 = st.columns(2)
    
    with col1:
        for centre in centres_prin:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">{centre}</div>
                <div class="metric-value">{repartition_secondaire[centre]:,.0f} DA</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        total_secondaire = sum([repartition_secondaire[c] for c in centres_prin])
        total_primaire = sum(st.session_state.charges_indirectes.values())
        
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Total Centres Principaux</div>
            <div class="metric-value">{total_secondaire:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
        
        if abs(total_secondaire - total_primaire) < 1:
            st.markdown("""
            <div class="validation-success">
                Cohérence vérifiée ✓
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="validation-error">
                Écart détecté: {total_secondaire - total_primaire:,.0f} DA
            </div>
            """, unsafe_allow_html=True)
    
    st.session_state.repartition_secondaire = repartition_secondaire

# ==================== MODULE 4 ====================
elif module == "Coûts d'UO":
    st.title("Calcul des Coûts d'Unité d'Oeuvre")
    
    if 'repartition_secondaire' not in st.session_state:
        st.warning("Veuillez d'abord compléter le Module 3")
        st.stop()
    
    repartition_secondaire = st.session_state.repartition_secondaire
    centres_prin = [c for c, t in st.session_state.centres.items() if t == 'Principal']
    
    st.info("Saisissez ci-dessous le nombre d'unités d'œuvre pour chaque centre au cours du mois")
    
    st.subheader("Configuration des Unités d'Œuvre")
    
    unites_updated = {}
    col1, col2 = st.columns(2)
    
    for i, centre in enumerate(centres_prin):
        if i % 2 == 0:
            with col1:
                st.markdown(f"**{centre}**")
                unites_updated[centre] = st.number_input(
                    "Nombre d'Unités d'Œuvre (N.U.O)",
                    value=st.session_state.unites_oeuvre[centre],
                    step=1,
                    key=f"nuo_{centre}",
                    label_visibility="collapsed"
                )
        else:
            with col2:
                st.markdown(f"**{centre}**")
                unites_updated[centre] = st.number_input(
                    "Nombre d'Unités d'Œuvre (N.U.O)",
                    value=st.session_state.unites_oeuvre[centre],
                    step=1,
                    key=f"nuo_{centre}",
                    label_visibility="collapsed"
                )
    
    st.session_state.unites_oeuvre = unites_updated
    
    st.markdown("---")
    
    # Calcul des CUO
    st.subheader("Tableau de Répartition Secondaire et Coûts Unitaires d'Œuvre")
    
    cuos = {}
    data_cuos = []
    
    for centre in centres_prin:
        total_centre = repartition_secondaire[centre]
        nuo = unites_updated[centre]
        cuo = total_centre / nuo if nuo > 0 else 0
        cuos[centre] = cuo
        
        data_cuos.append({
            'Centre': centre,
            'Total Répartition Secondaire (DA)': total_centre,
            'Nombre d\'Unités d\'Œuvre': nuo,
            'Coût Unitaire d\'Œuvre (DA/UO)': cuo
        })
    
    df_cuos = pd.DataFrame(data_cuos)
    st.dataframe(df_cuos, use_container_width=True)
    
    # Détail par centre
    st.subheader("Résumé par Centre")
    
    for centre in centres_prin:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">Total {centre}</div>
                <div class="metric-value">{repartition_secondaire[centre]:,.0f} DA</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">NUO {centre}</div>
                <div class="metric-value">{unites_updated[centre]}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">CUO {centre}</div>
                <div class="metric-value">{cuos[centre]:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.session_state.cuos = cuos

# ==================== MODULE 5 ====================
elif module == "Fiche de Commande":
    st.title("Fiche de Commande")
    
    if 'cuos' not in st.session_state:
        st.warning("Veuillez d'abord compléter le Module 4")
        st.stop()
    
    centres_prin = [c for c, t in st.session_state.centres.items() if t == 'Principal']
    
    st.subheader("Charges Directes")
    
    col1, col2 = st.columns(2)
    
    charges_dir_updated = {}
    cd_list = list(st.session_state.charges_directes.keys())
    
    for i, charge in enumerate(cd_list):
        if i % 2 == 0:
            with col1:
                charges_dir_updated[charge] = st.number_input(
                    charge,
                    value=st.session_state.charges_directes[charge],
                    step=1000,
                    format="%d"
                )
        else:
            with col2:
                charges_dir_updated[charge] = st.number_input(
                    charge,
                    value=st.session_state.charges_directes[charge],
                    step=1000,
                    format="%d"
                )
    
    st.session_state.charges_directes = charges_dir_updated
    total_cd = sum(charges_dir_updated.values())
    
    df_cd = pd.DataFrame({
        'Élément': charges_dir_updated.keys(),
        'Montant (DA)': charges_dir_updated.values()
    })
    st.dataframe(df_cd, use_container_width=True)
    
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Total Charges Directes</div>
        <div class="metric-value">{total_cd:,.0f} DA</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Consommation par Centre")
    
    col1, col2 = st.columns(2)
    
    consommation_updated = {}
    cons_list = list(st.session_state.consommation_command.keys())
    
    for i, centre in enumerate(cons_list):
        if i % 2 == 0:
            with col1:
                consommation_updated[centre] = st.number_input(
                    f"{centre} (UO)",
                    value=st.session_state.consommation_command[centre],
                    step=1
                )
        else:
            with col2:
                consommation_updated[centre] = st.number_input(
                    f"{centre} (UO)",
                    value=st.session_state.consommation_command[centre],
                    step=1
                )
    
    st.session_state.consommation_command = consommation_updated
    
    st.subheader("Frais Indirects Imputés")
    
    frais_indirects = {}
    data_frais = []
    
    for centre in centres_prin:
        cons = consommation_updated[centre]
        cuo = st.session_state.cuos[centre]
        frais = cons * cuo
        frais_indirects[centre] = frais
        
        data_frais.append({
            'Centre': centre,
            'Consommation (UO)': cons,
            'CUO (DA/UO)': cuo,
            'Frais (DA)': frais
        })
    
    df_frais = pd.DataFrame(data_frais)
    st.dataframe(df_frais, use_container_width=True)
    
    total_frais = sum(frais_indirects.values())
    
    st.subheader("Prix de Revient")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Charges Directes</div>
            <div class="metric-value">{total_cd:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Frais Indirects</div>
            <div class="metric-value">{total_frais:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        prix_revient = total_cd + total_frais
        st.markdown(f"""
        <div class="metric-box metric-red">
            <div class="metric-label">Prix de Revient</div>
            <div class="metric-value">{prix_revient:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.session_state.prix_revient = prix_revient
    st.session_state.total_frais_indirects = total_frais

# ==================== MODULE 6 ====================
elif module == "Devis":
    st.title("Devis et Aide à la Décision")
    
    if 'prix_revient' not in st.session_state:
        st.warning("Veuillez d'abord compléter le Module 5")
        st.stop()
    
    # Section Informations du Client
    st.subheader("Informations du Client")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.session_state.client_info['nom'] = st.text_input(
            "Nom du Client:",
            value=st.session_state.client_info['nom'],
            placeholder="Ex: Entreprise XYZ"
        )
        st.session_state.client_info['adresse'] = st.text_input(
            "Adresse:",
            value=st.session_state.client_info['adresse'],
            placeholder="Ex: 123 Rue de la Paix"
        )
    
    with col2:
        st.session_state.client_info['telephone'] = st.text_input(
            "Téléphone:",
            value=st.session_state.client_info['telephone'],
            placeholder="Ex: +213 21 23 45 67"
        )
        st.session_state.client_info['email'] = st.text_input(
            "Email:",
            value=st.session_state.client_info['email'],
            placeholder="Ex: contact@entreprise.com"
        )
    
    st.session_state.client_info['lieu_livraison'] = st.text_input(
        "Lieu de Livraison:",
        value=st.session_state.client_info['lieu_livraison']
    )
    
    st.markdown("---")
    
    prix_revient = st.session_state.prix_revient
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-box metric-blue">
            <div class="metric-label">Prix de Revient</div>
            <div class="metric-value">{prix_revient:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        marge_pct = st.slider("Marge Souhaitée (%)", 5, 50, 20, 1)
        st.markdown(f"""
        <div class="metric-box metric-green">
            <div class="metric-label">Taux de Marge (% PR)</div>
            <div class="metric-value">{marge_pct}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        marge_montant = prix_revient * (marge_pct / 100)
        st.markdown(f"""
        <div class="metric-box metric-orange">
            <div class="metric-label">Montant de Marge</div>
            <div class="metric-value">{marge_montant:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    prix_vente = prix_revient + marge_montant
    nb_units = int(st.session_state.consommation_command.get('DIST', 1))
    prix_unitaire = prix_vente / nb_units
    resultat = prix_vente - prix_revient
    taux_marge = (resultat / prix_vente) * 100
    
    st.subheader("Proposition de Devis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-box metric-purple">
            <div class="metric-label">Prix de Vente Total</div>
            <div class="metric-value">{prix_vente:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-box metric-blue">
            <div class="metric-label">Nombre d'Unités</div>
            <div class="metric-value">{nb_units}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-box metric-green">
            <div class="metric-label">Prix Unitaire</div>
            <div class="metric-value">{prix_unitaire:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Résultat Analytique")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-box metric-orange">
            <div class="metric-label">Résultat</div>
            <div class="metric-value">{resultat:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-box metric-red">
            <div class="metric-label">Taux de Marque (% PV)</div>
            <div class="metric-value">{taux_marge:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-box metric-purple">
            <div class="metric-label">CA Prévu</div>
            <div class="metric-value">{prix_vente:,.0f} DA</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-box metric-blue">
            <div class="metric-label">Coefficient</div>
            <div class="metric-value">{prix_vente/prix_revient:.2f}x</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Synthèse Financière")
    
    synthese = {
        'Élément': [
            'Charges directes',
            'Frais indirects',
            'Prix de revient',
            'Marge',
            'Prix de vente',
            'Par unité'
        ],
        'Montant (DA)': [
            sum(st.session_state.charges_directes.values()),
            st.session_state.total_frais_indirects,
            prix_revient,
            marge_montant,
            prix_vente,
            prix_unitaire
        ]
    }
    
    df_synthese = pd.DataFrame(synthese)
    st.dataframe(df_synthese, use_container_width=True)
    
    # Graphiques
    st.subheader("Analyses")
    
    # 1. COURBE DE SENSIBILITÉ
    st.markdown("**Sensibilité - Marge vs Prix de Vente**")
    
    marges = list(range(5, 51, 5))
    prix_marges = [prix_revient * (1 + m/100) for m in marges]
    
    fig_sensibilite = go.Figure()
    fig_sensibilite.add_trace(go.Scatter(x=marges, y=prix_marges, mode='lines+markers', 
                                         name='Prix de vente', line=dict(color='blue', width=3)))
    fig_sensibilite.add_hline(y=prix_revient, line_dash="dash", line_color="red", 
                              annotation_text="Prix de revient", annotation_position="right")
    fig_sensibilite.add_vline(x=marge_pct, line_dash="dash", line_color="green",
                              annotation_text=f"Marge actuelle: {marge_pct:.1f}%", annotation_position="top")
    fig_sensibilite.update_layout(xaxis_title="Taux de Marge (%)", yaxis_title="Prix de Vente (DA)", height=400)
    st.plotly_chart(fig_sensibilite, use_container_width=True)
    
    st.markdown("---")
    
    # 2. TAUX D'UTILISATION CAPACITÉ
    st.markdown("**Taux d'Utilisation - Ressources Disponibles**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        centres = ['APPRO', 'AT-D', 'AT-ML', 'DIST']
        capacites = [8400, 1200, 2400, 720]
        consommations = [
            st.session_state.consommation_command.get('APPRO', 0),
            st.session_state.consommation_command.get('AT-D', 0),
            st.session_state.consommation_command.get('AT-ML', 0),
            st.session_state.consommation_command.get('DIST', 0)
        ]
        disponibles = [cap - c for cap, c in zip(capacites, consommations)]
        
        fig_util = go.Figure(data=[
            go.Bar(name='Utilisé', x=centres, y=consommations, marker_color='lightblue'),
            go.Bar(name='Disponible', x=centres, y=disponibles, marker_color='lightgray')
        ])
        fig_util.update_layout(barmode='stack', xaxis_title="Centre", yaxis_title="Unités", height=400)
        st.plotly_chart(fig_util, use_container_width=True)
    
    with col2:
        taux_util = [(c/cap)*100 for c, cap in zip(consommations, capacites)]
        df_capacite = pd.DataFrame({
            'Centre': centres,
            'Capacité': capacites,
            'Consommation': consommations,
            'Taux utilisé (%)': [f"{t:.1f}%" for t in taux_util],
            'Disponible': disponibles
        })
        st.dataframe(df_capacite, use_container_width=True)
        
        taux_moyen = sum(taux_util) / len(taux_util)
        st.success(f"""
        **Synthèse:**
        - Taux d'utilisation moyen: {taux_moyen:.1f}%
        - Capacité disponible: {100-taux_moyen:.1f}%
        - Conclusion: L'entreprise peut accepter d'autres commandes
        """)
    
    st.markdown("---")
    
    # 3. COMPOSITION DU PRIX DE REVIENT
    st.markdown("**Composition du Prix de Revient**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        labels_donut = list(st.session_state.charges_directes.keys()) + ["Frais indirects"]
        sizes_donut = list(st.session_state.charges_directes.values()) + [st.session_state.total_frais_indirects]
        pct_donut = [s/prix_revient*100 for s in sizes_donut]
        
        fig_donut = go.Figure(data=[go.Pie(
            labels=[f"{l} ({p:.1f}%)" for l, p in zip(labels_donut, pct_donut)],
            values=sizes_donut,
            hole=0.3,
            marker=dict(colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
        )])
        st.plotly_chart(fig_donut, use_container_width=True)
    
    with col2:
        df_composition = pd.DataFrame({
            'Élément': labels_donut,
            'Montant (DA)': sizes_donut,
            '% du PR': [f"{p:.1f}%" for p in pct_donut]
        })
        st.dataframe(df_composition, use_container_width=True)
        
        max_idx = pct_donut.index(max(pct_donut))
        max_item = labels_donut[max_idx]
        max_pct = pct_donut[max_idx]
        
        st.warning(f"""
        **Synthèse:**
        - Poste dominant: {max_item} ({max_pct:.1f}%)
        - Priorité de négociation: {max_item}
        - Impact potentiel: Réduction directe du prix de revient
        """)
    
    st.subheader("Téléchargement du Devis")
    
    # Préparer les données pour le PDF
    donnees_devis = {
        'numero_devis': f"DEVIS-2024-{int(datetime.now().timestamp()) % 10000:04d}",
        'date': datetime.now().strftime('%d/%m/%Y'),
        'client': st.session_state.client_info['nom'] if st.session_state.client_info['nom'] else 'Client Non Renseigné',
        'adresse': st.session_state.client_info['adresse'],
        'telephone': st.session_state.client_info['telephone'],
        'email': st.session_state.client_info['email'],
        'lieu_livraison': st.session_state.client_info['lieu_livraison'],
        'charges_directes': st.session_state.charges_directes,
        'frais_indirects': st.session_state.total_frais_indirects,
        'prix_revient': prix_revient,
        'prix_vente': prix_vente,
        'marge': marge_montant,
        'taux_marge': taux_marge,
        'prix_unitaire': prix_unitaire,
        'quantite': 120,
        'resultat': resultat
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            pdf_bytes = creer_pdf_devis(donnees_devis)
            st.download_button(
                "Telecharger Devis (PDF)",
                pdf_bytes,
                f"Devis_ELCOBAT_{datetime.now().strftime('%Y%m%d')}.pdf",
                "application/pdf",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Erreur de génération PDF: {str(e)}")
    
    with col2:
        if st.button("Enregistrer et Historiser cette Commande", use_container_width=True, key="btn_save_command"):
            # Calcul des capacités résiduelles pour chaque centre
            capacites_residuelles = {}
            capacites = {'APPRO': 8400, 'AT-D': 1200, 'AT-ML': 2400, 'DIST': 720}
            
            for centre in capacites:
                cons = st.session_state.consommation_command.get(centre, 0)
                capacites_residuelles[centre] = capacites[centre] - cons
            
            # Ajouter à l'historique
            nouvelle_cmd = ajouter_commande(
                client_nom=st.session_state.client_info['nom'] or 'Client Non Renseigné',
                client_adresse=st.session_state.client_info['adresse'],
                client_telephone=st.session_state.client_info['telephone'],
                client_email=st.session_state.client_info['email'],
                prix_revient=prix_revient,
                prix_vente=prix_vente,
                marge_montant=marge_montant,
                marge_pct=marge_pct,
                taux_marge=taux_marge,
                resultat=resultat,
                charges_directes=st.session_state.charges_directes,
                frais_indirects=st.session_state.total_frais_indirects,
                consommation=st.session_state.consommation_command,
                capacites_residuelles=capacites_residuelles,
                numero_devis=donnees_devis['numero_devis']
            )
            
            st.success(f"Commande enregistrée avec succès! (N°{nouvelle_cmd['numero_devis']})")

# ==================== MODULE 7 ====================
elif module == "Tableau de Bord":
    st.title("Tableau de Bord - KPIs et Historique des Commandes")
    
    # Charger l'historique
    historique = charger_historique()
    
    if not historique:
        st.warning("Aucune commande enregistrée pour le moment.")
        st.info("Créez des devis et enregistrez-les pour voir apparaître les KPIs ici.")
    else:
        # Onglets principaux
        tab_kpi, tab_historique, tab_analyse, tab_clients, tab_optimisation = st.tabs([
            "KPIs Globaux",
            "Historique des Commandes",
            "Analyses Temporelles",
            "Analyse par Client",
            "Optimisation des Couts"
        ])
        
        with tab_kpi:
            st.subheader("Indicateurs de Performance Clés (KPIs)")
            
            kpis = calculer_kpis()
            
            # Première ligne de KPIs
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class="metric-box metric-blue">
                    <div class="metric-label">Nombre de Devis</div>
                    <div class="metric-value">{kpis['nombre_devis']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-box metric-green">
                    <div class="metric-label">Résultat Total</div>
                    <div class="metric-value">{kpis['resultat_total']:,.0f} DA</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="metric-box metric-purple">
                    <div class="metric-label">Résultat Moyen</div>
                    <div class="metric-value">{kpis['resultat_moyen']:,.0f} DA</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                st.markdown(f"""
                <div class="metric-box metric-orange">
                    <div class="metric-label">CA Total</div>
                    <div class="metric-value">{kpis['prix_vente_total']:,.0f} DA</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Deuxième ligne de KPIs
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class="metric-box metric-red">
                    <div class="metric-label">Coût Total</div>
                    <div class="metric-value">{kpis['prix_revient_total']:,.0f} DA</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-box metric-green">
                    <div class="metric-label">Marge Moyenne (%)</div>
                    <div class="metric-value">{kpis['marge_moyenne']:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="metric-box metric-purple">
                    <div class="metric-label">Coefficient Moyen</div>
                    <div class="metric-value">{kpis['coefficient_moyen']:.2f}x</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                st.markdown(f"""
                <div class="metric-box metric-blue">
                    <div class="metric-label">Taux de Marque Moyen</div>
                    <div class="metric-value">{kpis['taux_marge_moyen']:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Analyse du meilleur et pire résultat
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="metric-box metric-green">
                    <div class="metric-label">Meilleur Resultat</div>
                    <div class="metric-value">{kpis['meilleur_resultat']:,.0f} DA</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-box metric-red">
                    <div class="metric-label">Pire Resultat</div>
                    <div class="metric-value">{kpis['pire_resultat']:,.0f} DA</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                profit_margin = ((kpis['resultat_total'] / kpis['prix_vente_total']) * 100) if kpis['prix_vente_total'] > 0 else 0
                st.markdown(f"""
                <div class="metric-box metric-orange">
                    <div class="metric-label">Marge Nette Globale</div>
                    <div class="metric-value">{profit_margin:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
        
        with tab_historique:
            st.subheader("Historique des Commandes")
            
            df_historique = obtenir_df_historique()
            st.dataframe(df_historique, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            st.subheader("Actions")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Exporter en CSV", use_container_width=True):
                    csv_file = exporter_csv()
                    if csv_file:
                        with open(csv_file, 'rb') as f:
                            st.download_button(
                                "Télécharger CSV",
                                f.read(),
                                csv_file,
                                "text/csv",
                                use_container_width=True
                            )
            
            with col2:
                if st.button("Réinitialiser l'historique", use_container_width=True):
                    st.warning("Cette action est irréversible!")
        
        with tab_analyse:
            st.subheader("Évolution Temporelle des KPIs")
            
            df_evolution = obtenir_evolution_temporelle()
            
            if not df_evolution.empty:
                # Graphique d'évolution du résultat cumulé
                fig_cumul = go.Figure()
                
                fig_cumul.add_trace(go.Scatter(
                    x=df_evolution['Date'],
                    y=df_evolution['Cumul Résultat'],
                    mode='lines+markers',
                    name='Résultat Cumulé',
                    line=dict(color='green', width=3),
                    fill='tozeroy'
                ))
                
                fig_cumul.update_layout(
                    title="Cumul du Résultat dans le Temps",
                    xaxis_title="Date",
                    yaxis_title="Résultat Cumulé (DA)",
                    hovermode='x unified',
                    height=400
                )
                
                st.plotly_chart(fig_cumul, use_container_width=True)
                
                # Graphique des résultats individuels
                fig_resultats = px.bar(
                    df_evolution,
                    x='Date',
                    y='Résultat',
                    color='Coefficient',
                    hover_data=['Client', 'Résultat'],
                    title="Résultat par Commande",
                    color_continuous_scale='RdYlGn'
                )
                
                fig_resultats.update_layout(height=400)
                st.plotly_chart(fig_resultats, use_container_width=True)
                
                # Tableau détaillé
                st.markdown("**Détail Chronologique**")
                st.dataframe(df_evolution, use_container_width=True, hide_index=True)
            else:
                st.info("Pas assez de données pour l'analyse temporelle.")
        
        with tab_clients:
            st.subheader("Performance par Client")
            
            df_clients = obtenir_analyse_clients()
            
            if not df_clients.empty:
                st.dataframe(df_clients, use_container_width=True, hide_index=True)
                
                # Graphiques
                col1, col2 = st.columns(2)
                
                with col1:
                    fig_clients_resultat = px.bar(
                        df_clients,
                        x='Client',
                        y='Résultat Total (DA)',
                        title="Résultat Total par Client",
                        color='Résultat Moyen (DA)',
                        color_continuous_scale='RdYlGn'
                    )
                    st.plotly_chart(fig_clients_resultat, use_container_width=True)
                
                with col2:
                    fig_clients_ca = px.pie(
                        df_clients,
                        values='CA Total (DA)',
                        names='Client',
                        title="Distribution du CA par Client"
                    )
                    st.plotly_chart(fig_clients_ca, use_container_width=True)
            else:
                st.info("Pas de données client disponibles.")
        
        with tab_optimisation:
            st.subheader("Optimisation des Couts - Predictions d'Amelioration")
            
            # Récupérer les données historiques
            historique_data = charger_historique()
            
            if historique_data:
                # Analyse des éléments de coûts
                st.markdown("**PARTIE 1: Identification des Postes de Couts**")
                
                # Calculer les coûts moyens par poste
                total_charges_directes_cum = {}
                total_frais_indirects_cum = 0
                nb_commandes = len(historique_data)
                
                for cmd in historique_data:
                    for charge, montant in cmd['finances']['charges_directes'].items():
                        if charge not in total_charges_directes_cum:
                            total_charges_directes_cum[charge] = 0
                        total_charges_directes_cum[charge] += montant
                    total_frais_indirects_cum += cmd['finances']['frais_indirects']
                
                # Moyennes par poste
                charges_moyennes = {k: v/nb_commandes for k, v in total_charges_directes_cum.items()}
                frais_indirects_moyen = total_frais_indirects_cum / nb_commandes
                
                # Créer DataFrame des postes de coûts
                postes_couts = []
                total_cost = sum(charges_moyennes.values()) + frais_indirects_moyen
                
                for charge, montant in charges_moyennes.items():
                    pct = (montant / total_cost) * 100
                    postes_couts.append({
                        'Poste': charge,
                        'Cout Moyen (DA)': montant,
                        '% du Total': pct,
                        'Type': 'Charge Directe'
                    })
                
                postes_couts.append({
                    'Poste': 'Frais Indirects',
                    'Cout Moyen (DA)': frais_indirects_moyen,
                    '% du Total': (frais_indirects_moyen / total_cost) * 100,
                    'Type': 'Charge Indirecte'
                })
                
                df_postes = pd.DataFrame(postes_couts)
                df_postes_sorted = df_postes.sort_values('Cout Moyen (DA)', ascending=False)
                
                # Affichage
                col1, col2 = st.columns(2)
                
                with col1:
                    st.dataframe(df_postes_sorted, use_container_width=True, hide_index=True)
                
                with col2:
                    fig_postes = px.pie(
                        df_postes_sorted,
                        values='Cout Moyen (DA)',
                        names='Poste',
                        title='Distribution des Couts par Poste'
                    )
                    st.plotly_chart(fig_postes, use_container_width=True)
                
                st.markdown("---")
                
                # PARTIE 2: Scénarios d'optimisation
                st.markdown("**PARTIE 2: Scenarios de Reduction des Couts**")
                
                col1, col2, col3 = st.columns(3)
                
                # Sliders de réduction
                with col1:
                    reduction_charges_directes = st.slider(
                        "Reduction des Charges Directes (%)",
                        0, 30, 5, 1,
                        help="Négociation fournisseurs, optimisation achats"
                    )
                
                with col2:
                    reduction_frais_indirects = st.slider(
                        "Reduction des Frais Indirects (%)",
                        0, 20, 3, 1,
                        help="Optimisation des ressources, réduction des coûts fixes"
                    )
                
                with col3:
                    reduction_marge = st.slider(
                        "Augmentation de Marge (%)",
                        0, 10, 2, 1,
                        help="Augmentation du prix de vente ou du taux de marge"
                    )
                
                st.markdown("---")
                
                # Calcul des impacts
                st.markdown("**PREDICTIONS D'IMPACT**")
                
                # Scénario actuel
                coût_moyen_actuel = sum(charges_moyennes.values()) + frais_indirects_moyen
                marge_moyenne_actuelle = kpis['marge_moyenne']
                prix_vente_moyen_actuel = coût_moyen_actuel * (1 + marge_moyenne_actuelle/100)
                resultat_moyen_actuel = prix_vente_moyen_actuel - coût_moyen_actuel
                
                # Scénario optimisé
                charges_optimisees = sum(charges_moyennes.values()) * (1 - reduction_charges_directes/100)
                frais_optimises = frais_indirects_moyen * (1 - reduction_frais_indirects/100)
                coût_moyen_optimise = charges_optimisees + frais_optimises
                
                nouvelle_marge = marge_moyenne_actuelle + reduction_marge
                prix_vente_moyen_optimise = coût_moyen_optimise * (1 + nouvelle_marge/100)
                resultat_moyen_optimise = prix_vente_moyen_optimise - coût_moyen_optimise
                
                # Gains potentiels
                gain_par_commande = resultat_moyen_optimise - resultat_moyen_actuel
                gain_total = gain_par_commande * nb_commandes
                
                # Affichage des résultats
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Scenario Actuel")
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-label">Cout Moyen par Commande</div>
                        <div class="metric-value">{coût_moyen_actuel:,.0f} DA</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-label">Prix de Vente Moyen</div>
                        <div class="metric-value">{prix_vente_moyen_actuel:,.0f} DA</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="metric-box metric-green">
                        <div class="metric-label">Resultat Moyen</div>
                        <div class="metric-value">{resultat_moyen_actuel:,.0f} DA</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.subheader("Scenario Optimise")
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-label">Cout Moyen par Commande</div>
                        <div class="metric-value">{coût_moyen_optimise:,.0f} DA</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-label">Prix de Vente Moyen</div>
                        <div class="metric-value">{prix_vente_moyen_optimise:,.0f} DA</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="metric-box metric-orange">
                        <div class="metric-label">Resultat Moyen</div>
                        <div class="metric-value">{resultat_moyen_optimise:,.0f} DA</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("---")
                st.subheader("Gains Potentiels")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    economie_realisée = (reduction_charges_directes/100 * charges_optimisees) + (reduction_frais_indirects/100 * frais_optimises)
                    st.markdown(f"""
                    <div class="metric-box metric-blue">
                        <div class="metric-label">Economie par Commande</div>
                        <div class="metric-value">{gain_par_commande:,.0f} DA</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div class="metric-box metric-green">
                        <div class="metric-label">Gain Total (annuel)</div>
                        <div class="metric-value">{gain_total:,.0f} DA</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    pct_amelioration = ((resultat_moyen_optimise / resultat_moyen_actuel) - 1) * 100
                    st.markdown(f"""
                    <div class="metric-box metric-purple">
                        <div class="metric-label">Amelioration Resultat</div>
                        <div class="metric-value">+{pct_amelioration:.1f}%</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Graphique de comparaison
                st.subheader("Comparaison Scenario Actuel vs Optimise")
                
                comparison_data = {
                    'Scenario': ['Actuel', 'Optimise'],
                    'Couts': [coût_moyen_actuel, coût_moyen_optimise],
                    'Prix de Vente': [prix_vente_moyen_actuel, prix_vente_moyen_optimise],
                    'Resultat': [resultat_moyen_actuel, resultat_moyen_optimise]
                }
                
                fig_comparison = go.Figure()
                fig_comparison.add_trace(go.Bar(name='Couts', x=comparison_data['Scenario'], y=comparison_data['Couts']))
                fig_comparison.add_trace(go.Bar(name='Resultat', x=comparison_data['Scenario'], y=comparison_data['Resultat']))
                
                fig_comparison.update_layout(
                    title='Comparaison: Scenario Actuel vs Optimise',
                    xaxis_title='Scenario',
                    yaxis_title='Montant (DA)',
                    barmode='group',
                    height=400
                )
                st.plotly_chart(fig_comparison, use_container_width=True)
                
                st.markdown("---")
                
                # Recommandations
                st.markdown("**RECOMMANDATIONS D'OPTIMISATION**")
                
                recommendations = []
                
                # Analyser les postes majeurs
                top_poste = df_postes_sorted.iloc[0]
                recommendations.append(f"1. Priorite: Negocier le poste '{top_poste['Poste']}' ({top_poste['% du Total']:.1f}% du total)")
                
                if 'Salaires' in charges_moyennes or 'Salaires' in [p['Poste'] for p in postes_couts]:
                    recommendations.append("2. Optimiser les couts de main d'oeuvre par une meilleure productivite")
                
                if 'Transport' in charges_moyennes or 'Transport' in [p['Poste'] for p in postes_couts]:
                    recommendations.append("3. Negocier les couts de transport avec les prestataires")
                
                recommendations.append("4. Examiner les charges indirectes pour identifier les economies possibles")
                recommendations.append("5. Augmenter progressivement la marge tarifaire avec une justification client")
                recommendations.append("6. Revoir les processus pour eliminer les gaspillages")
                
                for rec in recommendations:
                    st.info(rec)
                
            else:
                st.warning("Pas assez de donnees historiques pour l'analyse d'optimisation.")
                st.info("Creez et enregistrez au moins une commande pour acceder a cette fonction.")

# Footer

st.markdown("---")
st.markdown("""
<footer style="text-align: center; color: #999; font-size: 12px; padding: 20px 0;">
ELCO-BAT SARL © 2024 | Calcul du Prix de Revient - Méthode des Sections Homogènes | Version 2.0 avec Historique & KPIs
</footer>
""", unsafe_allow_html=True)
