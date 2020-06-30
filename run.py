#!/usr/bin/env python3.6
from User import User
from Credentials import Credentials


def create_useraccount(username, email, password):
    '''
    method creates a user account
    '''
    new_user = User(username, email, password)
    return new_user

def save_user(user):
    '''
    method save user  account
    '''
    user.save_user()

def save_credentials(credentials):

    '''
    method save credentials  account
    '''

    credentials.save_credentials

# def find_user(username):
#     '''
#     method for find user using username
#     '''
#     return User.find_user(username)

    # create credentials
def create_credentials(account, email, passlock):
    '''
    method credentials details
    '''
    new_credential = Credentials(account, email, passlock)
    return new_credential
def save_credential(credential):
    '''
    save credentials
    '''
    credential.save_credential()
# def display_cred():
#     '''
#     method to display all the saved credentials
#     '''
#     return Credentials.display_credential()


def find_account(account):
    '''
    method to search for an account
    '''
    return Credentials.find_account(account)


def delete_credential(account):
    '''
    method to delete account
    '''
    account.delete_credential()

def main():
    print("Hello Welcome to your password locker. What is your name?")
    username = input()

    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:
      print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")
       
      short_code = input().lower()

      if short_code == 'cc':
            print("Creating account...")
            print("Key in these details:")
            print("Username: ")
            username = input()

            print("Password: ")
            password = input()

            print("Email: ")
            email = input()

            save_user(create_useraccount(username,email, password))
            print('\n')
            print(f"{username}'s Account information: ")
            print(f"Username: {username} , Password:{password} , Email:{email}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("*" * 80)

      elif short_code == 'dc':

        if display_user():
            print("Here is a list of all your contacts")
            print('\n')

            for user in display_user():
                 print(f"{user.username} {user.email} .....{user.password}")

                 print('\n')
        else:
                print('\n')
                print("You dont seem to have any account saved yet")
                print('\n')

      else:
                print("That contact does not exist")

       elif short_code == "ex":
        print("Bye .......")
        break
       else:
        print("I really didn't get that. Please use the short codes")