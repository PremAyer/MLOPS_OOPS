class chatbook:
    __user_id = 0  #static var

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id +=1
        self.__name = "Default name" #encapsulation or hidden variable
        self.username = ""
        self.password = ""
        self.loggedin = False
        #self.menu()
    
    #getter setter for static method
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val



    #getter and setter

    def get_name(self):
        return self.__name  #Here we donot use self._chatbook__name because we are inside a class and this self.__name is translated automatically to the self._chatbook__name. it is called name Mangling in python
    
    def set_name(self,value):
        self.__name = value

    def menu(self):
        user_input = input('''Welcome to Chatbook !! How would you like to proceed?
                           1.Press 1 to signup
                           2.Press 2 to signin
                           3.Press 3 to write a post
                           4.Press 4 to message a friend
                           5.Press any other key to exit-> ''')
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()
    
    def signup(self):
        email = input("Enter your email here->")
        password = input("set up your password here->")
        self.username = email
        self.password = password 
        print("You have signedup successfully !!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username =="" and self.password =="":
            print("please signup first by pressing 1 in the main menu")

        else:
            username = input("Enter your username/email here ->")
            password = input("Enter your password here->")
            if self.username ==username and self.password ==password:
                print("you have been successfully signedin")
                self.loggedin = True
            else:
                print("Pls enter the correct credentials...")
        print("\n")
        self.menu()
    
    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here ->")
            print(f"Following content has been posted-> {txt}")
        else:
            print("You need to signin first to post something...")    
        print("\n")  
        self.menu()
    
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter the msg here->")
            friend = input("Whom to send the msg->")
            print(f"Your msg has been sent to {friend}")
        else:
            print("You need to signin first to post something...")    
        print("\n")  
        self.menu()


user1 = chatbook()


        


