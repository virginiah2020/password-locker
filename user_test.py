import unittest
from user import User
class TestUser(unittest.TestCase):


class TestUser(unittest.TestCase):

     def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("virginiah2020","virgy@gmail","wamuyu")

     def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_user.username,"Virginiah2020")
            self.assertEqual(self.new_user.email,"virgy@gmail")
            self.assertEqual(self.new_user.password,"wamuyu")

            #save 
     def test_save_multiple_users(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","password","test@gmail") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

            #delete password
     def test_delete_contact(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","test@gmail") # new contact
            test_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_list),1)

     def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

        #find user
     def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("test", "password","test@gmail")
        test_user.save_user()
        found_user = User.find_user("virginiah2020")
        self.assertEqual(found_user.username, self.new_user.username)

        def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Contact.display_contacts(),Contact.contact_list)


     if __name__ == '__main__':
      unittest.main()


