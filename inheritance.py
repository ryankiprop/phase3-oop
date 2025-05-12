class Pet:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print("Pet is Speaking")


class Dog(Pet):
    def __init__(self,name,colour):
        super().__init__(name)
        self.colour = colour

    def speak(self):
        super().speak()
        print("Dog is speaking")

class Cat(Pet):
    pass


dog1=Dog("Rex", "White")
print(dog1.colour)
#dog1.speak()