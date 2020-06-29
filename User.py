class User:
    """
    Class that generates new instances of user.
    """

    User_list = [] # Empty contact list

    def __init__(self,username,email,password):

      # docstring removed for simplicity

        self.username = username
        self.email = email
        self.password = password
    