# lst = [1,2,3]
# my_str = "mlops playlist is good"
# my_int = 160

# print(type(my_int))
# lst.clear()
# print(lst)

from oops_project import chatbook

user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)
# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

#print(user1._chatbook__name) #to access hidden variable
#getter and setter
# print(user1.get_name())
# user1.set_name("Prem")
# print(user1.get_name())
