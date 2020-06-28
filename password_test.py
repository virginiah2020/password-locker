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

    if __name__ == '__main__':
    unittest.main()


