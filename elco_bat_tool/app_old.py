import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Configuration de la page
st.set_page_config(
    page_title="ELCO-BAT | Calcul de Prix de Revient",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
    .success-card {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .warning-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Initialiser les données en session
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    
    # Données par défaut ELCO-BAT SARL
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

# En-tête
st.title("🏭 ELCO-BAT SARL - Outil de Calcul du Prix de Revient")
st.markdown("**Méthode des sections homogènes - Calcul analytique des coûts**")

# Sidebar Navigation
with st.sidebar:
    st.image("https://via.placeholder.com/100?text=ELCO-BAT", width=100)
    st.markdown("---")
    
    module = st.radio("📋 Sélectionner le module", [
        "🔧 Module 1 - Paramétrage des charges",
        "📊 Module 2 - Répartition primaire",
        "🔄 Module 3 - Répartition secondaire",
        "📈 Module 4 - Coûts d'UO",
        "🛒 Module 5 - Fiche de la commande",
        "💰 Module 6 - Aide à la décision"
    ])

# ==================== MODULE 1 ====================
if "Module 1" in module:
    st.header("🔧 Module 1 - Paramétrage des charges")
    
    tab1, tab2, tab3 = st.tabs(["Charges indirectes", "Clés de répartition", "Charges directes"])
    
    with tab1:
        st.subheader("Saisie des charges indirectes")
        col1, col2 = st.columns(2)
        
        charges_data = {}
        charges_list = list(st.session_state.charges_indirectes.keys())
        
        for i, charge in enumerate(charges_list):
            if i % 2 == 0:
                with col1:
                    charges_data[charge] = st.number_input(
                        f"💰 {charge}",
                        value=st.session_state.charges_indirectes[charge],
                        step=1000,
                        key=f"charge_{charge}"
                    )
            else:
                with col2:
                    charges_data[charge] = st.number_input(
                        f"💰 {charge}",
                        value=st.session_state.charges_indirectes[charge],
                        step=1000,
                        key=f"charge_{charge}"
                    )
        
        st.session_state.charges_indirectes = charges_data
        
        # Affichage résumé
        total_charges = sum(charges_data.values())
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Nombre de charges", len(charges_data))
        with col2:
            st.metric("Total charges", f"{total_charges:,.0f} DA")
        with col3:
            st.metric("Moyenne", f"{total_charges/len(charges_data):,.0f} DA")
        
        # Tableau récapitulatif
        st.subheader("📋 Récapitulatif des charges")
        df_charges = pd.DataFrame({
            'Charge': charges_data.keys(),
            'Montant (DA)': charges_data.values()
        })
        st.dataframe(df_charges, use_container_width=True)
        
        # Graphique
        fig = px.pie(df_charges, names='Charge', values='Montant (DA)',
                     title="Distribution des charges indirectes")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Configuration des clés de répartition")
        st.info("💡 Les clés de répartition permettent de ventiler les charges entre les centres")
        
        charge_selected = st.selectbox("Sélectionner une charge:", list(st.session_state.cles_repartition.keys()))
        
        col1, col2, col3 = st.columns(3)
        
        # Centres principaux et auxiliaires
        centres_aux = [c for c, t in st.session_state.centres.items() if t == 'Auxiliaire']
        centres_prin = [c for c, t in st.session_state.centres.items() if t == 'Principal']
        
        cles_updated = st.session_state.cles_repartition[charge_selected].copy()
        
        with col1:
            st.write("**Centres Auxiliaires**")
            for centre in centres_aux:
                cles_updated[centre] = st.slider(
                    f"{centre}",
                    0.0, 1.0,
                    st.session_state.cles_repartition[charge_selected][centre],
                    0.05,
                    key=f"cle_{charge_selected}_{centre}"
                )
        
        with col2:
            st.write("**Centres Principaux (1/2)**")
            for centre in centres_prin[:2]:
                cles_updated[centre] = st.slider(
                    f"{centre}",
                    0.0, 1.0,
                    st.session_state.cles_repartition[charge_selected][centre],
                    0.05,
                    key=f"cle_{charge_selected}_{centre}"
                )
        
        with col3:
            st.write("**Centres Principaux (2/2)**")
            for centre in centres_prin[2:]:
                cles_updated[centre] = st.slider(
                    f"{centre}",
                    0.0, 1.0,
                    st.session_state.cles_repartition[charge_selected][centre],
                    0.05,
                    key=f"cle_{charge_selected}_{centre}"
                )
        
        total_cles = sum(cles_updated.values())
        if abs(total_cles - 1.0) < 0.001:
            st.success(f"✅ Total des clés = {total_cles:.2%}")
        else:
            st.warning(f"⚠️ Total des clés = {total_cles:.2%} (doit être 100%)")
        
        st.session_state.cles_repartition[charge_selected] = cles_updated
        
        # Tableau des clés
        st.subheader("📊 Tableau des clés de répartition")
        cles_df = pd.DataFrame(st.session_state.cles_repartition).T
        st.dataframe(cles_df, use_container_width=True)
    
    with tab3:
        st.subheader("Identification des charges directes de la commande")
        
        col1, col2 = st.columns(2)
        
        charges_directes = {}
        cd_list = list(st.session_state.charges_directes.keys())
        
        for i, charge in enumerate(cd_list):
            if i % 2 == 0:
                with col1:
                    charges_directes[charge] = st.number_input(
                        f"💳 {charge}",
                        value=st.session_state.charges_directes[charge],
                        step=1000,
                        key=f"cd_{charge}"
                    )
            else:
                with col2:
                    charges_directes[charge] = st.number_input(
                        f"💳 {charge}",
                        value=st.session_state.charges_directes[charge],
                        step=1000,
                        key=f"cd_{charge}"
                    )
        
        st.session_state.charges_directes = charges_directes
        
        total_cd = sum(charges_directes.values())
        st.metric("Total charges directes", f"{total_cd:,.0f} DA")
        
        df_cd = pd.DataFrame({
            'Charge': charges_directes.keys(),
            'Montant (DA)': charges_directes.values()
        })
        st.dataframe(df_cd, use_container_width=True)

# ==================== MODULE 2 ====================
elif "Module 2" in module:
    st.header("📊 Module 2 - Répartition primaire")
    
    # Calcul de la répartition primaire
    centres = list(st.session_state.centres.keys())
    charges = list(st.session_state.charges_indirectes.keys())
    
    repartition_primaire = {}
    for centre in centres:
        repartition_primaire[centre] = 0
        for charge in charges:
            montant = st.session_state.charges_indirectes[charge]
            cle = st.session_state.cles_repartition[charge][centre]
            repartition_primaire[centre] += montant * cle
    
    # Créer le tableau détaillé
    data_repartition = {}
    for charge in charges:
        data_repartition[charge] = {}
        for centre in centres:
            montant = st.session_state.charges_indirectes[charge]
            cle = st.session_state.cles_repartition[charge][centre]
            data_repartition[charge][centre] = montant * cle
    
    df_repartition = pd.DataFrame(data_repartition).T
    df_repartition['Total'] = df_repartition.sum(axis=1)
    totaux_colonnes = df_repartition.sum()
    
    st.subheader("📋 Tableau de répartition primaire")
    st.dataframe(df_repartition, use_container_width=True)
    
    # Totaux par centre
    st.subheader("📊 Totaux par centre (avant transfert)")
    
    col1, col2, col3 = st.columns(3)
    centres_aux = [c for c in centres if st.session_state.centres[c] == 'Auxiliaire']
    centres_prin = [c for c in centres if st.session_state.centres[c] == 'Principal']
    
    with col1:
        st.write("**Centres Auxiliaires**")
        for centre in centres_aux:
            st.metric(centre, f"{repartition_primaire[centre]:,.0f} DA")
    
    with col2:
        st.write("**Centres Principaux (1/3)**")
        for centre in centres_prin[:2]:
            st.metric(centre, f"{repartition_primaire[centre]:,.0f} DA")
    
    with col3:
        st.write("**Centres Principaux (2/3)**")
        for centre in centres_prin[2:]:
            st.metric(centre, f"{repartition_primaire[centre]:,.0f} DA")
    
    # Graphique
    st.subheader("📈 Graphique de répartition")
    
    tab1, tab2 = st.tabs(["Par centre", "Par charge"])
    
    with tab1:
        fig = px.bar(
            x=list(repartition_primaire.keys()),
            y=list(repartition_primaire.values()),
            labels={'x': 'Centre', 'y': 'Montant (DA)'},
            title="Répartition primaire par centre"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        fig = px.line(df_repartition.iloc[:, :-1], 
                      title="Évolution des charges par centre")
        st.plotly_chart(fig, use_container_width=True)
    
    st.session_state.repartition_primaire = repartition_primaire

# ==================== MODULE 3 ====================
elif "Module 3" in module:
    st.header("🔄 Module 3 - Répartition secondaire")
    
    # Récupérer la répartition primaire
    if 'repartition_primaire' not in st.session_state:
        st.warning("⚠️ Veuillez d'abord compléter le Module 2")
        st.stop()
    
    repartition_primaire = st.session_state.repartition_primaire.copy()
    repartition_secondaire = repartition_primaire.copy()
    
    centres_aux = [c for c, t in st.session_state.centres.items() if t == 'Auxiliaire']
    centres_prin = [c for c, t in st.session_state.centres.items() if t == 'Principal']
    
    # Afficher les clés de répartition secondaire
    st.subheader("📋 Clés de répartition secondaire")
    
    repart_sec_updated = {}
    for centre_aux in centres_aux:
        st.write(f"**Distribution du centre {centre_aux}:**")
        repart_sec_updated[centre_aux] = {}
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("Centres auxiliaires:")
            for centre_dest in centres_aux:
                if centre_dest != centre_aux:
                    repart_sec_updated[centre_aux][centre_dest] = st.slider(
                        f"{centre_aux} → {centre_dest}",
                        0.0, 1.0,
                        st.session_state.repart_secondaire[centre_aux].get(centre_dest, 0.0),
                        0.05,
                        key=f"rs_{centre_aux}_{centre_dest}"
                    )
        
        with col2:
            st.write("Centres principaux:")
            centres_prin_list = [c for c in centres_prin if c not in repart_sec_updated[centre_aux]]
            for centre_dest in centres_prin_list:
                repart_sec_updated[centre_aux][centre_dest] = st.slider(
                    f"{centre_aux} → {centre_dest}",
                    0.0, 1.0,
                    st.session_state.repart_secondaire[centre_aux].get(centre_dest, 0.0),
                    0.05,
                    key=f"rs_{centre_aux}_{centre_dest}"
                )
        
        st.markdown("---")
    
    st.session_state.repart_secondaire = repart_sec_updated
    
    # Calcul du vidage
    st.subheader("🔄 Vidage des centres auxiliaires")
    
    for centre_aux in centres_aux:
        montant_aux = repartition_secondaire[centre_aux]
        st.write(f"**Vidage {centre_aux}: {montant_aux:,.0f} DA**")
        
        for centre_dest, cle in repart_sec_updated[centre_aux].items():
            montant_transfer = montant_aux * cle
            repartition_secondaire[centre_dest] += montant_transfer
            st.write(f"  → {centre_dest}: {cle:.0%} × {montant_aux:,.0f} = {montant_transfer:,.0f} DA")
        
        repartition_secondaire[centre_aux] = 0
    
    # Résultats finaux
    st.subheader("✅ Totaux finaux des centres principaux")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Centres Principaux**")
        for centre in centres_prin:
            st.metric(centre, f"{repartition_secondaire[centre]:,.0f} DA")
    
    with col2:
        st.write("**Vérification**")
        total_secondaire = sum([repartition_secondaire[c] for c in centres_prin])
        total_primaire = sum(st.session_state.charges_indirectes.values())
        st.metric("Total centres princ.", f"{total_secondaire:,.0f} DA")
        st.metric("Total charges", f"{total_primaire:,.0f} DA")
        if abs(total_secondaire - total_primaire) < 1:
            st.success("✅ Cohérent!")
        else:
            st.error(f"❌ Écart: {total_secondaire - total_primaire:,.0f} DA")
    
    # Graphique
    fig = px.bar(
        x=centres_prin,
        y=[repartition_secondaire[c] for c in centres_prin],
        labels={'x': 'Centre principal', 'y': 'Montant (DA)'},
        title="Répartition après vidage des centres auxiliaires"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.session_state.repartition_secondaire = repartition_secondaire

# ==================== MODULE 4 ====================
elif "Module 4" in module:
    st.header("📈 Module 4 - Calcul des coûts d'UO")
    
    if 'repartition_secondaire' not in st.session_state:
        st.warning("⚠️ Veuillez d'abord compléter le Module 3")
        st.stop()
    
    repartition_secondaire = st.session_state.repartition_secondaire
    centres_prin = [c for c, t in st.session_state.centres.items() if t == 'Principal']
    
    st.subheader("⚙️ Configuration des unités d'œuvre")
    
    unites_updated = {}
    col1, col2 = st.columns(2)
    
    for i, centre in enumerate(centres_prin):
        if i % 2 == 0:
            col = col1
        else:
            col = col2
        
        with col:
            unites_updated[centre] = st.number_input(
                f"{centre} - Nombre d'UO du mois",
                value=st.session_state.unites_oeuvre[centre],
                step=10,
                key=f"uo_{centre}"
            )
    
    st.session_state.unites_oeuvre = unites_updated
    
    # Calcul des CUO
    st.subheader("💰 Calcul du coût de l'unité d'œuvre")
    
    cuos = {}
    data_cuos = []
    
    for centre in centres_prin:
        total_centre = repartition_secondaire[centre]
        nuo = unites_updated[centre]
        cuo = total_centre / nuo if nuo > 0 else 0
        cuos[centre] = cuo
        
        data_cuos.append({
            'Centre': centre,
            'Total (DA)': total_centre,
            'NUO': nuo,
            'CUO (DA/UO)': cuo
        })
    
    df_cuos = pd.DataFrame(data_cuos)
    st.dataframe(df_cuos, use_container_width=True)
    
    # Affichage par centre
    st.subheader("📊 Détail par centre")
    
    for centre in centres_prin:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                f"{centre} - Total",
                f"{repartition_secondaire[centre]:,.0f} DA"
            )
        
        with col2:
            st.metric(
                f"{centre} - NUO",
                f"{unites_updated[centre]} UO"
            )
        
        with col3:
            st.metric(
                f"{centre} - CUO",
                f"{cuos[centre]:,.2f} DA/UO"
            )
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(df_cuos, x='Centre', y='Total (DA)',
                     title="Total des charges par centre")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.bar(df_cuos, x='Centre', y='CUO (DA/UO)',
                     title="Coût unitaire d'œuvre par centre")
        st.plotly_chart(fig, use_container_width=True)
    
    st.session_state.cuos = cuos

# ==================== MODULE 5 ====================
elif "Module 5" in module:
    st.header("🛒 Module 5 - Fiche de la commande")
    
    if 'cuos' not in st.session_state:
        st.warning("⚠️ Veuillez d'abord compléter le Module 4")
        st.stop()
    
    centres_prin = [c for c, t in st.session_state.centres.items() if t == 'Principal']
    
    st.subheader("A. Charges directes de la commande")
    
    col1, col2 = st.columns(2)
    
    charges_dir_updated = {}
    cd_list = list(st.session_state.charges_directes.keys())
    
    for i, charge in enumerate(cd_list):
        if i % 2 == 0:
            with col1:
                charges_dir_updated[charge] = st.number_input(
                    f"{charge}",
                    value=st.session_state.charges_directes[charge],
                    step=1000,
                    key=f"cmd_cd_{charge}"
                )
        else:
            with col2:
                charges_dir_updated[charge] = st.number_input(
                    f"{charge}",
                    value=st.session_state.charges_directes[charge],
                    step=1000,
                    key=f"cmd_cd_{charge}"
                )
    
    st.session_state.charges_directes = charges_dir_updated
    total_cd = sum(charges_dir_updated.values())
    
    data_cd = pd.DataFrame({
        'Élément': charges_dir_updated.keys(),
        'Montant (DA)': charges_dir_updated.values()
    })
    st.dataframe(data_cd, use_container_width=True)
    st.metric("Total charges directes", f"{total_cd:,.0f} DA")
    
    st.subheader("B. Consommation de la commande par centre")
    
    col1, col2 = st.columns(2)
    
    consommation_updated = {}
    cons_list = list(st.session_state.consommation_command.keys())
    
    for i, centre in enumerate(cons_list):
        if i % 2 == 0:
            with col1:
                consommation_updated[centre] = st.number_input(
                    f"{centre} (UO)",
                    value=st.session_state.consommation_command[centre],
                    step=1,
                    key=f"cons_{centre}"
                )
        else:
            with col2:
                consommation_updated[centre] = st.number_input(
                    f"{centre} (UO)",
                    value=st.session_state.consommation_command[centre],
                    step=1,
                    key=f"cons_{centre}"
                )
    
    st.session_state.consommation_command = consommation_updated
    
    st.subheader("C. Frais indirects imputés")
    
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
            'Frais imputés (DA)': frais
        })
    
    df_frais = pd.DataFrame(data_frais)
    st.dataframe(df_frais, use_container_width=True)
    
    total_frais = sum(frais_indirects.values())
    
    st.subheader("💰 Prix de revient")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Charges directes", f"{total_cd:,.0f} DA")
    
    with col2:
        st.metric("Frais indirects", f"{total_frais:,.0f} DA")
    
    with col3:
        prix_revient = total_cd + total_frais
        st.metric("Prix de revient", f"{prix_revient:,.0f} DA", delta=f"+{total_frais:,.0f}")
    
    with col4:
        st.metric("Nombre d'unités", int(st.session_state.consommation_command.get('DIST', 1)))
    
    # Tableau récapitulatif
    st.subheader("📋 Fiche complète du prix de revient")
    
    fiche = {
        'Catégorie': ['Aluminium', 'Vitrage', 'Quincaillerie', 'MOD directe',
                     'Approvisionnement', 'Atelier Découpe', 'Atelier Montage', 'Distribution',
                     'TOTAL'],
        'Montant (DA)': [
            charges_dir_updated['Aluminium'],
            charges_dir_updated['Vitrage'],
            charges_dir_updated['Quincaillerie'],
            charges_dir_updated['MOD'],
            frais_indirects['APPRO'],
            frais_indirects['AT-D'],
            frais_indirects['AT-ML'],
            frais_indirects['DIST'],
            prix_revient
        ]
    }
    
    df_fiche = pd.DataFrame(fiche)
    st.dataframe(df_fiche, use_container_width=True)
    
    st.session_state.prix_revient = prix_revient
    st.session_state.total_frais_indirects = total_frais

# ==================== MODULE 6 ====================
elif "Module 6" in module:
    st.header("💰 Module 6 - Aide à la décision")
    
    if 'prix_revient' not in st.session_state:
        st.warning("⚠️ Veuillez d'abord compléter le Module 5")
        st.stop()
    
    prix_revient = st.session_state.prix_revient
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📊 Prix de revient")
        st.metric("", f"{prix_revient:,.0f} DA")
    
    with col2:
        st.subheader("📈 Marge souhaitée (%)")
        marge_pct = st.slider("Marge bénéficiaire (%)", 5, 50, 20, 1)
    
    with col3:
        marge_montant = prix_revient * (marge_pct / 100)
        st.subheader("💵 Marge (DA)")
        st.metric("", f"{marge_montant:,.0f} DA")
    
    st.markdown("---")
    
    # Calcul du devis
    prix_vente = prix_revient + marge_montant
    nb_units = int(st.session_state.consommation_command.get('DIST', 1))
    prix_unitaire = prix_vente / nb_units
    
    st.subheader("💼 Proposition de devis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Prix de vente total", f"{prix_vente:,.0f} DA")
    
    with col2:
        st.metric("Nombre d'unités", nb_units)
    
    with col3:
        st.metric("Prix unitaire", f"{prix_unitaire:,.2f} DA/U")
    
    st.markdown("---")
    
    # Résultat analytique
    st.subheader("📊 Résultat analytique")
    
    resultat = prix_vente - prix_revient
    taux_marge = (resultat / prix_vente) * 100
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Résultat", f"{resultat:,.0f} DA")
    
    with col2:
        st.metric("Taux de marge", f"{taux_marge:.1f}%")
    
    with col3:
        st.metric("CA prévu", f"{prix_vente:,.0f} DA")
    
    with col4:
        st.metric("Coefficient", f"{prix_vente/prix_revient:.2f}x")
    
    st.markdown("---")
    
    # Tableau de synthèse
    st.subheader("📋 Tableau de synthèse financière")
    
    synthese = {
        'Élément': [
            'Charges directes',
            'Frais indirects imputés',
            'PRIX DE REVIENT',
            'Marge bénéficiaire',
            'PRIX DE VENTE',
            'Nombre d\'unités',
            'PRIX UNITAIRE'
        ],
        'Montant (DA)': [
            sum(st.session_state.charges_directes.values()),
            st.session_state.total_frais_indirects,
            prix_revient,
            marge_montant,
            prix_vente,
            nb_units,
            prix_unitaire
        ]
    }
    
    df_synthese = pd.DataFrame(synthese)
    st.dataframe(df_synthese, use_container_width=True)
    
    # Graphiques d'analyse
    st.subheader("📈 Graphiques d'analyse")
    
    tab1, tab2, tab3 = st.tabs(["Composition du prix", "Sensibilité marge/prix", "Analyse coûts-revenus"])
    
    with tab1:
        labels = ['Charges directes', 'Frais indirects', 'Marge']
        sizes = [
            sum(st.session_state.charges_directes.values()),
            st.session_state.total_frais_indirects,
            marge_montant
        ]
        fig = px.pie(names=labels, values=sizes, title="Composition du prix de vente")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        marges = list(range(5, 51, 5))
        prix_marges = [prix_revient * (1 + m/100) for m in marges]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=marges, y=prix_marges, mode='lines+markers',
                                name='Prix de vente'))
        fig.add_hline(y=prix_revient, line_dash="dash", line_color="red", 
                     annotation_text="Prix de revient")
        fig.update_layout(title="Sensibilité: Marge vs Prix de vente",
                         xaxis_title="Marge (%)",
                         yaxis_title="Prix de vente (DA)")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        categories = ['Charges\ndirectes', 'Frais\nindirects', 'Total\ncoûts', 'Prix\nde vente',
                     'Résultat']
        montants = [
            sum(st.session_state.charges_directes.values()),
            st.session_state.total_frais_indirects,
            prix_revient,
            prix_vente,
            resultat
        ]
        
        fig = px.bar(x=categories, y=montants, 
                    title="Analyse coûts-revenus",
                    labels={'x': '', 'y': 'Montant (DA)'})
        st.plotly_chart(fig, use_container_width=True)
    
    # Générer un devis exportable
    st.markdown("---")
    st.subheader("📄 Devis proposé")
    
    devis_text = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║              DEVIS ELCO-BAT SARL                         ║
    ║           Menuiserie Aluminium - Tizi Ouzou             ║
    ╚═══════════════════════════════════════════════════════════╝
    
    Commande: 120 ensembles de menuiserie aluminium
    
    ───────────────────────────────────────────────────────────
    DÉTAIL DU PRIX DE REVIENT
    ───────────────────────────────────────────────────────────
    
    Charges directes:
      • Aluminium (profilés)      : {st.session_state.charges_directes['Aluminium']:>15,.0f} DA
      • Vitrage                   : {st.session_state.charges_directes['Vitrage']:>15,.0f} DA
      • Quincaillerie/accessoires : {st.session_state.charges_directes['Quincaillerie']:>15,.0f} DA
      • Main-d'œuvre directe      : {st.session_state.charges_directes['MOD']:>15,.0f} DA
    
    Frais indirects imputés:
      • Approvisionnement         : {st.session_state.cuos['APPRO'] * st.session_state.consommation_command['APPRO']:>15,.0f} DA
      • Atelier Découpe           : {st.session_state.cuos['AT-D'] * st.session_state.consommation_command['AT-D']:>15,.0f} DA
      • Atelier Montage-Laquage   : {st.session_state.cuos['AT-ML'] * st.session_state.consommation_command['AT-ML']:>15,.0f} DA
      • Distribution              : {st.session_state.cuos['DIST'] * st.session_state.consommation_command['DIST']:>15,.0f} DA
    
    ───────────────────────────────────────────────────────────
    PRIX DE REVIENT (total)      : {prix_revient:>20,.0f} DA
    MARGE BÉNÉFICIAIRE ({marge_pct}%)  : {marge_montant:>20,.0f} DA
    ───────────────────────────────────────────────────────────
    PRIX DE VENTE (HT)           : {prix_vente:>20,.0f} DA
    
    Prix unitaire                 : {prix_unitaire:>20,.2f} DA/ensemble
    
    ───────────────────────────────────────────────────────────
    RÉSULTAT ANALYTIQUE          : {resultat:>20,.0f} DA
    TAUX DE MARGE                : {taux_marge:>20,.1f} %
    ───────────────────────────────────────────────────────────
    
    Date: {datetime.now().strftime('%d/%m/%Y')}
    Validité: 30 jours
    """
    
    st.code(devis_text, language="text")
    
    # Bouton téléchargement
    st.download_button(
        label="📥 Télécharger le devis",
        data=devis_text,
        file_name=f"Devis_ELCOBAT_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p style='color: #888; font-size: 12px;'>
    ELCO-BAT SARL © 2024 | Outil de calcul du prix de revient - Méthode des sections homogènes
    </p>
</div>
""", unsafe_allow_html=True)
