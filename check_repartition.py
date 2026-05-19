charges_indirectes = {
    'Loyer': 180000,
    'Électricité / énergie': 96000,
    'Entretien matériels': 72000,
    'Salaires personnel indirect': 240000,
    'Amortissement machines': 120000,
    'Fournitures administratives': 24000,
    'Transport / livraison': 60000
}

cles = {
    'Loyer': {'ADM': 0.10, 'ENT': 0.05, 'APPRO': 0.10, 'AT-D': 0.30, 'AT-ML': 0.35, 'DIST': 0.10},
    'Électricité / énergie': {'ADM': 0.05, 'ENT': 0.05, 'APPRO': 0.05, 'AT-D': 0.40, 'AT-ML': 0.40, 'DIST': 0.05},
    'Entretien matériels': {'ADM': 0.0, 'ENT': 0.60, 'APPRO': 0.05, 'AT-D': 0.15, 'AT-ML': 0.15, 'DIST': 0.05},
    'Salaires personnel indirect': {'ADM': 0.30, 'ENT': 0.10, 'APPRO': 0.15, 'AT-D': 0.20, 'AT-ML': 0.15, 'DIST': 0.10},
    'Amortissement machines': {'ADM': 0.0, 'ENT': 0.10, 'APPRO': 0.0, 'AT-D': 0.45, 'AT-ML': 0.45, 'DIST': 0.0},
    'Fournitures administratives': {'ADM': 0.40, 'ENT': 0.0, 'APPRO': 0.20, 'AT-D': 0.10, 'AT-ML': 0.10, 'DIST': 0.20},
    'Transport / livraison': {'ADM': 0.0, 'ENT': 0.0, 'APPRO': 0.10, 'AT-D': 0.0, 'AT-ML': 0.0, 'DIST': 0.90}
}

centres = ['ADM','ENT','APPRO','AT-D','AT-ML','DIST']
repart_primaire = {c:0 for c in centres}
for charge, montant in charges_indirectes.items():
    for c in centres:
        repart_primaire[c] += montant * cles[charge][c]

print('Repartition primaire:')
for c in centres:
    print(c, f"{repart_primaire[c]:,.0f}")

# secondary mapping
repart_secondaire = {
    'ADM': {'ENT': 0.10, 'APPRO': 0.15, 'AT-D': 0.25, 'AT-ML': 0.30, 'DIST': 0.20},
    'ENT': {'ADM': 0.15, 'APPRO': 0.10, 'AT-D': 0.30, 'AT-ML': 0.35, 'DIST': 0.10}
}

# start with primary totals
repart_final = repart_primaire.copy()
# solve ADM/ENT reciprocal
A = repart_final['ADM']
B = repart_final['ENT']
# selon convention: x = part(ENT->ADM), y = part(ADM->ENT)
x = repart_secondaire['ENT']['ADM']
y = repart_secondaire['ADM']['ENT']
denom = 1 - x*y
A_real = (A + x*B)/denom
E_real = B + y*A_real
print('\nADM primaire', A, 'ENT primaire', B)
print('ADM réel approx', A_real)
print('ENT réel approx', E_real)
# distribute
for dest, cle in repart_secondaire['ADM'].items():
    if dest not in ['ADM','ENT']:
        repart_final[dest] += A_real * cle
for dest, cle in repart_secondaire['ENT'].items():
    if dest not in ['ADM','ENT']:
        repart_final[dest] += E_real * cle
repart_final['ADM'] = 0
repart_final['ENT'] = 0

print('\nRepartition finale (principaux):')
for c in ['APPRO','AT-D','AT-ML','DIST']:
    print(c, f"{repart_final[c]:,.0f}")

print('\nTotal final:', f"{sum(repart_final.values()):,.0f}")
print('Total primaire sum:', f"{sum(charges_indirectes.values()):,.0f}")

# Calcul des CUO et prix de revient
charges_directes = {
    'Tissu principal': 840000,
    'Fournitures de couture': 72000,
    'Bandes réfléchissantes et renforts EPI': 96000,
    'Main-d’œuvre directe couture': 192000
}

unites_oeuvre = {'APPRO': 12000, 'AT-D': 7200, 'AT-ML': 2400, 'DIST': 1800}
consommation_command = {'APPRO': 3000, 'AT-D': 3000, 'AT-ML': 600, 'DIST': 600}

cuos = {}
frais_indirects = {}
for centre in ['APPRO','AT-D','AT-ML','DIST']:
    total_centre = repart_final[centre]
    nuo = unites_oeuvre[centre]
    cuo = total_centre / nuo if nuo>0 else 0
    cuos[centre] = cuo
    frais_indirects[centre] = cuo * consommation_command[centre]

total_cd = sum(charges_directes.values())
total_frais = sum(frais_indirects.values())
prix_revient = total_cd + total_frais

print('\nCharges directes total:', f"{total_cd:,.0f}")
print('Frais indirects imputés total:', f"{total_frais:,.0f}")
print('Prix de revient:', f"{prix_revient:,.0f}")

# Devis avec marge 20%
marge_pct = 20
marge_montant = prix_revient * (marge_pct/100)
prix_vente = prix_revient + marge_montant
prix_unitaire = prix_vente / consommation_command['DIST']

print('\nMarge 20%:', f"{marge_montant:,.0f}")
print('Prix de vente proposé:', f"{prix_vente:,.0f}")
print('Prix unitaire:', f"{prix_unitaire:,.0f} DA par tenue")
