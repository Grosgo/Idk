import pandas as pd 
import numpy as np 
pd.set_option('display.max_columns', None)
df = pd.read_csv("C:/Users/AS TECH/Desktop/Data Sets/Movies - movies.csv")




df['YEAR'] = df['YEAR'].str.replace('[^\d]','',regex=True)
df['YEAR'] = df['YEAR'].apply(lambda x: str(x)[0:4] + '-' + str(x)[4:8] if len(str(x))>4 else str(x))
df.fillna('',inplace=True)
df[['DIRECTORS' ,'ACTORS']] = df['STARS'].str.split('|',n=1,expand=True)
df.drop(columns=['STARS'], inplace=True)
df.drop_duplicates(inplace=True)
df['ACTORS'] = df['ACTORS'].str.replace('\n','')
df['ACTORS'] = df['ACTORS'].str.replace('Stars:','')
df['DIRECTORS'] = df['DIRECTORS'].str.replace('\n','')
df['DIRECTORS'] = df['DIRECTORS'].str.replace('Director:','')
df['DIRECTORS'] = df['DIRECTORS'].str.replace('Directors:','')

df = df.reset_index(drop=True)

print(df.head())
