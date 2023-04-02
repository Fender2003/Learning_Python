class mammal:
    def walk(self):
        print("walk")

class Dog(mammal):
    def bark(self):
        print("bark")

class Cat(mammal):
    def annoying(self):
        print("annoy")

dog1 = Dog()
dog1.walk()

cat1=Cat()
cat1.annoying()
