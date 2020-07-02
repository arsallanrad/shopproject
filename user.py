import hashlib
import json
import sys
import re
from json import JSONEncoder
class user :
    def __init__(self,firstname='',lastname='',location='',email='',password='',mobile=''):
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.email = email
        self.password = password
        self.mobile = mobile
        



    def input(self):

       self.firstname =str(input(f"your first name is : {self.firstname}"))
       if (len(self.firstname) == 0 or self.firstname == None): 
           print("EMPTY ERROR \n TRY AGAIN")     
           sys.exit()

       self.lastname =str(input(f"your last name is : {self.lastname}"))
       if (len(self.lastname) == 0 or self.lastname == None): 
           print("EMPTY ERROR \n TRY AGAIN")     
           sys.exit()

       self.location =str(input(f"your location is : {self.location}"))
       if (len(self.location) == 0 or self.location == None): 
           print("EMPTY ERROR \n TRY AGAIN")     
           sys.exit()

       self.email =str(input(f"your email addres is : {self.email}"))
       if (len(self.email) == 0 or self.email == None): 
           print("EMPTY ERROR \n TRY AGAIN")     
           sys.exit()

       self.mobile = int(input(f"your mobile phone is : {self.mobile}"))
       if ( self.mobile == None): 
           print("EMPTY ERROR \n TRY AGAIN")     
           sys.exit()
       

       
        




       

    def print(self):
        
        password = input("enter your password: ")
        passHashMd5 = hashlib.md5(password.encode())
        print(passHashMd5.hexdigest())
        print("\twelcome to onlineshop!!")

    


x = user()
# x.input()
# x.print()

print("Welcome to online shop")
print("-----------------------------")
print("1. Sign up")
print("2. Log in\n")
select = input("select an option: ")

if (str(select) == "1"):
   x.input()
   password = input("enter your password: ")
   passHashMd5 = hashlib.md5(password.encode())
   with open('./test_file' , mode='w') as passwordFile:
    passwordFile.write(passHashMd5.hexdigest())
   print("\twelcome to onlineshop!!")
elif (str(select) == "2"):
    email = input("enter your email: ")
    if (len(email) == 0 or email == None): 
           print("EMPTY ERROR \n TRY AGAIN")     
           sys.exit()
    # if (email in str(select) == "1") == (email in str(select) == "2"):
    #     print("loged in")
    password = input("enter your password: ")
    if (len(password) == 0 or password == None): 
           print("EMPTY ERROR \n TRY AGAIN")     
           sys.exit()




class userData(JSONEncoder):
        def default(self, a):
            return a.dict
        
print(userData().encode(x))
userJSONData = json.dumps(x, indent=4, cls=userData)
print(userData)
userJSON = json.loads(userJSONData)
print(userJSON)

with open('userJSON.json', 'w') as json_file:
    json.dump(userJSON, json_file)
elif (str(select) == "3"):
    sys.exit()