'''class linkedin:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email
        self.__password=password
    @property
    def accessemail(self):
        return self._email
    @accessemail.setter
    def accessemail(self,newemail):
        self._email=newemail
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword
        print(f"Welcome to the linkedin {self.name}")

kavya=linkedin('kavya','kavya@gmail.com','kavya@540')
print(kavya.name)
kavya.name='rajitha'
print(kavya.accessemail)
kavya.accessemail='rajitha@gmail.com'
print(kavya.getpassword())
kavya.getpassword='30rajitha'

'''
class Linkedin:
    def __init__(self, name, email, password):
        self.name = name          # Public
        self._email = email       # Protected
        self.__password = password  # Private

    @property
    def accessemail(self):
        return self._email

    @accessemail.setter
    def accessemail(self, newemail):
        self._email = newemail

    def getpassword(self):
        return self.__password

    def setpassword(self, newpassword):
        self.__password = newpassword
        print(f"Welcome to LinkedIn {self.name}")


kavya = Linkedin('kavya', 'kavya@gmail.com', 'kavya@540')

print(kavya.name)

kavya.name = 'rajitha'

print(kavya.accessemail)

kavya.accessemail = 'rajitha@gmail.com'

print(kavya.getpassword())

kavya.setpassword('30rajitha')
