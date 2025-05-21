def fac(i):
    if i == 1:
        return 1
    return i*fac(i-1)

a = int(input("Введите любую цифру: "))
print(f"{a}! = ", end="")
print(fac(a))
