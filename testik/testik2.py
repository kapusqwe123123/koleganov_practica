USERS = [
   {"login":"admin","password": "admin","role":"Администратор"},
   {"login":"user","password": "user","role":"Пользователь"},
]

def find_user(login, password):
    for u in USERS:
        if u["login"] == login and u["password"] == password:
            return u
    return None