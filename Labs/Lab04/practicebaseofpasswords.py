from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("600x600")
root.title("Необходимо авторизироваться в системе:")

def registration():
    text = Label(text = "Для входа в систему необходимо зарегистрироваться")
    text_login = Label(text = "Придумайте логин:")
    registr_login = Entry()
    text_password1 = Label(text = "Придумайте пароль: ")
    registr_password1 = Entry()
    text_password2 = Label(text = "Введите пароль ещё раз: ")
    registr_password2 = Entry(show = "*")
    button_registr = Button(text = "Зарегистрироваться", command = lambda: save())
    text.pack()
    text_login.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()] = registr_password1.get()
        f = open("base.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text = "Теперь вы можете авторизироваться в системе")
    text_enter_login = Label(text = "Введите ваш логин:")
    enter_login = Entry()
    text_enter_pass = Label(text = "Введите ваш пароль:")
    enter_password = Entry(show = "*")
    text_log.pack()
    button_login = Button(text = "Войти", command = lambda: log_pass())
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_login.pack()

    def log_pass():
        f = open("base.txt","rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен")
            else:
                messagebox.showerror("Ошибка, вы ввели неверный логин или пароль!")
        else:
            messagebox.showerror("Ошибка, вы ввели неверный логин!")

registration()
root.mainloop()
