class Animal(object):
    def _init_(self, startname, age):
        self.name = startname
        self.age = age
    def description(self):
        print("this is " + self.name)
        print("he/she is " + str(self.age) + "years old")