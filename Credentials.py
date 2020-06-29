import pyperclip
class Credentials:

    '''
    class that creates instaces of user accounts
    '''
    credential_list = []


    def __init__(self, username , email , passlock):
    
        self.username = username
        self.email = email
        self.passlock = passlock

