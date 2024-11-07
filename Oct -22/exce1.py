try:
    import aman_back 
    print(aman_back.hey())
    no1= 10
    no2 = 0
    result = no1/no2
    print(f"the division of {no1} and {no2} is {result}")
except ArithmeticError as e:
    print(e)
except ModuleNotFoundError as e:
    print(e)
except:
    print("error found in some where !")
finally:
    print("Thanks visit again ")