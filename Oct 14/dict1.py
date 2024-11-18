# dict enter element via user input 
dct = dict()

while True:
    name = input("Enter the dict : ")
    if name =='' or name == " ":
        break
    else:
        dct[name] = input("Enter the value of given key : ")
print(dct)