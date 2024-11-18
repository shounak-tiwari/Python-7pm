dct = dict()
while True:
    key = input("Enter the key : ")

    if key == '' or key ==" ":
        break
    else:
        dct[key] = input(f"Enter the values of {key} : ")


for key,value in dct.items():
    print(f"{key} == {value}")