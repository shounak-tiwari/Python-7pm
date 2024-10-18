# 2. no parameter with return

def add():
    no1 = int(input("Enter the value of number 1 : "))
    no2 = int(input("Enter the value of number 2 : "))

    return no1+no2


result = add()

print(type(result))
