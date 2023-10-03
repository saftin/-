n = int(input("введите число от 1 до 100. "))
no = n % 3
nt = n % 5
if no == 0 and nt == 0:
    print("физбаз")
    
elif no == 0:
    print("физ")

elif no == 0 and nt == 0:
    print("физбаз")
elif nt == 0:
    print("баз")

    
