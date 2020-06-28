import unittest
from password import Password


class TestPassword(unittest.TestCase):

     def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = password("virginiah2020","wamuyu")
