import pyperclip
class Credentials:

    '''
    class that creates instaces of user accounts
    '''
    credential_list = []


    def __init__(self, username , email , passlock):
    
        self.account = account
        self.email = email
        self.passlock = passlock

        #save
    def save_credential(self):
        '''
        self credentials in credential_list
        '''
        Credentials.credential_list.append(self)

        #delete
     def delete_credential(self):
        '''
        delete credentials 
        '''
        Credentials.credential_list.remove(self)    
        #search
     @classmethod
     def find_account(cls, account):
        '''
        search for accounts
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return credential  

      @classmethod
      def credential_exists(cls, account):
        '''
        confirm a class actually exists
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return True
        return False          


