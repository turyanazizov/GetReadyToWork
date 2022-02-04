def method(obyekt):
    for atr in vars(obyekt):
        if atr[0:2]!='__':
            print(atr)
    print('Number of attributes: ',len(vars(obyekt))-4)

class Class1:
    a = 3

class Class2:
    c = 6
    b = 2

class Class3:
    x = 5
    y = 3
    z = 23

class Class4:
    s = 15
    list=[12,35,5,67]
    def cma():
        pass
    y = 45
    def asd():
        print('salam')
    f = 'sadaf'

method(Class2)