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