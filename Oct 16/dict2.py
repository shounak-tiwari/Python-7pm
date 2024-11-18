dct1 = {'Name' : 'Akash','Age' : '24', 'address' : 'indore'}
dct2 = {'Name1' : 'Akash','Age1' : '24', 'address1' : 'indore'}




# dct1.update(dct2)
# print(dct1)

# remove element from dictionary using key 

# key_remove_item = dct.pop('Age')

# print(key_remove_item)

# for removing last item from dictionary 

# last_item = dct.popitem()

# print("last item of dict : ",last_item)

# print("After removing last item from dictionary\n",dct)

# print(type(dct))

# copy_dict = dct.copy()

# print("Copy dict is copy of original dct : ",copy_dict)

# for clearing all items from dict 

# dct.clear()

# print("dict after apply clear function : ",dct)

# items =  dct.get('address')

# print(items)

# lst = ['Hasan','Ankita','Payal','Bhumika','Priyal','Aman','kaif','Ganesh','Faiz']
# value = "Universal"
# new_dct = dict.fromkeys(lst, value)
# print(new_dct)

# x = dct.items()
# print(type(x))


# intro = [('Name','akash'),('age','23'),('address','indore')]
# print(type(intro[0]))


car = {
    'Brand-name':'Toyota',
    'Model-name':'Fortuner',
    'year':'2025'
}

x = car.setdefault('Model-name-1','Fortuner legender')

print(x)

print(car)