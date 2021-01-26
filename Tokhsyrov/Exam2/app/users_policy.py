from flask_login import current_user
# по таблице ролей 

ADMIN_ROLE_ID = 1
USER_ROLE_ID = 2
MODERATOR_ROLE_ID = 3

#  является ли пользователь админом 
# def is_admin():
#     return current_user.role_id == ADMIN_ROLE_ID

def is_admin():
    
    return current_user.role_id == ADMIN_ROLE_ID

def is_moderator():
    
    return current_user.role_id == MODERATOR_ROLE_ID

def is_user():
   
   
    return current_user.role_id == USER_ROLE_ID




#разграничения действий пользлватля, допуск к определенной функциональности 
class UsersPolicy:

    def __init__(self, record=None):
        self.record = record
#редактирование ( проверяем являетяс ли текущий пользовател тем, кого пытаются отредактировать)
    def edit(self):
        is_editing_user = current_user.id == self.record.id
        return is_admin() or is_editing_user
# права на просмор ( либо может смотреть подробную инфу о себе, либо если админ, то любую запись)
    def show(self):
        is_showing_user = current_user.id == self.record.id
        return is_admin() or is_showing_user
# создает запись только админ    
    def new(self):
        return is_admin()
# удаляет только админ, возвращает тру или фолз 
    def delete(self):
        return is_admin()

    # def assign_role(self):
    #     return is_admin()

    def edit2(self):
        return is_admin() or is_moderator()

# # права на просмор ( либо может смотреть подробную инфу о себе, либо если админ, то любую запись)
#     def show2(self):
#         is_showing2_user = current_user.id == self.record.id
#         return is_admin() or is_showing2_user
# # создает запись только админ    
#     def new2(self):
#         return is_admin()
# # удаляет только админ, возвр
#     def delete2(self):
#         return is_admin()


    def show2(self):
        return is_admin() or is_user() or is_moderator()
# создает запись только админ    
    def new2(self):
        return is_admin()
# удаляет только админ, возвр
    def delete2(self):
        return is_admin()