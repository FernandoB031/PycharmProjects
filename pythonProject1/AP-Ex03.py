import pandas as pd
files_store = 'D:\Estudos\Faculdade Uninter - Redes de computadores\C-Fase 2 2022\Linguagem de programação\Aula 07 - Atividade Prática\Stores.csv'
df = pd.read_csv(files_store, sep=',')
df.head()

df.columns.values