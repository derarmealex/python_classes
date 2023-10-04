class Input_name_pas:
    """
    Pattern of login control: name, password
    ...
    Methods
    -------
    input_name_pas_key_key(name, pas):
        Compare user's input of username and password
        with those stored in internal dictionary -
        - if name and password are stored separately
        {Name="x", Password="y"}
    input_name_pas_key_val(name, pas):
        Compare user's input of username and password
        with those stored in internal dictionary -
        - if name and password are stored together
        {"Name": "Password"}
    """
# TYPE "NAME, PASSWORD"
    def input_name_pas_key_key():
        user = dict(Name="Marek", Password="1234")
        while True:
            n = input("Enter your username: ")
            p = input("Enter your password: ")
            if n == user.get("Name") and user.get("Password") == p:
                print("\n\tWelcome to app! You can go on...\n")
                break
            else:
                print("\t\nUsername or password isn't OK!\n")
# TYPE "NAME: PASSWORD"
    def input_name_pas_key_val():
        user = {'Marek': '1234'}
        while True:
            n = input("Enter your username: ")
            p = input("Enter your password: ")
            if user.get(n) == p:
                print("Welcome to app! You can go on...")
                break
            else:
                print("Username or password isn't OK!")
