class employee:
    #special method/magic method/dunder method - constructor 
    def __init__(self):
        #print(id(self)) #id is the location of self in RAM
        #print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation= "software Eng"
        #print("attributes/data have been initiated")
    
    def travel(self,destination):
        print("This travel method is called manually")
        print(f"Employee is now travelling to {destination}")


#create an obj/instance of the class
 
sam = employee()

'''*******we can create obj outside the class as well like this*******'''
sam.name = "sam kumar"
print(sam.name)

# print(id(sam))
# print(sam.salary)
# print(sam.id)
# sam.travel("Pokhara") # sam is going in to the paranthesis so we use self in method
# print(type(sam))