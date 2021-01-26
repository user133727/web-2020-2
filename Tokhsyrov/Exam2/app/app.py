from flask import Flask, render_template, request, url_for, make_response, session, redirect, flash
from flask_login import login_required, current_user
from mysql_db import MySQL
import mysql.connector as connector
from sqlalchemy import Column, ForeignKey, Integer, String  
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData

# login_manager = LoginManager()

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

mysql = MySQL(app)


# from models import Image

from auth import bp as auth_bp, init_login_manager, check_rights

# from api import bp as api_bp

init_login_manager(app)
app.register_blueprint(auth_bp)

# app.register_blueprint(api_bp)




def load_roles():
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT id, name FROM roles2;')
    roles = cursor.fetchall()
    cursor.close()
    return roles

# def load_films():
#     cursor = mysql.connection.cursor(named_tuple=True)
#     cursor.execute('SELECT * FROM films;')
#     films = cursor.fetchall()
#     cursor.close()
#     return films

@app.route('/')
def films():
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM films;')
    films = cursor.fetchall()
    cursor.close()   
    return render_template('index.html', films=films ) 

@app.route('/films/new2')
@login_required
def new2():
    return render_template('films/new2.html', films={})



@app.route('/films/create', methods=['POST'])
@check_rights('new2')
@login_required
def create2():
    
    name = request.form.get('name') or None
    description = request.form.get('description') or None
    year = request.form.get('year') or None
    country = request.form.get('country') or None
    director = request.form.get('director') or None
    actor = request.form.get('actor') or None
    duration = request.form.get('duration') or None
    query = '''
        INSERT INTO films (name, description, year, country, director, actor, duration)
        VALUES ( %s, %s, %s, %s, %s, %s, %s );
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    try:
        cursor.execute(query, (name, description, year, country, director, actor, duration))
    except connector.errors.DatabaseError:
        flash('Введены некорректные данные, ошибка сохранения', 'danger')
        
        films = {
       
            'name': name,
            'description': description,
            'year': year,
            'country': country,
            'director': director,
            'actor': actor,
            'duration': duration
        }
        return render_template('films/new2.html', films=films)
    # добавление данных в таблице
    # Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
    mysql.connection.commit()
    cursor.close()
    flash(f'Фильм {name} был успешно создан.', 'success')
    return redirect(url_for('index'))

@app.route('/films/<int:films_id>')
@login_required
def show2(films_id):
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM films WHERE id = %s;', (films_id,) )
    films = cursor.fetchone()
    return render_template('films/show2.html', films=films)






@app.route('/films/<int:films_id>/edit2')
# @check_rights('edit2')
@login_required   
def edit2(films_id):
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM films WHERE id = %s;', (films_id,))
    # fetchone-вернет одну запись записи (когда много записей fetchmany(fetchall))
    films = cursor.fetchone()
    cursor.close()
    return render_template('films/edit2.html', films=films)







@app.route('/films/<int:films_id>/update2', methods=['POST'])
# @check_rights('edit2')
@login_required
def update2(films_id):
    name = request.form.get('name') or None
    description = request.form.get('description') or None
    year = request.form.get('year') or None
    country = request.form.get('country') or None
    director = request.form.get('director') or None
    actor = request.form.get('actor') or None
    duration = request.form.get('duration') or None
    query = '''
    UPDATE films SET name=%s, description=%s, year=%s, country=%s, director=%s, actor=%s, duration=%s
    WHERE id=%s;
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    try:
        cursor.execute(query, (name, description, year, country, director, actor, duration, films_id))
    except connector.errors.DatabaseError as err:
        flash('Введены некоректные данные. Ошибка сохранения', 'danger')

        films = {
            'id': films_id,
            'name': name,
            'description': description,
            'year': year,
            'country': country,
            'director': director,
            'actor': actor,
            'duration': duration,
        }
        return render_template('films/edit2.html', films=films)
    mysql.connection.commit()
    cursor.close()
    flash(f'Фильм {name} был успешно обновлён', 'success')
    return redirect(url_for('index'))



