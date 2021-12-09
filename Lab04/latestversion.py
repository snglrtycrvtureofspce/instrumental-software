import random
import os
from colorama import *
import datetime
from time import sleep
from tkinter import*
from tkinter import messagebox
import pickle
import subprocess

init()

def cls():
    subprocess.call("cls", shell=True)

date = datetime.datetime.now()

spisok_filmov_eighteen_yo = ('Птичий короб', 'Социальная сеть', 'Джентельмены', 'Отряд самоубийц', 'План побега 2')
spisok_filmov_noteighteen_yo = (
    'Интерстеллар', 'Начало', 'Унесённые призраками', 'Ford против Ferrari', 'Богемская рапсодия')

def print_genres(dct):
    for genre, number in dct.items():
        print("{} ({})".format(genre, number))
genres = {
    "Боевик": 1,
    "Вестерн": 2,
    "Детектив": 3,
    "Драма": 4,
    "Комедия": 5,
    "Ужасы": 6,
}

cls()
root = Tk()
root.geometry("600x600")
root.title("Необходимо авторизироваться в нашем приложении:")

def registration():
    text = Label(text="Для входа в систему необходимо зарегистрироваться")
    text_login = Label(text="Придумайте логин:")
    registr_login = Entry()
    text_password1 = Label(text="Придумайте пароль: ")
    registr_password1 = Entry()
    text_password2 = Label(text="Введите пароль ещё раз: ")
    registr_password2 = Entry(show="*")
    button_registr = Button(text="Зарегистрироваться", command=lambda: save())
    text.pack()
    text_login.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {registr_login.get(): registr_password1.get()}
        f = open("base.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text="Теперь вы можете авторизироваться!")
    text_enter_login = Label(text="Введите ваш логин:")
    enter_login = Entry()
    text_enter_pass = Label(text="Введите ваш пароль:")
    enter_password = Entry(show="*")
    text_log.pack()
    button_login = Button(text="Войти", command=lambda: log_pass())
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_login.pack()

    def log_pass():
        f = open("base.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен")
                root.destroy()
            else:
                messagebox.showerror("Ошибка, вы ввели неверный логин или пароль!")
        else:
            messagebox.showerror("Ошибка, вы ввели неверный логин!")

registration()
root.mainloop()

sleep(2)
print(Fore.GREEN + "Приветствую вас в приложении КиноКос =D" + Fore.WHITE)
sleep(2)
print(Fore.CYAN + "Дата и время: " + Fore.WHITE + ("{:%d/%m/%Y %H:%M}".format(date)) + Fore.WHITE)
sleep(2)
print("_____________________________________________________________________")
print(
    Fore.YELLOW + "1 - " + Fore.MAGENTA + "Покупка билетов" + Fore.YELLOW + "\n2 - " + Fore.MAGENTA + "Популярные "
                                                                                                      "жанры фильмов"
                                                                                                      "в кино" +
    Fore.YELLOW + "\n3 - " + Fore.MAGENTA + "О приложении" + Fore.WHITE)
vibor = 0
while vibor < 1 or vibor > 3:
    try:
        vibor = int(input("Выберите:"))
        if vibor < 1 or vibor > 3:
            print("Введите значения ещё раз.")
            vibor = int(input("Выберите:"))
    except ValueError:
        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)

