from functools import wraps
from flask import Flask,Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from app import mysql
from users_policy import UsersPolicy

bp = Blueprint('auth', __name__, url_prefix='/auth')


class User(UserMixin):
    def __init__(self, user_id, login, role_id):
        super().__init__()
        self.id = user_id
        self.login = login 
        self.role_id = role_id
# проверка на выполнение ( может ли пользователь выполнять действие action -действие, record- запись)
    def can(self, action, record=None):
        policy =  UsersPolicy(record=record)
        #getattr позволяет по названию атрибуда получить значение или если нет то none
        method = getattr(policy, action, None)
        if method:
            return method()
        return False

# проверка записи
def load_record(user_id):
    if user_id is None:
        return None
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users2 WHERE id = %s;', (user_id,))
    record = cursor.fetchone()
    cursor.close()
    return record

# функция  для проверки прав, возвращающаяя декаратор
def check_rights(action):
    def decorator(func):
        #что бы имя функции не заменилось и док был не из другой функции  
        @wraps(func)
        # функция обертки в ней проверяются есть ли право 
        def wrapper(*args, **kwargs):
            # загружаем запись ( загрузка записей всегда по user_id)
            record = load_record(kwargs.get('user_id'))
            # если у пользователя недостаточно прав 
            if not current_user.can(action, record=record):
                flash('У вас недостаточно прав для доступа к данной странице', 'danger')
                # возвращаем на главную страницу 
                return redirect(url_for('index'))
                # возвращаем  исходную  функцию с аргументами, переданными в функцтию обертку 
            return func(*args, **kwargs)
        return wrapper
    return decorator



def load_user(user_id):
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users2 WHERE id = %s;', (user_id,))
    db_user = cursor.fetchone()
    cursor.close()
    if db_user:
        return User(user_id=db_user.id, login=db_user.login, role_id=db_user.role_id)        
    return None   
 
@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        remember_me = request.form.get('remember-me') == 'on'
        if login and password:
                cursor =  mysql.connection.cursor(named_tuple=True)
                cursor.execute('SELECT * FROM users2 WHERE login = %s AND password_hash = SHA2(%s, 256);', (login, password))
                db_user = cursor.fetchone()
                cursor.close()
                if db_user:
                    user = User(user_id=db_user.id, login=db_user.login, role_id=db_user.role_id) 
                    login_user(user, remember=remember_me)

                    flash('Вы успешно аутентифицированы', 'success')
                    next = request.args.get('next')
                    return redirect(next or url_for('index'))

        flash('Введены неверные логин и/или пароль.', 'danger')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view= 'auth.login'
    login_manager.login_message= 'Для доступа необходимо пройти процедуру аутентификации'
    login_manager.login_message_category= 'warning'
    login_manager.user_loader(load_user)