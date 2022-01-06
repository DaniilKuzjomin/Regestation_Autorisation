from random import *

users=["Daniil"]
passwords=["505034"]


def menu():
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
                        print("Извините, но Ваш пароль не подходить.")
                        print()
        if a==2:
            print("Введите Ваши данные для входа!")
            login=str(input("Ваш логин - "))
            password=str(input("Ваш пароль - "))
            check=autorisation_check(login,password)
            if check==True and check1==True:
                print("Успешный вход, добро пожаловать!")
            else:
                print("Неверный логин либо пароль! Попробуйте ещё раз.")
                print()



def auto_pass():
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
    """Проверяет присутствуют ли в пароле числа, большие и маленькие буквы и есть ли в них символы.
    """
    spisok=list(passwords)
    for p in spisok:
        if p.isdigit():
            c=True
        if p.isalpha():
            b=True
        if p.isupper():
            u=True
        if p.islower():
            l=True
        if p in list(".,:;!_*-+()/#¤%&"):
            s=True
        if c==True and b==True and u==True and l==True and s==True:
            check=True
        else:
            check=False
            return check

def autorisation_check(login,password):
    if login in users:
        check=True
    else:
        check=False
    if password in passwords:
        check1=True
    else:
        check1=False
        return check
        return check1