if vibor == 1:
    sleep(1)
    cls()
    print(Fore.CYAN + "Заказать билеты можно двумя способами:" + Fore.WHITE)
    print("_____________________________________________________________________")
    print(
        Fore.YELLOW + "1 - " + Fore.MAGENTA + "Прямо в приложении" + Fore.YELLOW + "\t2 - " + Fore.MAGENTA + "Позвонив на горячую линию" + Fore.WHITE)
    vibor1 = 0
    while vibor1 < 1 or vibor1 > 2:
        try:
            vibor1 = int(input("Выберите:"))
            if vibor1 < 1 or vibor1 > 2:
                print("Введите значения ещё раз.")
                vibor1 = int(input("Введите:"))
        except ValueError:
            print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
    subprocess.call("cls", shell=True)
    if vibor1 == 1:
        sleep(1)
        cls()
        vibor11 = 0
        while vibor11 < 1 or vibor11 > 100:
            try:
                vibor11 = int(input("Ваш возраст:"))
                if vibor11 < 1 or vibor11 > 100:
                    print("Введите корректный возраст.")
                    vibor11 = int(input("Ваш возраст:"))
            except ValueError:
                print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
        if vibor11 >= 18:
            sleep(1)
            cls()
            print(Fore.CYAN + "Список фильмов" + Fore.RED + " (18+)" + Fore.CYAN + ":" + Fore.WHITE)
            for i in spisok_filmov_eighteen_yo:
                print(i)
            vibor111 = 0
            while vibor111 < 1 or vibor111 > 4:
                try:
                    vibor111 = int(input("Введите номер желаемого желаемый фильм:"))
                    if vibor111 < 1 or vibor111 > 4:
                        print("Введите номер фильма ещё раз")
                        vibor111 = int(input("Введите номер желаемого желаемый фильм:"))
                except ValueError:
                    print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
            if vibor111 == 1:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[0])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print("Пять лет назад мир погрузился в хаос: увидев нечто, люди кончают жизнь самоубийством. Женщина "
                      "с двумя пятилетними детьми, услышав по радио о безопасном месте, отправляется на поиски "
                      "выжившей общины и прихватывает с собой попугаев в коробке. Чтобы сохранить жизнь в этом новом "
                      "мире, самое главное — не смотреть по сторонам и слушать, как птицы реагируют на приближающуюся "
                      "опасность.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "8:30" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "14:00" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "20:35" + Fore.WHITE)
                vibor1111 = 0
                while vibor1111 < 1 or vibor1111 > 3:
                    try:
                        vibor1111 = int(input("Выберите:"))
                        if vibor1111 < 1 or vibor1111 > 3:
                            print("Выберите ещё раз.")
                            vibor1111 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                    print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
            if vibor111 == 2:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[1])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print(
                    "В фильме рассказывается история создания одной из самых популярных в Интернете социальных сетей "
                    "- Facebook. Оглушительный успех этой сети среди пользователей по всему миру навсегда изменил "
                    "жизнь студентов-однокурсников гарвардского университета, которые основали ее в 2004 году и за "
                    "несколько лет стали самыми молодыми мультимиллионерами в США.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "8:00" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "11:50" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "18:45" + Fore.WHITE)
                vibor1112 = 0
                while vibor1112 < 1 or vibor1112 > 3:
                    try:
                        vibor1112 = int(input("Выберите:"))
                        if vibor1112 < 1 or vibor1112 > 3:
                            print("Выберите ещё раз.")
                            vibor1112 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
            if vibor111 == 3:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[2])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print(
                    "Один ушлый американец ещё со студенческих лет приторговывал наркотиками, а теперь придумал схему "
                    "нелегального обогащения с использованием поместий обедневшей английской аристократии и очень "
                    "неплохо на этом разбогател. Другой пронырливый журналист приходит к Рэю, правой руке американца, "
                    "и предлагает тому купить киносценарий, в котором подробно описаны преступления его босса при "
                    "участии других представителей лондонского криминального мира — партнёра-еврея, китайской "
                    "диаспоры, чернокожих спортсменов и даже русского олигарха.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "13:00" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "17:00" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "21:45" + Fore.WHITE)
                vibor1113 = 0
                while vibor1113 < 1 or vibor1113 > 3:
                    try:
                        vibor1113 = int(input("Выберите:"))
                        if vibor1113 < 1 or vibor1113 > 3:
                            print("Выберите ещё раз.")
                            vibor1113 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
            if vibor111 == 4:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[3])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print(
                    "Правительство решает дать команде суперзлодеев шанс на искупление. Подвох в том, "
                    "что их отправляют на выполнение миссии, где они, вероятнее всего, погибнут.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "12:00" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "17:30" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "22:40" + Fore.WHITE)
                vibor1114 = 0
                while vibor1114 < 1 or vibor1114 > 3:
                    vibor1114 = int(input("Выберите:"))
                    try:
                        if vibor1114 < 1 or vibor1114 > 3:
                            print("Выберите ещё раз.")
                            vibor1114 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
            if vibor111 == 5:
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[4])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print(
                    "Новая, самая современная тюрьма, из которой не сбежать. Ему снова брошен вызов! Он вернулся, "
                    "чтобы выручить напарника и доказать, что для него нет невозможного. Добро пожаловать в АиД!")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "11:00" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "16:00" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "23:45" + Fore.WHITE)
                vibor1111 = 0
                while vibor1114 < 1 or vibor1114 > 3:
                    try:
                        vibor1111 = int(input("Выберите:"))
                        if vibor1114 < 1 or vibor1114 > 3:
                            print("Выберите ещё раз.")
                            vibor1114 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))

        elif vibor11 < 18:
            sleep(1)
            cls()
            print(Fore.CYAN + "Список фильмов" + Fore.RED + "(<18)" + Fore.CYAN + ":" + Fore.WHITE)
            print(*spisok_filmov_noteighteen_yo, sep='\n')
            vibor111 = 0
            while vibor111 < 1 or vibor111 > 4:
                try:
                    vibor111 = int(input("Введите номер желаемого желаемый фильм:"))
                    if vibor111 < 1 or vibor111 > 4:
                        print("Введите номер фильма ещё раз")
                        vibor111 = int(input("Введите номер желаемого желаемый фильм:"))
                except ValueError:
                    print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
            if vibor111 == 1:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[0])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print("Наше время на Земле подошло к концу, команда исследователей берет на себя самую важную миссию в истории человечества; путешествуя за пределами нашей галактики, чтобы узнать есть ли у человечества будущее среди звезд.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "8:30" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "14:00" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "20:35" + Fore.WHITE)
                vibor1111 = 0
                while vibor1111 < 1 or vibor1111 > 3:
                    try:
                        vibor1111 = int(input("Выберите:"))
                        if vibor1111 < 1 or vibor1111 > 3:
                            print("Выберите ещё раз.")
                            vibor1111 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
            if vibor111 == 2:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[1])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print("Кобб — талантливый вор, лучший из лучших в опасном искусстве извлечения: он крадет ценные секреты из глубин подсознания во время сна, когда человеческий разум наиболее уязвим. Редкие способности Кобба сделали его ценным игроком в привычном к предательству мире промышленного шпионажа, но они же превратили его в извечного беглеца и лишили всего, что он когда-либо любил.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "8:00" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "11:50" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "18:45" + Fore.WHITE)
                vibor1112 = 0
                while vibor1112 < 1 or vibor1112 > 3:
                    try:
                        vibor1112 = int(input("Выберите:"))
                        if vibor1112 < 1 or vibor1112 > 3:
                            print("Выберите ещё раз.")
                            vibor1112 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
            if vibor111 == 3:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[2])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print("Маленькая Тихиро вместе с мамой и папой переезжают в новый дом. Заблудившись по дороге, они оказываются в странном пустынном городе, где их ждет великолепный пир. Родители с жадностью набрасываются на еду и к ужасу девочки превращаются в свиней, став пленниками злой колдуньи Юбабы, властительницы таинственного мира древних богов и могущественных духов.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "13:00" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "17:00" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "21:45" + Fore.WHITE)
                vibor1113 = 0
                while vibor1113 < 1 or vibor1113 > 3:
                    try:
                        vibor1113 = int(input("Выберите:"))
                        if vibor1113 < 1 or vibor1113 > 3:
                            print("Выберите ещё раз.")
                            vibor1113 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
            if vibor111 == 4:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[3])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print("Сюжет повествует о группе американских инженеров и дизайнеров. В 1960-х под руководством конструктора Кэрролла Шелби и при поддержке британского гонщика Кена Майлса они должны были с нуля сделать абсолютно новый спорткар, способный опередить Феррари — непобедимого чемпиона 24-часовой гонки на выносливость Ле-Ман.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "12:00" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "17:30" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "22:40" + Fore.WHITE)
                vibor1114 = 0
                while vibor1114 < 1 or vibor1114 > 3:
                    try:
                        vibor1114 = int(input("Выберите:"))
                        if vibor1114 < 1 or vibor1114 > 3:
                            print("Выберите ещё раз.")
                            vibor1114 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
            if vibor111 == 5:
                sleep(1)
                cls()
                print(Fore.MAGENTA + "Вы выбрали: " + Fore.WHITE + spisok_filmov_eighteen_yo[4])
                print(Fore.LIGHTBLUE_EX + "Краткое описание фильма:" + Fore.WHITE)
                print("Чествование группы Queen, их музыки и их выдающегося вокалиста Фредди Меркьюри, который бросил вызов стереотипам и победил условности, чтобы стать одним из самых любимых артистов на планете. Фильм прослеживает головокружительный путь группы к успеху, благодаря их культовым песням и революционному звуку, практически распад коллектива, поскольку образ жизни Меркьюри выходит из-под контроля, и их триумфальное воссоединение накануне концерта Live Aid, ставшим одним из величайших выступлений в истории рок-музыки.")
                print(
                    Fore.CYAN + "Свободное время:" + Fore.YELLOW + "\n1 - " + Fore.LIGHTCYAN_EX + "11:00" + Fore.YELLOW + "\n2 - " + Fore.LIGHTCYAN_EX + "16:00" + Fore.YELLOW + "\n3 - " + Fore.LIGHTCYAN_EX + "23:45" + Fore.WHITE)
                vibor1111 = 0
                while vibor1114 < 1 or vibor1114 > 3:
                    try:
                        vibor1111 = int(input("Выберите:"))
                        if vibor1114 < 1 or vibor1114 > 3:
                            print("Выберите ещё раз.")
                            vibor1114 = int(input("Выберите:"))
                    except ValueError:
                        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
                print(Fore.LIGHTGREEN_EX + "Ваш уникальный номер билета " + Fore.WHITE + "№:" + str(
                    random.randint(10320, 10033200)))
        else:
            print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
            
    elif vibor1 == 2:
        sleep(1)
        cls()
        print(Fore.GREEN + "Горячая линия: " + Fore.WHITE + "+375(33)358-94-89" + Fore.CYAN + " (МТС)" + Fore.WHITE)
    else:
        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)

