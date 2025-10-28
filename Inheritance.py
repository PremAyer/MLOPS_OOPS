
# #simple inheritance

# #Base class
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# #Derived class
# class Dog(Animal):
#     # def __init__(self):
#     #     self.behaviour="friendly"
        
#     def speak1(self):
#         print(f"{self.name} barks.")

# #create an instance of Animal
# # animal = Animal("Generic Animal")
# # animal.speak()

# #create an instance of Dog 

# dog = Dog("Buddy")
# dog.speak()
# dog.speak1()


#Super keyword 

#Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

#Derived class
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed
        
    def speak(self):
        super().speak() #call the base class method 
        print(f"{self.name} barks. It is a {self.breed}.")


dog = Dog("Golden Retriever")
dog.speak()
