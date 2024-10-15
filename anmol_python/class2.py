class anmol:
    name = "abc"
    version = 20

    #Added function in class
    def testingfunc(self):
        print("This is a test function")
        print(self.name)

#Instatiating the class
T1=anmol()

#Calling function of class
T1.testingfunc()

#Printing variables of class
print(T1.name)
print(T1.version)

