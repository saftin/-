import  random


name = input("Введите имя пресонажа ")
stra = input("Введите название страны ")
game = True
vh = 1
money = 0
g = 0
lvl = 0
o = 2
pl_1 = 0
pl_2 = 0


print("вы играете за президента по имени", name, "в стране", stra, "отношение с соседней страной нейтрально.")
print("-------------------------------------------------")
print("деньги в ход - 1$")
print("деньги - 0$")
print("жители - 0")
print("LVL - 1")
print("-------------------------------------------------")


while game == True:
    wari = input("1 - построить завод = 100$, 2 - открыть чат = 0$, 3 - построить дом = 50$, enter - пропуск хода = 0: ")
    money += vh
    
    
    if wari == "1" and money > 99:
        vh += 1
        money -= 100

        
    if wari == "3" and money > 49:
        g += 1
        money -= 50


    if wari == "2" and lvl > 2:
        money -= 0
        
        if o == 2:
            wari = input("1 - подарок = -20$ + отношение, 2 - разговоры,")
            if wari == "1" and money > 19:
                money -= 20
                if o != 3:
                    o += 1
                    
                    
            if wari == "2":
                 wari = input("1 - похвалить, 2 - обозвать, 3 - выйти")
                 if wari == "1":
                    if o != 3:
                        o += 1
                    
                    
                 elif wari == "2":
                     if o != 1:
                        o -= 1
                

        elif o == 3:
            wari = input("1 - подарок, 2 - разговоры, 3 - торговля")
            if wari == 3:
                if money > 19999:
                    pl_1 = random.randint(2, 12)
                    pl_2 = random.randint(2, 12)
                    print("Вы выбросили", pl_1, ", компьютер выбросил", pl_2)
                    if pl_1 > pl_2:
                        print("вы победили!")
                        money += 20000
                    elif pl_1 > pl_2:
                        print("вы проиграли!")
                    else:
                        print("ничья")


                    
                else:
                    print("У тебя не 20000$!")
                    

        elif o == 3:
            wari = input("1 - подарок, 2 - разговоры, 3 - война")
            
            
    elif wari == "2" and lvl < 3:
        print("!!! Чтобы открыть чат нужен уровень 3 !!!")
        
       
    lvl = vh

       
    print("-------------------------------------------------")
    print("деньги в ход -", vh, "$")
    print("деньги - ", money, "$")
    print("жители -", g * 3)
    print("LVL -", lvl)
    print("отношение с соседней страной -", o)
    print("1 - враг, 2 - нейтрально, 3 - друг")
    print("-------------------------------------------------")
