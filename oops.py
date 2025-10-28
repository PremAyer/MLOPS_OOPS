class employee:
    #special method/magic method/dunder method - constructor 
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation= "software Eng"
        print("attributes/data have been initiated")
    
    def travel(self,destination):
        print("This travel method is called manually")
        print(f"Employee is now travelling to {destination}")


#create an obj/instance of the class

sam = employee()
# print(sam.salary)
# print(sam.id)
# sam.travel("Pokhara")
print(type(sam))