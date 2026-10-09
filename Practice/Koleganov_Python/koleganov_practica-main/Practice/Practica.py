import tkinter as tk
from tkinter import *
from tkinter import messagebox

BG = "#f9f1e5"
FIELD_BG = "#ffffff"
FIELD_FG = "#22262b"

PRIMARY_BG = "#1e5fd0"
PRIMARY_FG = "#ffffff"
SECOND_BG = "#e5e7eb"
SECOND_FG = "#111827"

FONT_TITLE = ("Arial", 16, "bold")
FONT_LABEL = ("Arial", 11, "bold")
FONT_BUTTON = ("Arial", 12, "bold")

root = tk.Tk()
root.title("Учебное приложение")
root.geometry("450x450")
root.configure(bg="#f9f1e5")
label = tk.Label(root, text="Привет")
label.pack()
container = tk.Frame(root, bg=BG)
container.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(container, text="Логин").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(container).grid(row=0, column=1, sticky="ew", pady=5)

tk.Label(container, text="Пароль").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(container, show="*").grid(row=1, column=1, sticky="ew", pady=5)

tk.Button(container, text="Войти").grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

container.columnconfigure(1, weight=1)

entry = tk.Entry (root)
entry.pack()

text = entry .get()
entry.delete (0,"end")
entry.insert(0,"admin")

def open_admin ():
    print("Открыли админку")

btn = tk.Button(root, text ="Админка", command=open_admin)
bad = tk.Button(root, text="Админка",command=open_admin)

messagebox.showinfo("Готово", "Пользователь добавлен")
messagebox.showwarning("Внимание", "Заполните все поля")
messagebox.showerror("Ошибка", "Неверный логин или пароль")

if messagebox.askyesno("Выход","Выйти из программы"):
    root.destroy()

tree = ttk.Treeview(container, columns=("login", "role", "locked"),
                    show="headings", height=8)

tree.heading ("login", text="Логин")
tree.heading("role", text="Роль")
tree.heading("locked", text="Заблокирован")

tree.column("login", width=180, anchor="w")
tree.column("role", width=160, anchor="w")
tree.column("locked", width=120, anchor="center")

tree.insert("", "end", values=("admin", "Администратор", "нет"))
tree.pack(fill="both", expand=True)

selected = tree.selection()
if not selected:
    messagebox.showwarning("Внимание", "Сначала выберите строку.")
else:
    login = tree.item(selected[0])["values"][0]


root.mainloop()

