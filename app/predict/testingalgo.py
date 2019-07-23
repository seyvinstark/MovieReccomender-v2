import pandas as pd

movies = pd.read_csv('../data/movies.csv')
ratings = pd.read_csv('../data/ratings.csv')#userid movieid rating timestamp
links = pd.read_csv('../data/links2.csv')

#print(links.head())
movie_titles= ['movieId','title']
#df = movieid* userid title rating timestamp
df = pd.merge(ratings, movies[movie_titles], on='movieId')
#ratings has title and average rating per title
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
#add a ratings col with number of ratings
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())


#building a pivot table row userid and col title,movieId
moviemat = df.pivot_table( index='userId',columns='title',values='rating')

moviechosen ='Matrix, The (1999)'

user_rating = moviemat[moviechosen]#users who rated that specific movie

#similar movies to that rated movie
similar_to_movie = moviemat.corrwith(user_rating)

corr_to_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
corr_to_movie.dropna(inplace=True)

corrs = corr_to_movie.sort_values('Correlation', ascending=False)

#we filter out those with less  than 100 reviews
corrs = corrs.join(ratings['num of ratings'])
corrs = corrs.join(df['title'])
prediction = corrs[corrs['num of ratings']>200].sort_values('Correlation', ascending=False)

#print(prediction['title'].head(10))
datas = prediction['title'].str.split(")",n=2, expand=True)
answer = datas[0]
print(answer)
#