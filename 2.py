a=int(input("Введите число"))
b=int(input("Введите число"))
if b==0:
    print("На ноль делить нельзя")
elif a%b:
    print("Делится с остатком")
else:
    print(a/b)