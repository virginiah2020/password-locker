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
            self.assertEqual(self.new)new_password.password,"wamuyu")

         def test_save_multiple_passwords(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list

    if __name__ == '__main__':
    unittest.main()


