class Password:
    """
    Password that generates new instances of passwords.
    """

    Password_locker = [] # Empty contact list

    def __init__(self,username,email,password):

      # docstring removed for simplicity

        self.username = username
        self.email = email
        self.password = password
    