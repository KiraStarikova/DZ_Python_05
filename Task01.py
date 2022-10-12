#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота "интеллектом"

konf = 101

# ф-ция жеребъёвка
import random

def lottery():
    if random.randint(0, 1)== 1:
        user_name = "gamer1"
    else:
        user_name = "gamer2"
    return user_name
    
def valid_move(konf_left):# проверка правильности ввода кол-ва конфет
    while True:
        n = int(input('- сколько конфет хотите взять? - '))
        if 0 < n <= 28:
            konf_taken = n
            if n > konf_left:
                print('- Столько конфет нет - ')
            else:
                print(f'- Утащил {n} конфет -')
                return konf_taken # если н = 0?
        else:
            print('- не верное кол-во -') 


def show_desk(konf_left, user_name):# рисуем поле игры: ск-ко конфет и кто ходит
    print('*'*80)
    print(f'- на столе {konf_left} конфеток -')
    print(f'- ход игрока - {user_name} - ')
    

def game():# игра: 
    konf_left = konf# ск-ко конфет на столе
    user_name = lottery()# чей первый ход - выбор
    show_desk(konf_left, user_name)# обновляем поле игры
    while konf_left > 0:# до тех пор пока есть конфеты на столе
        konf_taken = valid_move(konf_left)
        konf_left -= konf_taken# осталось конфет после хода
        if konf_left > 0:# если конфеты ещё есть - передаём ход др игроку
            if user_name == "gamer1":
                user_name = "gamer2"
            else:
                user_name = "gamer1"
        show_desk(konf_left, user_name)# финальная отрисовка доски 
    print(f"@- Победил - {user_name} @")# Публикование рез=та


if __name__== '__main__':
    game()