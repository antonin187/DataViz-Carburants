import pandas as pd
from pathlib import Path 

df_carb = pd.read_csv("../Prix_carburants_France_instantane.csv", delimiter=';', on_bad_lines='skip')
# print(df_carb.head)

#Affiche les colonnes avant nettoyage
print("Colonnes originales : ", df_carb.columns)

# Retire la colonne "pop" et "Services proposés" du dataframe (en erreur pour l'instant)
df_carb.drop(columns=['pop', 'Services proposés' ], inplace=True)

# Enlever les lignes qui n'ont pas d'informations dans "carburant disponible"
df_carb.drop(df_carb[df_carb['Carburants disponibles'].notnull() == False].index, inplace = True)


# Supprimer les lignes avec des valeurs manquantes dans la colonne "departement"
df_carb = df_carb.dropna(subset=['Département'])

#affiche les colonnes apres le nettoyage
print("Colonnes après nettoyage : ", df_carb.columns)

# Écrire le resultat dans un autre csv
# filepath = Path('../cleaned_Prix_carburants_France_instantane.csv')  
df_carb.to_csv('../cleaned_Prix_carburants_France_instantane.csv', sep = ';', index=False)