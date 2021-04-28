import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv')
# # print(df)
# # print(df.columns)

# movie = df['movie_title'].value_counts()
# # print(movie.head(10))

# df_gross = df.groupby('director_name')['gross'].sum()

# df_gross = df_gross.sort_values(ascending = False)

# print(df_gross.head(10))

# print('______________________________________________')

# df_num = df['director_name'].value_counts()

# print(df_num.head(10))


# df_year = df.groupby(['title_year'])['movie_title'].count()


# print('______________________________________________')


# print(df_year.head(10))


# langs = df['language'].unique()
# print(langs)

