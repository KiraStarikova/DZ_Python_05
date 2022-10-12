#2 Создайте программу для игры в "Крестики-нолики".

desk = [1,2,3,4,5,6,7,8,9]
 
victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],
             [1,4,7],[2,5,8],[0,4,8],[2,4,6]]
 
def print_desk():
    print(desk[0], end = " ")
    print(desk[1], end = " ")
    print(desk[2])
 
    print(desk[3], end = " ")
    print(desk[4], end = " ")
    print(desk[5])
 
    print(desk[6], end = " ")
    print(desk[7], end = " ")
    print(desk[8])    
 
def step_desk(step,symbol):
    ind = desk.index(step)
    desk[ind] = symbol
 
def get_result():
    win = ""
 
    for i in victories:
        if desk[i[0]] == "X" and desk[i[1]] == "X" and desk[i[2]] == "X":
            win = "X"
        if desk[i[0]] == "O" and desk[i[1]] == "O" and desk[i[2]] == "O":
            win = "O"   
             
    return win
 
game_over = False
player1 = True
 
while game_over == False:
 
    print_desk()
 
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))
 
    step_desk(step,symbol) 
    win = get_result() 
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
 
       
print_desk()
print("Победил", win)