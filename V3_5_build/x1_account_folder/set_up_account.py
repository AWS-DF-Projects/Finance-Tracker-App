from V3_5_build.x1_account_folder.class_for_account import CreateNewAccount as Cna

class CreateAccountFunctions:
    def __init__(self):
        self.keys = [
            "first_name", "last_name", "user_name", "password", "take_home"
        ]
        self.current_user = ""

    #  Create Account Function
    #  Check Account Function / Check user and password match return userID
    #  Display Account Function    /  print some text for account
    #  Edit Account Function
    #  Delete Account Function
