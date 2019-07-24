from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import GenreForm, MovieForm
from .. import db
from ..models import Genre, Movie, User, Cart


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)


# Category Views to list all genres in the database
@admin.route('/genres', methods=['GET', 'POST'])
@login_required
def list_genres():
    """
    List all genres
    """
    check_admin()

    genres = Genre.query.all()

    return render_template('admin/genres/genres.html',
                           genres=genres, title="genres")


@admin.route('/genres/add', methods=['GET', 'POST'])
@login_required
def add_genre():
    """
    Add a genre to the database
    """
    check_admin()

    add_genre = True

    form = GenreForm()
    if form.validate_on_submit():
        genre = Genre(name=form.name.data,
                                description=form.description.data)
        try:
            # add genre to the database
            db.session.add(genre)
            db.session.commit()
            flash('You have successfully added a new genre.')
        except:
            # in case genre name already exists
            flash('Error: genre name already exists.')

        # redirect to genres page
        return redirect(url_for('admin.list_genres'))

    # load genre template
    return render_template('admin/genres/genre.html', action="Add",
                           add_genre=add_genre, form=form,
                           title="Add genre")


@admin.route('/genres/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_genre(id):
    """
    Edit a genre
    """
    check_admin()

    add_genre = False

    genre = Genre.query.get_or_404(id)
    form = GenreForm(obj=genre)
    if form.validate_on_submit():
        genre.name = form.name.data
        genre.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the genre.')

        # redirect to the genres page
        return redirect(url_for('admin.list_genres'))

    form.description.data = genre.description
    form.name.data = genre.name
    return render_template('admin/genres/genre.html', action="Edit",
                           add_genre=add_genre, form=form,
                           genre=genre, title="Edit genre")


@admin.route('/genres/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_genre(id):
    """
    Delete a genre from the database
    """
    check_admin()

    genre = Genre.query.get_or_404(id)
    db.session.delete(genre)
    db.session.commit()
    flash('You have successfully deleted the genre.')

    # redirect to the genres page
    return redirect(url_for('admin.list_genres'))

    return render_template(title="Delete genre")


# Role Views

'''
@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")



'''

# User Views

@admin.route('/Users')
@login_required
def list_users():
    """
    List all Users
    """
    check_admin()
    

    users = User.query.all()
    return render_template('admin/users/users.html',
                           users=users, title='Users')


'''
@admin.route('/users/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_user(id):
    """
    Assign a genre and a role to an User
    """
    check_admin()

    user = User.query.get_or_404(id)

    # prevent admin from being assigned a genre or role
    if user.is_admin:
        abort(403)

    form = UserAssignForm(obj=user)
    if form.validate_on_submit():
        user.genre = form.genre.data
        user.role = form.role.data
        db.session.add(user)
        db.session.commit()
        flash('You have successfully assigned a genre and role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_users'))

    return render_template('admin/users/user.html',
                           user=user, form=form,
                           title='Assign User')


'''
























# View for adding the movie in the database

@admin.route('/movie/add', methods=['GET', 'POST'])
@login_required
def add_movie():
    """
    Add a movie to the database
    """
    check_admin()

    add_movie = True

    form = MovieForm()
    if form.validate_on_submit():
        movie = Movie(title=form.name.data,
                    genre=form.genre.data,
                    rating=form.rating.data,
                    description=form.description.data)

        try:
            # add movie to the database
            db.session.add(movie)
            db.session.commit()
            flash('You have successfully added a new movie.')
        except:
            # in case role name already exists
            flash('Error: movie name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_movies'))

    # load role template
    return render_template('admin/movies/movie.html', add_movie=add_movie,
                           form=form, title='Add Movie')








# genre Views to list all genres in the database
@admin.route('/movies')
@login_required
def list_movies():
    check_admin()
    """
    List all movies
    """
    movies = Movie.query.all()
    return render_template('admin/movies/admin_movies.html',
                           movies=movies, title='Movies list')






# genre Views to list all genres in the database
@admin.route('/movies/orders')
@login_required
def orders():
    check_admin()
    """
    List all movies
    """
    movies = Cart.query.all()
    return render_template('admin/movies/orders.html',
                           movies=movies, title='Movies list')






# genre Views to list all genres in the database
@admin.route('/movies/orders/approve/<int:cartId>', methods=['GET', 'POST'])
@login_required
def approve(cartId):
    check_admin()
    """
    List all movies
    """
    #movies = Cart.query.all()
    cart = Cart.query.get_or_404(cartId)

    cart.status = 1
    db.session.commit()
    flash('You have successfully approved the order.')
    return redirect(url_for('admin.orders'))



