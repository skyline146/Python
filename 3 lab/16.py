# Створити гру «камінь-ножиці-папір» між двома умовними гравцями.
import random as r
def Results(player1, player2):
    FinalValues = ["Камень", "Ножницы", "Бумага"]
    print("Игрок 1:", FinalValues[player1])
    print("Игрок 2:", FinalValues[player2])
    if player1 == player2:
        print("Ничья!")
    if (player1 == 0 and player2 == 1) or (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 0):
        print("Выиграл Игрок 1!")
    if (player2 == 0 and player1 == 1) or (player2 == 1 and player1 == 2) or (player2 == 2 and player1 == 0):
        print("Выиграл Игрок 2!")
player1 = r.randint(0, 2)
player2 = r.randint(0, 2)
Results(player1, player2)