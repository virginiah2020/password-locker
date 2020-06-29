import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase)

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_cred = Credentials("Github", "vancycy254@gmail.com", "111222")
    def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credentials.cred_list = []

      #intiailizing
     def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_credential.account, "GitHub")
        self.assertEqual(self.new_credential.email, "vancyvy254@gmail.com")
        self.assertEqual(self.new_credential.passlock, "111222")

        #save
     def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)

     def test_saving_multiple_creds(self):
        '''
        check if users can store multiple credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Facebook", "testuser","password")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)

        #delete
    def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Facebook", "testuser","password")
        test_credential.save_credential()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credential_list), 1)


        #search

    def test_search_for_credential(self):
        '''
        test if credentials can be searched for
        '''
        self.new_cred.save_credential()
        test_credential = Credentials("Twitter", "testuser","password")
        test_credential.save_credential()
        find_credential= Credentials.find_account("Twitter")
        self.assertEqual(find_credential.account, test_credential.account)

      #confirm credential
    def test_confirm_credential_exists(self):
        '''
        confirm that credentials actually exists
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Twitter", "testuser","password")
        test_credential.save_credential()
        cred_exists = Credentials.credential_exists("Twitter")
        self.assertTrue(credential_exists)

        
    def test_display_credentials(self):
        '''
        test if all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_credential(), Credentials.credential_list)

    def test_copy_password(self):
        '''
        test whether generated password can be copied
        '''
        self.new_credential.save_credential()
        Credentials.copy_passlock("111222")
        self.assertEqual(self.new_credential.passlock, pyperclip.paste())            
