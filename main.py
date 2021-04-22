import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv')
print(df)
print(df.columns)
movies = df['movie_title']
print(movies.head(10))

rating = df[df['imdb_score']>7.5]
print(rating)