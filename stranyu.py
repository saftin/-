name = input("Введите имя пресонажа ")
stra = input("Введите название страны ")
game = True
vh = 1
money = 0

print("вы играете за президента", name, "в стране", stra, "отношение с соседней страной нейтрально.")
print("-------------------------------------------------")
print("деньги в ход - 1$")
print("деньги - 0$")
print("жители - 0")
print("-------------------------------------------------")

while game == True:
    wari = input("1 - построить завод = 100$, 2 - открыть чат = 0$, 3 - построить дом = 50$, enter - пропуск хода = 0: ")
    money += vh
    
    if wari == "1" and money > 99:
        vh += 1
        money -= 100
        
    print("-------------------------------------------------")
    print("деньги в ход -", vh, "$")
    print("деньги - ", money, "$")
    print("жители - 0")
    print("-------------------------------------------------")
