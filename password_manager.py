# To write a password manager that will generate new password for user as well as stores every new password 
# create a class password manager
# receive length of password
# generate new password of length with rndom characters 
# store and allow for retrieve

import random


class PasswordManager:
    def __init__(self):
        self.characters = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        self.savedp_dictionary = {}
        
    def generate_new_password(self, key, length):
        password = ''
        
        for no in range(length):
            random_chr = random.randint(0, len(self.characters))
            password += self.characters[random_chr]
            
        self.savedp_dictionary[key] = password
        return f"{key} password is {password}"
    
    def retrieve_saved_password(self, key):
        if key in self.savedp_dictionary:
            return f"Your password for {key} is {self.savedp_dictionary[key]}"
        else:
            return "Not Found"
            
PM = PasswordManager()
get = PM.generate_new_password('facebook', length=8)
retrieve = PM.retrieve_saved_password('facebook')
print(get)
print(retrieve)