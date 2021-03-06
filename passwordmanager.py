import sys

class BasePasswordManager:

    old_passwords = []

    def get_password(self):
        if(self.old_passwords):
          return self.old_passwords[len(self.old_passwords)-1]

    def is_correct(self, value):
        return value==self.get_password()

class PasswordManager(BasePasswordManager):
    def get_level(self, value=None):
        if value is None:
            value = self.get_password()
        if value.isdigit() or value.isalpha():
            return 0
        elif value.isalnum():
            return 1
        else:
            return 2
      
    def set_password(self, value):
        if len(value)>=6:
            if len(self.old_passwords)==0:
                self.old_passwords.append(value)
                print("Password added")
            else:
                if self.get_level()==2:
                    if self.get_level(value)==2:
                        self.old_passwords.append(value)
                        print("Password added")
                    else:
                        print("Password too weak")
                else:
                    if self.get_level(value)>self.get_level():
                        self.old_passwords.append(value)
                        print("Password added")
                    else:
                        print("Password too weak")
        else:
            print("Password too short")

# a=PasswordManager()

while(1):
  print("\n------- Enter Your choice ----------\n")
  print("1 : Check List Of Old Passwords ")
  print("2 : Set New Password ")
  print("3 : Your Last Password")
  print("4 : Delete Old Password")
  print("5 : Exit")
  
  a=PasswordManager()

  class Switcher(object):
    def indirect(self,i):
      method_name='number_'+str(i)
      method=getattr(self,method_name,lambda :'Invalid')
      return method()
      
    def number_1(self):
      print("List Of All Passwords are :")
      print(a.old_passwords)
      
    def number_2(self):
      print("Enter Your New Password :")
      print(a.set_password(input()))

    def number_3(self):
      print("Your Last Password was :")
      print(a.get_password())

    def number_4(self):
      # a.old_passwords.pop(0)
      print("Old Password"+"----'"+ a.old_passwords.pop(0)+"'----"+"Deleted Successfully")

    def number_5(self):
      sys.exit("")

  s=Switcher()
  s.indirect(input("\n"))

