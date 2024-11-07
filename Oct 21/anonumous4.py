import functools
lst = [1,2,3,4,5,6,7,8,9]
add = functools.reduce(lambda x,y :x+y,lst)
print(add)