elif vibor == 2:
    sleep(1)
    cls()
    print(Fore.CYAN + "В данный момент у нас такой список жанров: " + Fore.WHITE)
    print("_____________________________________________________________________")
    print_genres(genres)

elif vibor == 3:
    sleep(1)
    cls()
    print(Fore.CYAN + "Наше приложение специализирауется на всём что связано с киноиндустрией" + Fore.WHITE)
    print("_____________________________________________________________________")
    print(
        Fore.YELLOW + "1 - " + Fore.MAGENTA + "Связь" + Fore.YELLOW + "\t2 - " + Fore.MAGENTA + "Вакансии" + Fore.YELLOW + "\t3 - " + Fore.MAGENTA + "Правовая информация" + Fore.YELLOW + "\t4 - " + Fore.MAGENTA + "Размещение рекламы" + Fore.YELLOW + "\t5 - " + Fore.MAGENTA + "Пользовательское соглашение" + Fore.WHITE)
    vibor3 = 0
    while vibor3 < 1 or vibor3 > 5:
        try:
            vibor3 = int(input("Выберите:"))
            if vibor3 < 1 or vibor3 > 5:
                print("Введите значения ещё раз.")
                vibor3 = int(input("Выберите:"))
        except ValueError:
            print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)
    if vibor3 == 1:
        sleep(1)
        cls()
        print(Fore.CYAN + "\nС нами можно связаться:" + Fore.WHITE)
        print("_____________________________________________________________________" + Fore.WHITE)
        print(Fore.GREEN + "Электронная почта: " + Fore.WHITE + "asp1rantzenevich@gmail.com")
        print(Fore.GREEN + "Рабочий телефон" + Fore.CYAN + " (МТС)" + Fore.WHITE + ": " + "+375(33)358-94-89")
        print(Fore.GREEN + "Рабочий адрес" + Fore.WHITE + ": " + "Cт.м. " + "Каменная горка")
    elif vibor3 == 2:
        sleep(1)
        cls()
        print(Fore.CYAN + "\nВакансии:" + Fore.WHITE)
        print("_____________________________________________________________________" + Fore.WHITE)
        print("\nВ данный момент вакансий не существует." + Fore.WHITE)
    elif vibor3 == 3:
        sleep(1)
        cls()
        print(Fore.CYAN + "\nПравовая информация: " + Fore.WHITE)
        print("_____________________________________________________________________" + Fore.WHITE)
        print(Fore.MAGENTA + "Материалы положения: " + Fore.WHITE)
        print(
            "Доступ к материалам приложения, в том числе к отзывам пользователей, предоставляется исключительно для "
            "личного использования и ознакомления. Дальнейшее использование, воспроизведение, распространение любым "
            "способом, копирование, передача в эфир для всеобщего сведения, перевод, переделка и использование любым "
            "иным способом в каких-либо иных целях контента приложения возможно только с указанием активной ссылки на "
            "приложение, в случае с картинками – с указанием ссылки на приложение  на каждом фото. К лицам, "
            "нарушающим имущественные и личные неимущественные права, законные интересы авторов и правообладателей, "
            "могут быть применены меры гражданско-правовой, административной и уголовной ответственности в "
            "соответствии с действующим законодательством Республики Беларусь.")
        print(Fore.MAGENTA + "Предупреждение об ответственности:" + Fore.WHITE)
        print("Приложение КиноКос не несет ответственности за содержание рекламных материалов.")
        print(Fore.MAGENTA + "Правила размещения комментариев:" + Fore.WHITE)
        print(
            "Оставляя комментарии к материалам, размещенным в приложении КиноКос, руководствуйтесь " + Fore.MAGENTA + "Пользовательским соглашением." + Fore.WHITE)
        print(Fore.MAGENTA + "Политика обработки персональных данных:" + Fore.WHITE)
        print(
            "Политика, с которой пользователь соглашается, отправляя электронный адрес и (или) иные данные через "
            "форму заявки и подписки.")
        print(Fore.MAGENTA + "Контакты:" + Fore.WHITE)
        print(
            "По вопросам использования материалов и сотрудничества пишите по адресу:" + Fore.CYAN + "asp1rantzenevich"
                                                                                                    "@gmail.com" +
            Fore.WHITE)

    elif vibor3 == 4:
        sleep(1)
        cls()
        print(Fore.CYAN + "\nРазмещение рекламы:" + Fore.WHITE)
        print("В данный момент заказ рекламы недоступен")
        print("_____________________________________________________________________" + Fore.WHITE)
    elif vibor3 == 5:
        sleep(1)
        cls()
        print(Fore.CYAN + "\nПользовательское соглашение:" + Fore.WHITE)
        print("_____________________________________________________________________" + Fore.WHITE)
    else:
        print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)

else:
    print("Произошли технические неполадки." + Fore.RED + "\nError404" + Fore.WHITE)