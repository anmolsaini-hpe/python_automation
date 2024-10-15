####CREATE AN OBJECT
class Tools:
    name = "Jenkins"
    version = 20

    def toolsdes(self):
        print(self.version, self.name + "\tTOOLS")

T1 = Tools()
T1.toolsdes()

print(T1.name)
print(T1.version)