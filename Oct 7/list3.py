l1 = [1,-1,-2,3,-5,6,7,4]

x =0 

while x< len(l1):

    if l1[x] < 0 :
        l1.pop(x)
    
    else:
        x=x+1
    

print(l1)