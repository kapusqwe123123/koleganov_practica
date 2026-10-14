import tkinter as tk
from tkinter import messagebox
from testik2 import *

CURRENT_USER = None
CURRENT_EDIT = None
ENTRY_LOGIN = None

BG = "#f9f1e5"
FIELD_BG = "#ffffff"
FIELD_FG = "#22262b"

FONT_TITLE = ("Arial", 16, "bold")
FONT_LABEL = ("Arial", 11, "bold")
FONT_BUTTON = ("Arial", 12, "bold")

root = tk.Tk()
root.title("Окно входа")
root.geometry("720x640")

container = tk.Frame(root, padx=30, pady=25)
container.pack(expand=True)

def clear_screen():
    for w in container.winfo_children():
        w.destroy()

def make_title(text):
    return tk.Label(container, text=text, bg=BG, fg=FIELD_FG, font=FONT_TITLE)

def make_label(text):
    return tk.Label(container, text=text, bg=BG, fg=FIELD_FG, font=FONT_LABEL, anchor="w")

def make_entry(password=False):
    entry = tk.Entry(container, font=FONT_BUTTON, bg=FIELD_BG, fg=FIELD_FG,
                     insertbackground=FIELD_FG, relief="solid", borderwidth=1)
    if password:
        entry.configure(show="*")
    return entry

def make_button(text, command, parent=None):
    host = container if parent is None else parent
    return tk.Button(host, text=text, command=command, font=FONT_BUTTON)

def window_login():
    clear_screen()

    tk.Label(container, text="Вход", font=("Arial", 20)).pack(pady=(0, 20))

    tk.Label(container, text="Логин").pack(anchor="w")

    login = tk.Entry(container, width=32)
    login.pack(pady=(4, 12))

    tk.Label(container, text="Пароль").pack(anchor="w")
    password = tk.Entry(container, width=32, show="*")
    password.pack(pady=(4, 18))

    tk.Button(container, text="Войти", command = admin_window, width=20).pack()
    user = find_user(login,password)
    
    if user["role"] == "Администратор":
        admin_window()
    else:
        add_user_window()

def admin_window() :
    clear_screen()
    row = tk.Frame(container, bg=BG)
    row.pack(fill="x")
    tk.Label(container, text="Окно администратора", font=("Arial", 20)).pack(pady=(10,20),padx=10)
    tk.Button(container, text="Выйти", command=window_login, width=20).pack(side="left", padx=(0, 6))
    tk.Button(container, text="Добавить пользователя", command=add_user_window, width=20).pack(side="left", padx=(0, 6))
    tk.Button(container, text="Изменить пользователя", command=change_user, width=20).pack(side="left", padx=(0, 6))


def add_user_window():
    clear_screen()
    row = tk.Frame(container, bg=BG)
    row.pack(fill="x")
    tk.Label(container, text="Добавить пользователя",font=("Arial", 20)).pack(pady=(0, 20))
    username_entry = tk.Entry(container, width=32)
    username_entry.pack(pady=(4, 12))
    tk.Button(container, text="Добавить", command=admin_window, width=20).pack()
    tk.Button(container, text="Отмена", command=admin_window, width=20).pack()



def change_user():
    clear_screen()
    row = tk.Frame(container, bg=BG)
    row.pack(fill="x")

    tk.Label(container, text="Изменить пользователя", font=("Arial", 20)).pack(pady=(0, 20))
    tk.Button(container, text="Отмена", command=admin_window, width=20).pack()

window_login()
root.mainloop()
