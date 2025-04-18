import pandas as pd


df = pd.read_excel('creepypastas.xlsx')


average_rating = df['average_rating'].mean()
print(average_rating)