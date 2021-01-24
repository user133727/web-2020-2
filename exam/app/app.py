from flask import Flask, session, render_template, url_for, request, make_response, redirect, flash
from flask_login import login_required, current_user
from mysql_db import MySQL
import mysql.connector as connector

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

mysql = MySQL(app)

from auth import bp as auth_bp, init_login_manager, check_rights

init_login_manager(app)
app.register_blueprint(auth_bp)

def load_roles():
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT id, name FROM roles;')
    roles = cursor.fetchall()
    cursor.close()
    return roles

@app.route('/')
def index():
    return render_template('index.html')

################## F I L M S ###########################

@app.route('/films')
def films():
    cursor = mysql.connection.cursor(named_tuple = True)
    cursor.execute('SELECT * FROM films;')
    films = cursor.fetchall()
    cursor.close()
    return render_template('films/index.html', films=films)

@app.route('/films/new')
@login_required
@check_rights('new')
def new_film():
    return render_template('films/new.html', film={}, roles=load_roles())

@app.route('/films/<int:film_id>/show')
def show_film(film_id):
    cursor = mysql.connection.cursor(named_tuple = True)
    cursor.execute('SELECT * FROM films WHERE films.id=%s;', (film_id,))
    films = cursor.fetchone()
    cursor.close()
    return render_template('films/show.html', film=films, roles=load_roles())

@app.route('/films/<int:film_id>/edit')
@login_required
@check_rights('edit')
def edit_film(film_id):
    cursor = mysql.connection.cursor(named_tuple = True)
    cursor.execute('SELECT * FROM films WHERE films.id=%s;', (film_id,))
    films = cursor.fetchone()
    cursor.close()
    return render_template('films/edit.html', film=films, roles=load_roles())

@app.route('/films/create', methods=['POST'])
@login_required
@check_rights('new')
def create_film():
    title = request.form.get('title')
    description = request.form.get('description')
    production_year = request.form.get('production_year')
    type_id = request.form.get('type_id')
    country = request.form.get('country')
    producer = request.form.get('producer')
    scenarist = request.form.get('scenarist')
    actors = request.form.get('actors')
    time_in_m = request.form.get('time_in_m')
    poster_id = request.form.get('poster_id')
    query = '''
        INSERT INTO films (title, description, type_id, production_year, country, producer, scenarist, actors, time_in_m, poster_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    cursor = mysql.connection.cursor(named_tuple = True)
    try:
        cursor.execute(query, (title, description, type_id, production_year, country, producer, scenarist, actors, time_in_m, poster_id))
    except connector.errors.DatabaseError:
        flash('Input data error!', 'danger')
        films = {
            'title': title,
            'description': description,
            'type_id': type_id,
            'production_year': production_year,
            'country': country,
            'producer': producer,
            'scenarist': scenarist,
            'actors': actors,
            'time_in_m': time_in_m,
            'poster_id': poster_id
        }
        return render_template('films/new.html', films=films)
    mysql.connection.commit()
    cursor.close()
    flash('Success!', 'success')
    return redirect(url_for('films'))

@app.route('/films/<int:film_id>/update', methods=['POST'])
@login_required
@check_rights('edit')
def update_film(film_id):
    title = request.form.get('title')
    description = request.form.get('description')
    type_id = request.form.get('type_id')
    production_year = request.form.get('production_year')
    country = request.form.get('country')
    producer = request.form.get('producer')
    scenarist = request.form.get('scenarist')
    actors = request.form.get('actors')
    time_in_m = request.form.get('time_in_m')
    poster_id = request.form.get('poster_id')
    query = '''
        UPDATE films SET title=%s, description=%s, type_id=%s, production_year=%s, country=%s,
                         producer=%s, scenarist=%s, actors=%s, time_in_m=%s, poster_id=%s
        WHERE id=%s;
    '''
    cursor = mysql.connection.cursor(named_tuple = True)
    try:
        cursor.execute(query, (title, description, type_id, production_year, country, producer, scenarist, actors, time_in_m, poster_id, film_id))
    except connector.errors.DatabaseError:
        flash('Input data error!', 'danger')
        films = {
            'title': title,
            'description': description,
            'type_id': type_id,
            'production_year': production_year,
            'country': country,
            'producer': producer,
            'scenarist': scenarist,
            'actors': actors,
            'time_in_m': time_in_m,
            'poster_id': poster_id
        }
        return render_template('films/edit.html', films=films)
    mysql.connection.commit()
    cursor.close()
    flash('Success!', 'success')
    return redirect(url_for('films'))

@app.route('/films/<int:film_id>/delete', methods=['POST'])
@login_required
@check_rights('delete')
def delete_film(film_id):
    with mysql.connection.cursor(named_tuple = True) as cursor:
        try:
            cursor.execute('DELETE FROM films WHERE id=%s;', (film_id,))
        except connector.errors.DatabaseError:
            flash('Failed to delete movie!', 'danger')
            return redirect(url_for('films'))
        mysql.connection.commit()
        flash('Movie has been removed!', 'success')  
    return redirect(url_for('films'))      

################## U S E R S ###########################

@app.route('/users')
def users():
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute(
        'SELECT users.*, roles.name AS role_name FROM users LEFT OUTER JOIN roles on users.role_id = roles.id;')
    users = cursor.fetchall()
    cursor.close()
    return render_template('users/index.html', users=users)

@app.route('/users/<int:user_id>')
@check_rights('show')
@login_required
def show(user_id):
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users Where id = %s;', (user_id,))
    user = cursor.fetchone()
    cursor.execute('SELECT * FROM roles Where id = %s;', (user.role_id,))
    role = cursor.fetchone()
    cursor.close()
    return render_template('users/show.html', user=user, role=role)