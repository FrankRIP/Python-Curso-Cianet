class A():
    def primero(self):
        return "Esta es la clase A"

class B():
    def segunda(self):
        return "Esta es la clase B"

class C(A, B):
    pass

objc = C()
print (objc.primero())
print (objc.segunda())