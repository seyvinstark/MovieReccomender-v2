from flask import render_template, redirect, url_for, request, flash
from . import pred
import pandas as pd
from .forms import MovieForm
from flask_login import current_user, login_required
from .. models import Movie, Cart, User


movies = pd.read_csv('app/data/movies.csv')
ratings = pd.read_csv('app/data/ratings.csv')
links = pd.read_csv('app/data/links2.csv')

@pred.route('/get_prediction', methods=['GET','POST'])
def get_prediction():
    #dataset

    return render_template('predict/index.html', title='Our Reccomendation')

@pred.route('/predict_page', methods=['POST','GET'])
@login_required
def predict_page():
    user = User.query.filter_by(userId=current_user.userId).first()
    carts = user.carts.all()
    carts_count = user.carts.count()

    ''' goes to the prediction page '''
    form = MovieForm()

    movies = pd.read_csv('app/data/movies.csv')
    ratings = pd.read_csv('app/data/ratings.csv')
    links = pd.read_csv('app/data/links2.csv')
    if (request.method=='POST' and form.validate_on_submit()):
        #if our form is good
        moviechosen = form.movie_entered.data
        test = movies["title"] == moviechosen
        movies['test'] = test

        #have = movies['test']!=False
        if(movies['test'].any()):# != False):
            flash("we have the movie")
            movie_titles = ['movieId','title']
            df = pd.merge(ratings, movies[movie_titles])
            ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
            #add nmber of ratings in ratings columns
            ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
            #pivot our table
            moviemat = df.pivot_table(index='userId', columns='title',values='rating')
            user_rating = moviemat[moviechosen]
            similar_to_movie = moviemat.corrwith(user_rating)
            corr_to_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
            corr_to_movie.dropna(inplace=True)

            corrs = corr_to_movie.sort_values('Correlation', ascending=False)
            #we remove those with less than 200 reviews
            corrs = corrs.join(ratings['num of ratings'])
            corrs = corrs.join(df['title'])
            prediction = corrs[corrs['num of ratings']>200].sort_values('Correlation', ascending=False)
            datas = prediction['title'].str.split(")", n=2, expand=True)
            #good = prediction.join(df['title'])
            #print(good)
            answer = datas[0]
            final_result = prediction.index.to_list()
            rec = prediction.head()
            pre = prediction.values
            mylist=[]
            mylist.append(prediction)
            #print the predictions
            print(prediction)
            return render_template('predict/index.html',final_result=final_result,mylist=mylist,carts_count=carts_count, form=form,title="These are the resutls",pre=pre, rec = rec)
            #redirect(url_for('pred.predict_page', answer=answer))
        else:
            flash("we dont have the movie Try another one")

    return render_template('predict/index.html',form=form, carts_count=carts_count, title="Reccomendation Page")

