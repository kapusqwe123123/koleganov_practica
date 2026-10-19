# USERS = [
#     {"login": "admin", "password" : "admin", "role": "Администратор","full_name":"Администратор системы","locked":False,"attempts": 0},
#         {"login": "Ivanov", "password" : "123", "role": "Администратор","full_name":"Иванов Иван","locked":True,"attempts": 3},
#             {"login": "petrov", "password" : "qwerty", "role": "Администратор","Петров Петр":"Администратор системы","locked":False,"attempts": 0},
# ] 

DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/nmo"
engine = create_engine("sqlite:///app.db", echo=False)

def _to_dict(user):
    if user is None:
        return None
    return {
        "id": user.id,
        "login": user.login,
        "password" : user.password, 
        "role" : user.role,
        "full_name": user.full_name,
        "locked" : bool(user.is_locked),
        "attempts" : user.attempts,
    }

"""""""Возвращает список всех пользователей"""""""
def all_users():
    with Session(engine) as session:
        users = session.scalars(select(User).order_by(User.id)).all()
        return [_to_dict(u) for u in users]
    
    """""""Ищет пользователя по логину и паролю,если нет -None"""""""
    
def find_user(login,password):
    with Session(engine) as session:
        user= session.scalars(
            select(User).where(User.login == login,User.password == password)
        ).first()
        return _to_dict(user)
    
    """""""Возвращает пользователя по логину"""""""
def user_by_login(login):
    with Session(engine) as session:
        user=session.scalars(select(User).where(User.login==login)).first()
        return _to_dict(user)
    
    """""""Есть ли пользователь с таким логином"""""""
def login_exists(login):
    return user_by_login(login) is not None

"""""""Добавляет нового пользователя"""""""

def add_user(login,password,role,full_name):
    with Session(engine) as session:
        session.add(
            User(
                login-login,
                password=password,
                full_name=full_name,
                role=role,
                is_locked=0,
                attempts=0,
                is_active=1,
            )
        )
        session.commit()       