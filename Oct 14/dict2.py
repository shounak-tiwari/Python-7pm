dct = dict()
while True:
    key = input("Enter key : ")
    if key == '' or key==" ":
        break
    else:
        dct[key] = input("Enter value : ")
for key,value in dct.items():
    print(key ,"=> ",value)