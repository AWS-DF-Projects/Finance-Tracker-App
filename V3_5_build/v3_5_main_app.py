from V3_5_build.x5_DB_SQLite_folder.create_db import create_db
from V3_5_build.x0_functions_folder.functions import HelperTools as Ht
from V3_5_build.x1_account_folder.class_for_account import CreateNewAccount as Cna

print("Welcome to the Python Finance Tracker!!")
print("Do you want to 1 - Sign In or 2 - sign Up?")
sign_up_in = int(input("Enter 1 or 2: "))

if sign_up_in == 1:
    print("We need some details.")
    e_user = input("Please Enter your Username")
    e_pass = input("Please Enter your Password")
elif sign_up_in == 2:
    create_db()
    def add_new_acc(self):
        try:
            f_name = Ht.check_blank_input("  First name")              # get input str
            l_name = Ht.check_blank_input("  Last name ")              # get input str
            u_name = Ht.check_blank_input("  User name ")              # get input str
            p_word = Ht.check_blank_input("  Password  ")              # get input str
            m_wage = Ht.check_number("  Take home ", float)  # get input float
            new_user = Cna(f_name, l_name, u_name, p_word, m_wage)     # save new user to variable
            self.accounts[new_user.user_name] = new_user               # set new user as tag and account
            return u_name                                              # return user for applying self.current_user
        except Exception as e:
            print(f"⚠️ Sorry there seems to be an issue. {e}")