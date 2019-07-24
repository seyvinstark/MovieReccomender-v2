from flask import abort, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from .. import db
import pandas as pd
from .. models import Movie, Cart, User
from . import home
from flask import jsonify
from .. predict import forms
import nexmo


import os

import stripe

client = nexmo.Client(key='e88f8d53', secret='w7j2m7zksG7RPPVc')


stripe_keys = {
  'secret_key': os.environ['STRIPE_SECRET_KEY'],
  'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']



#export STRIPE_PUBLISHABLE_KEY=pk_test_l8INkseWioNZqSRgs78wq7AG
#export STRIPE_SECRET_KEY=sk_test_OXZNLFLMjrg0Lc2mSnp5htQw


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    
    user = User.query.filter_by(username=current_user.username).first()
    carts = user.carts.all()
    carts_count = user.carts.count()
    """

    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    user = User.query.filter_by(username=current_user.username).first()
    carts = user.carts.all()
    carts_count = user.carts.count()
    return render_template('home/dashboard.html',
                            carts_count=carts_count, title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    user = User.query.filter_by(username=current_user.username).first()
    carts = user.carts.all()
    carts_count = user.carts.count()
    return render_template('home/admin_dashboard.html',
                            carts_count=carts_count, title="Dashboard")





# Views to list all genres in the database for the non admin users
@home.route('/moviesShop')
@login_required
def list_movies_shop():
    """
    List all movies
    """
    '''
    user = User.query.filter_by(username=current_user.username).first()
    carts = user.carts.all()
    carts_count = user.carts.count()
    movies = Movie.query.all()
    return render_template('home/movies_shop.html',
                           movies=movies, carts_count=carts_count, title='Movies shop list')

    '''
    user = User.query.filter_by(userId=current_user.userId).first()
    carts = user.carts.all()
    carts_count = user.carts.count()


    movies = pd.read_csv('app/data/movies.csv')
    ratings = pd.read_csv('app/data/ratings.csv')
    links = pd.read_csv('app/data/links2.csv')
    col=['movieId']
    df = pd.merge(movies,links, on=col).head(20)
    data = df.values
    res = df.to_json()
    #movie_list = df['imdbId']
    return render_template('home/movies_shop.html',answer=jsonify(res),result=res,df=df, 
                            dataframe=df.to_html(),data=data, carts_count=carts_count)


# Views to give all the details of one specific movie
@home.route('/movie_details/<int:id>')
@login_required
def MovieDetails(id):
    """
    List all movies
    """
    user = User.query.filter_by(username=current_user.username).first()
    carts = user.carts.all()
    carts_count = user.carts.count()
    movie = Movie.query.get_or_404(id)
    return render_template('home/movie_details.html',
                           movie=movie, carts_count=carts_count, title='Movies details')



#data = df.movieId[1]


# Views to give all the details of one specific movie
@home.route('/movie_details_info/<int:movieId>', methods=['GET', 'POST'])
@login_required
def MovieDetailsInfo(movieId):
    """
    List all movies
    
    user = User.query.filter_by(username=current_user.username).first()
    carts = user.carts.all()
    carts_count = user.carts.count()
    movie = Movie.query.get_or_404(id)

    movies = pd.read_csv('app/data/movies.csv')
    ratings = pd.read_csv('app/data/ratings.csv')
    links = pd.read_csv('app/data/links2.csv')
    col=['movieId']
    df = pd.merge(movies,links, on=col).head(20)
    data_detail = df.movieId
    res = df.to_json()

    user_movie = movieId

    movies =    Cart(
                        userId = current_user.id,
                        movieId = user_movie
                    )

    db.session.add(movies)
    db.session.commit()
    """
    
    movies = pd.read_csv('app/data/movies.csv')

    user_movie = movieId
    movies =    Cart(
                        userId = current_user.userId,
                        movieId = user_movie
                    )

    db.session.add(movies)
    db.session.commit()
    flash("Movies was added to cart successfully, Add more movies or Checkout")

    return redirect(url_for('home.list_movies_shop'))
    #return render_template('frank/movie_info.html', one=one)
     #                      movie=movie, carts_count=carts_count, data_detail=data_detail, title='Movies details')







@home.route('/addToCart/<int:movieId>', methods=['GET', 'POST'])
def addToCart(movieId):
    """
    Allow the user to add movies in the cart
    """
    user = User.query.filter_by(username=current_user.username).first()
    carts = user.carts.all()
    carts_count = user.carts.count()
    movieInCart = Movie.query.get_or_404(movieId)
    movies = Cart (
            userId = current_user.id,
            movieId = movieInCart.movieId
            )
    db.session.add(movies)
    db.session.commit()
    flash("You have added move in the cart!")
    return redirect(url_for('home.list_movies_shop'))




@home.route('/user/<int:userId>/cart/', methods=['GET', 'POST'])
def userCart(userId):
    user = User.query.filter_by(userId=current_user.userId).first()
    carts = user.carts.all()
    carts_count = user.carts.count()

    #return render_template('home/movie_details.html')
    return render_template('home/user_cart.html',
                            user=user, carts=carts, carts_count=carts_count,
                            key=stripe_keys['publishable_key'])


@home.route('/charge', methods=['POST'])
def charge():

    # amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='sample@customer.com',
        source=request.form['stripeToken']
    )

    stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Lamperouge Charge'
    )

    client.send_message({
        'from': 'Lamperouge',
        'to': '250783751728',
        'text': 'Your order has been confirmed - ',
    })

    return render_template('home/charge.html', amount=amount)
