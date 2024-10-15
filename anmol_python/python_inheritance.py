class A(object):
    def anmol(self):
        print("Hello")

    def __init__(self, something):
        print("A init called")
        self.something = something

# The moment you will instatiate a class, init function will be called.
# Also, the variables for the class should be passed in the init function.

T1 = A("erboiner")