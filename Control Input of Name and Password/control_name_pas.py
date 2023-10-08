class InNamePas:
    """
    Pattern of log-in control: name, password
    ...
    Methods
    -------------------------------------------------
    key_key():
        Compare user's input of username and password
        with those stored in internal dictionary -
        - if name and password are stored separately
        {Name="x", Password="y"}
    key_val():
        Compare user's input of username and password
        with those stored in internal dictionary -
        - if name and password are stored together
        {"Name": "Password"}
    """
    def __init__(self):
        """
        set attributes for InNamePas
        ...
        Attributes
        ----------------------------
        """
    def input_ctr(self):
        name = input("Enter your username: ")
        pas = input("Enter your password: ")
        yield name
        yield pas

#    def key_key(self):
#        user = dict(Name="Marek", Password="1234")
#        while True:
#            n = input("Enter your username: ")
#            p = input("Enter your password: ")
#            if n == user.get("Name") and user.get("Password") == p:
#                print("\n\tWelcome to app! You can go on...\n")
#                print("{}".format(self.text))
#                break
#            else:
#                print("\n\tUsername or password isn't OK!\n")

#    def key_val(self):
#        user = {'Marek': '1234'}
#        while True:
#            n = input("Enter your username: ")
#            p = input("Enter your password: ")
#            if user.get(n) == p:
#                print("\n\tWelcome to app! You can proceed...\n")
#                print("{}".format(self.text))
#                break
#            else:
#                print("\n\tUsername or password isn't OK!\n")
