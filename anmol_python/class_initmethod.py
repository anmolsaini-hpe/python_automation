class anmol:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def testfunct(self):
        print("My name is ", self.name)

#Instatiating class and pass parameters value
T1=anmol("Hello",30)

T1.testfunct()

print(T1.age)