import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

movies = pd.read_csv('movie_data.csv')

movies.replace(['?', 'NA', ''], np.nan, inplace=True)
movies = movies.dropna()

genre_ratings = movies.groupby('Genre')['IMDB_Rating'].mean()

label_genre = LabelEncoder()
label_director = LabelEncoder()
movies['Genre'] = label_genre.fit_transform(movies['Genre'])
movies['Director'] = label_director.fit_transform(movies['Director'])

scaler = MinMaxScaler()
movies[['Budget', 'Duration']] = scaler.fit_transform(movies[['Budget', 'Duration']])

movies.to_csv('cleaned_movies.csv', index=False)
print("Data wrangling complete!")