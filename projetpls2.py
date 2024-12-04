
import pandas as pd
import numpy as np
import matplotlib as plt
data_dir = "C:/Users/celin/Documents/M2/PLS2"

data = pd.read_csv(data_dir+"/cwurData.csv", sep=",")

#Affichage 5 premières lignes et infos
print(data.head())
print(data.info())

#Statistique descriptive
print(data.describe())

#Vérification de données manquantes 
print(data.isnull().sum())


#Moyenne des scores par pays et ordination par ordre croissant
print(data.groupby('country')['score'].mean().sort_values(ascending=False))


