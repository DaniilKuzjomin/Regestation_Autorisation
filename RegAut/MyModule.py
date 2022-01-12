from random import *


def menu():
    """Peamenüü, millega kasutaja saab registreeruda või sisse logida
    """
    while True:
        print("Добро пожаловать!")
        print("1 - Регистрация")
        print("2 - Авторизация")
        a=int(input())
        print()
        if a==1:
            print("Для регистрации вам необходимо ввести логин и пароль.")
            print()
            while 1:
                login=input("Введите ваш Логин: ")
                if login not in users:
                    print("Вы заняли Логин:", login)
                    print()
                    break
                else:
                    print("К сожалению данный Логин уже используется, попробуйте ввести другой.")
                    print()
            print("Выберите как будет создаватся Ваш пароль:")
            print("1 - Самостоятельно")
            print("2 - Автоматически")
            b=int(input())
            if b==2:
                ps=auto_pass()
                passwords.append(ps)
            while 1:
                if b==1:
                    print("ВНИМАНИЕ! Ваш пароль должен содержать: знаки, большие и маленькие символы, а так же цифры.")
                    ps=input("Введите свой придуманный пароль: ")
                    check=pass_check(passwords)
                    if check==True:
                        users.append(login)
                        passwords.append(ps)
                    else:
                        print()
                        print("Извините, но Ваш пароль не подходить.")
                        print()
        if a==2:
            print("Введите Ваши данные для входа!")
            login=str(input("Ваш логин - "))
            password=str(input("Ваш пароль - "))
            check=autorisation_check(login,password)
            if check==True:
                print("Успешный вход, добро пожаловать!")
            else:
                print("Неверный логин либо пароль! Попробуйте ещё раз.")
                print()



def auto_pass():
    """Genereerib kasutajatele random parool
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    print(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    return ls

def pass_check(passwords:str)-> bool:
    """Kontrollib, kas parool sobib kõikidele parameetritele
    :param str passwords:
    :rtype: bool
    """
    spisok=list(passwords)
    c=b=u=l=s=0
    for p in spisok:
        if p.isdigit(): # Состоит ли пароль из цифр
            c=True
        if p.isalpha(): # Состоит ли пароль из букв
            b=True
        if p.isupper(): # Состоит ли пароль из символов в верхнем регистре
            u=True
        if p.islower(): # Состоит ли пароль из символов в нижнем регистре 
            l=True
        if p in list(".,:;!_*-+()/#¤%&"): # Состоит ли пароль из указанных символов
            s=True
        if c==True and b==True and u==True and l==True and s==True:
            check=True
        else:
            check=False
            return check

def autorisation_check(login:str,password:str):
    """Kontrollib, kas loendis on selline kasutaja ja parool
    :param str login:
    :param str password:
    :rtype: bool
    """
    a=b=0
    if login in users:
        a=True
    if password in passwords:
        b=True
    if a==True and b==True:
        check=True
    else:
        check=False
        return check
