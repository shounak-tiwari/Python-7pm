# polymorphisms : poly-morphisms is a laten green work which means poly means many and morphisms means forms 

# compile time polymorphisms
    # method overloading
    # method overriding 

try:
    from multipledispatch import dispatch

    class Demopoly:
        @dispatch(int, int)
        def add(self, i, j):
            print(i + j)

        @dispatch(str, int)
        def add(self, i, j):
            print("name:", i)
            print("age:", j)

    kaif = Demopoly()
    kaif.add('moh. kaif', 19)

except ModuleNotFoundError as e:
    print(e)
