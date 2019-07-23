from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    """
    Create users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    userId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    is_admin = db.Column(db.Boolean, default=False)
    carts = db.relationship('Cart', backref='user', lazy='dynamic')


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


    def get_id(self):
           return (self.userId)



# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Genre(db.Model):
    """
    Create a Category or genre table
    """
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True)
    movies = db.Column(db.String(200))
    users = db.relationship('User', backref='genre', lazy='dynamic')

    def __repr__(self):
        return '<Genre: {}>'.format(self.title)

 

class Movie(db.Model):
    """
    Create an movies table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'movies'

    movieId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), index=True, unique=True)
    genre = db.Column(db.String(60), index=True, unique=True)
    #arts = db.relationship('Cart')

    def __repr__(self):
        return '<Movie: {}>'.format(self.name)


class Ratings(db.Model):
    '''Ratings table
    '''
    __tablename__='ratings'

    ratingId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('users.userId'))
    movieId = db.Column(db.Integer, db.ForeignKey('movies.movieId'))
    rating = db.Column(db.Float)
    timestamp = db.Column(db.TIMESTAMP)

class Cart(db.Model):
    __tablename__ = 'carts'

    cartId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('users.userId'))
    movieId = db.Column(db.Integer)

    def __repr__(self):
        return '<Cart: {}>'.format(self.cartId)
