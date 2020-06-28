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
            self.assertEqual(self.new_password.first_name,"James")
            self.assertEqual(self.new_contact.last_name,"Muriuki")
            self.assertEqual(self.new_contact.phone_number,"0712345678")
            self.assertEqual(self.new_contact.email,"james@ms.com")