@app.route('/delete2/<int:films_id>', methods=['POST'])
@check_rights('delete2')
@login_required
def delete2(films_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute('DELETE FROM films WHERE id = %s;', (films_id,))
        except connector.errors.DatabaseError as err:
            flash('Не удалось удалить запись','danger')
            return redirect(url_for('films'))
        mysql.connection.commit()
        flash('Запись была успешно удалена','info')
    return redirect(url_for('index'))

# @app.route('/films')
# def films():
#     return render_template('index.html')

def load_genres():
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT id, name FROM genres;')
    genres = cursor.fetchall()
    cursor.close()
    return genres










@app.route('/')
def index():
    return render_template('index.html')



# рендер таблички
@app.route('/users')
def users():
    cursor = mysql.connection.cursor(named_tuple=True)
    # LEFT OUTER- для записей бещ=з ролей, что б они отображались на странице
    cursor.execute(
        'SELECT users2.*, roles2.name AS role_name FROM users2 LEFT OUTER JOIN roles2 ON users2.role_id=roles2.id;')
    users = cursor.fetchall()
    cursor.close()
    return render_template('users/index.html', users=users)


@app.route('/users/new')
@check_rights('new')
@login_required
def new():
    return render_template('users/new.html', user={}, roles=load_roles())

@app.route('/users/<int:user_id>')
# проверка на аунтификацию пользователя 
@check_rights('show')
@login_required
def show(user_id):
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users2 WHERE id = %s;', (user_id,))
    user = cursor.fetchone()
    cursor.execute('SELECT * FROM roles2 WHERE id = %s;', (user.role_id,))
    role = cursor.fetchone()
    cursor.close()
    return render_template('users/show.html', user=user, role=role)

@app.route('/users/<int:user_id>/edit')
@check_rights('edit')
@login_required
def edit(user_id):
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users2 WHERE id = %s;', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return render_template('users/edit.html', user=user, roles=load_roles())

#Создание юзера через форму
@app.route('/users/create', methods=['POST'])
@check_rights('new')
@login_required
def create():
    login = request.form.get('login') or None
    password = request.form.get('password') or None
    first_name = request.form.get('first_name') or None
    last_name = request.form.get('last_name') or None
    middle_name = request.form.get('middle_name') or None
    role_id = request.form.get('role_id') or None
    query = '''
    INSERT INTO users2 (login, password_hash, first_name, last_name, middle_name, role_id)
    VALUES (%s,SHA2(%s,256),%s,%s,%s,%s)
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    try:
        cursor.execute(query, (login, password, first_name,
                               last_name, middle_name, role_id))
    except connector.errors.DatabaseError:
        flash('Введены некоректные данные. Ошибка сохранения', 'danger')
        user = {
            'login': login,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'role_id': None if role_id == None else int(role_id),
        }
        return render_template('users/new.html', user=user, roles=load_roles())
    mysql.connection.commit()
    cursor.close()
    flash(f'Пользователь {login} был успешно создан', 'success')
    return redirect(url_for('users'))

# ОБНОВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
@app.route('/users/<int:user_id>/update', methods=['POST'])
@check_rights('edit')
@login_required
def update(user_id):
    login = request.form.get('login') or None
    first_name = request.form.get('first_name') or None
    last_name = request.form.get('last_name') or None
    middle_name = request.form.get('middle_name') or None
    role_id = request.form.get('role_id') or None
    query = '''
    UPDATE users2 SET login=%s, first_name =%s,
                     last_name=%s, middle_name=%s, role_id=%s
    WHERE id=%s;
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    try:
        cursor.execute(query, (login, first_name, last_name,
                               middle_name, role_id, user_id))
    except connector.errors.DatabaseError:
        flash('Введены некоректные данные. Ошибка сохранения', 'danger')
        user = {
            'id': user_id,
            'login': login,
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'role_id': None if role_id == None else int(role_id),
        }
        return render_template('users/edit.html', user=user, roles=load_roles())
    mysql.connection.commit()
    cursor.close()
    flash(f'Пользователь {login} был успешно обновлён', 'success')
    return redirect(url_for('users'))


@app.route('/users/<int:user_id>/delete', methods=['POST'])
@check_rights('delete')
@login_required
def delete(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute('DELETE FROM users2 WHERE id = %s;', (user_id,))
        except connector.errors.DatabaseError as err:
            flash('Не удалось удалить запись','danger')
            return redirect(url_for('users'))
        mysql.connection.commit()
        flash('Запись была успешно удалена','info')
    return redirect(url_for('users'))




# @app.route('/images/<image_id>')
# def image(image_id):
#     img = Image.query.get(image_id)
#     if img is None:
#         abort(404)
#     return send_from_directory(app.config['UPLOAD_FOLDER'], img.storage_filename)