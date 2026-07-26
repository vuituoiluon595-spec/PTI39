#user : full name , birthdate, esername , email , password, gender
class user:
    def __init__ (self, full_name, birthdate, username, password, gender):
        self._full__name = full_name
        self,birthdate = birthdate
        self.username = username
        self.password = password
        self.gender = gender


    #getter methods 
    def get_full_name(self):
        return self.full_name
    def get_birthdate(self):
        return self._birthdate
    def get_username(self):
        return self.get_username
    def get_email(self):
            return self.get_email 
    def get_password(self):
            return self.get_password 
    def get_gender(self):
            return self.get_gender 
    #setter methods 
    #sua gioi tinh 
    #sua username(user>6 ki tu)
    def set_username(self, username):
         if len(username)>6:
              self._username = username
         else:
             print("Username must be longer than 6 characters.")
    
    #sua password(password tren 6ki tu)
    def set_password(self, old_password,new_password):
        if    old_password == self._password: 
             if len(new_password)>6:
                  self._password = new_password
             else:
                 print("New password must be longer than 6 characters.")
        else:
             print("old password is incorrect.")
    #gender (male, famle. other)
    def set_genser(self, gender):
        if gender in ['male','famle','gender']:
            self.__gender = gender
        else:
            print("invalid gender.plsease choose from 'male','female',or'other'.")