import tkinter as tk
from tkinter import messagebox
from tkinter import *

CURRENT_USER = None

root=tk.Tk()
root.title("Учебное приложение")
root.geometry("800x600")
root.configure(bg="#f9f1e5")

container=tk.Frame (root,bg="#f9f1e5")
container.pack(fill="both",expand=True,padx=20,pady=20) 

BG = "#f9f1e5"
FIELD_BG = "#ffffff"
FIELD_FG = "#000000"

FONT_TITLE = ("Arial", 16, "bold")
FONT_LABEL = ("Arial", 11, "bold")
FONT_BUTTON = ("Arial", 12, "bold")

def clear_screen():
    for w in container.winfo_children():
        w.destroy()

def make_title(text):
    return tk.Label(container,text=text,bg=BG,fg="#000000",font=FONT_TITLE)

def make_label(text):
    return tk.Label(container,text=text,bg=BG,fg="#000000",
                    font=FONT_TITLE,anchor="w")

def make_entry(password =False):
    entry=tk.Entry(container,font=FONT_BUTTON,bg=FIELD_BG,fg=FIELD_FG ,insertbackground=FIELD_FG,relief="solid",borderwidth=1)
    if password:
        entry.configure(show="*")
    return entry
    
def make_button (text,command,parent=None):
    host= container if parent is None else parent
    return tk.Button (host,text=text,command=command,font=FONT_BUTTON)

def try_login(login,password):
    global CURRENT_USER
    login= login.strip()
    password=password.strip()
    if not login or not password:
        messagebox.showwarning("Внимание","Заполните логин или пароль.")
        return
    user = find_user (login,password)
    if user in None:
        messagebox.showerror("Ошибка входа","Вы ввели неверный логин или пароль."
                             "Пожалуйста проверьте еще раз свои данные")
        return
    CURRENT_USER=user
    messagebox.showinfo("Авторизация", "Вы успешно авторизовались")
    if user ["role"]== "Администратор":
        open_admin()
    else:
        open_user()

def open_login():
    clear_screen()
    make_title("Вход в систему").pack(pady=(0,10))

    make_label("Логин").pack(fill="x")
    entry_login=make_entry()
    entry_login.pack (fill="x", pady=(0,8))
    make_label("Пароль").pack(fill="x")
    entry_pass = make_entry(password=True)
    entry_pass.pack(fill="x",pady=(0,10))

    make_button("Войти",
                lambda:try_login(entry_login.get(),entry_pass.get())
                ).pack(fill="x",ipady=6)
    
def open_admin():
    clear_screen()
    make_title("Панель администратора").pack(pady=(0,10))
    make_label(f"Вы вошли как:{CURRENT_USER['login']}").pack(fill="x",pady=(0,10))
    make_button("Выйти",open_login).pack (ipadx=24,ipady=4)

def change_user():
    tk.Label(container, text="Измените пользователя")


def open_user():
    clear_screen()
    make_title("Рабочее место пользователя").pack(pady=(0,10))
    make_label(f"Вы вошли как:{CURRENT_USER['login']}").pack(fill="x",pady=(0,6))
    make_label(f"Вы вошли как:{CURRENT_USER['role']}").pack(fill="x",pady=(0,20))
    make_button("Выйти",open_login).pack (ipadx=24,ipady=4)
 
open_login()
root.mainloop()