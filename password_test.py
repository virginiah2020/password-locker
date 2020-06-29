import unittest
from password import Password


class TestPassword(unittest.TestCase):

     def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = password("virginiah2020","virgy@gmail","wamuyu")

     def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_password.username,"Virginiah2020")
            self.assertEqual(self.new_password.email,"virgy@gmail")
            self.assertEqual(self.new_password.password,"wamuyu")

     def test_save_multiple_passwords(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list
            '''
            self.new_password.save_password()
            test_password = Password("Test","password","test@gmail") # new contact
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)
            #delete password
     def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","test@gmail") # new contact
            test_password.save_password()

            self.new_password.delete_password()# Deleting a contact object
            self.assertEqual(len(Password.password_list),1)

     def delete_password(self):

        '''
        delete_password method deletes a saved password from the password_list
        '''

        Password.password_list.remove(self)

     if __name__ == '__main__':
     unittest.main()


