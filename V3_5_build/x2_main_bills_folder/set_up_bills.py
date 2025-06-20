from V3_5_build.x2_main_bills_folder.class_bill_set_up import CreateNewBill
from V3_5_build.x0_functions_folder.functions import HelperTools
import re
import fuzzywuzzy
from fuzzywuzzy import fuzz
h_tool = HelperTools()

cnb = CreateNewBill
class BillDataBase:
    def __init__(self):
        self.bills_list = {
            "df": [
                CreateNewBill(1,"rent",       570.00,1, ["Permanent"],      True),
                CreateNewBill(2,"council tax",161.00,2, ["Permanent"],      True),
                CreateNewBill(3,"gas & elec", 157.12,5, ["Permanent"],      True),
                CreateNewBill(4,"water",      150.00,3, ["Permanent", "kt"],True),
            ],
            "kt": [
                CreateNewBill(1, "mortgage",   670.00,1,["Permanent"],      True),
                CreateNewBill(2, "council tax",161.00,2,["Permanent"],      True),
                CreateNewBill(3, "gas & elec", 157.12,5,["Permanent"],      True),
                CreateNewBill(4, "water",      150.00,3,["Permanent", "df"],True),
            ],
        }
        self.common_bill_List = {
            "house_hold_bills": ["Rent/Mortgage", "Gas & Electric", "Water", "Council Tax" ],
            "common_bills"    : ["Internet", "Mobile Phone", ],
            "transport_bills" : ["Fuel", "Insurance", "Car Finance", "Car Tax"],
            "subs"            : ["Youtube", "Netflix", "Sky", ],
        }
        self.tags_list = {
            "1": "permanent", "2": "utility", "3": "subscription", "4": "invest", "5": "loan", "6": "car",
            "7": "food", "8": "temporary", "9": "custom", "": "", "x": "To end adding tags.",
        }
        self.key_list = {
            "1": "bill_name","2": "bill_cost","3": "bill_date","4": "bill_tags","5": "is_active"
        }

# -----------------------------------------------------------------------------------------------------------------
#                                 >>>>>>>>>>>>>>>>>> FUNCTIONS <<<<<<<<<<<<<<<<<<<<<<
# -----------------------------------------------------------------------------------------------------------------
    def length_of_bill_db(self, user):
        try:
            return len(self.bills_list[user])
        except Exception as e:
            print(f"⚠️ Sorry there seems to be an issue. {e}")
# -----------------------------------------------------------------------------------------------------------------
    def add_tags(self):
        try:
            return_tags = []                                                     # save the tags in a list
            print(f"Here are some common tags:")                                 # Print message
            for tag in self.tags_list.items():                                   # loop through the tags dict
                 print("") if tag[0] == "" else print(f"  {tag[0]}: {tag[1].capitalize()}") # print tags key: value                                                 # space out the print display
            print("")                                                            # Print the space
            add_tag = h_tool.check_blank_input(
                "Please add up to 3 tags (eg. 256 = common, loan, car)")         # ask for nums
            if add_tag.strip().lower() == "x":                                   # Checks for "x" to Exit
                return return_tags                                               # if so returns []
            tag_nums_set = set()                                                 # store the 3 digits
            tag_nums_lst = []                                                    # store the 3 digits
            for char in add_tag:                                                 # Loop through the add_tag input
                if char.isdigit() and char not in tag_nums_set:                  # Take first 3 digits, and check inf in tag_nums_set
                    tag_nums_set.add(char)                                       # add char to tag_nums
                    tag_nums_lst.append(char)                                       # add char to tag_nums
                if len(tag_nums_lst) == 3:                                            # check if tag_nums length is 3
                    break                                                        # if so break
            tag_nums_lst.sort()                                                  # sort the list 543 -> 345 for uniform tagging
            for t in tag_nums_lst:                                               # loop through the tag nums
                if t in ["1", "2", "3", "4", "5", "6", "7", "8"]:                # Check the numbers str(1-9)
                    return_tags.append(self.tags_list[t])                        # append the tag to the return tags
                elif t == "9":                                                   # if "9" input custom tag
                    cust_tag = h_tool.check_input_len(
                        "Please enter custom tag", 3, 9)  # if so get custom tag
                    return_tags.append(cust_tag)                                 # Return the custom tag
            print(f"  Tags: {", ".join(return_tags)}")                           # Print the tags as a set
            return return_tags                                                   # return the list as a set then put back as a list
        except Exception as e:
            print(f"⚠️ Sorry there seems to be an issue. {e}")                   # catch any errors
    # b_db.add_tags()
# -----------------------------------------------------------------------------------------------------------------
    def add_bill(self, user, bill):
        try:
            ad_user = self.bills_list.get(user)
            index = self.length_of_bill_db(user) + 1
            active = True
            name = bill
            cost = h_tool.check_number("  Cost per month £: ", float)
            date = h_tool.check_number("  Date bills due (eg. 16 = 16th): ", int)
            is_active = h_tool.check_list(input("  Is this bill currently active? (y/n): "), ["y", "n"], str)
            if is_active == "n":
                active = False
            tags = self.add_tags()
            ad_user.append(cnb(index, name, cost, date, tags, active))
        except Exception as e:
            print(f"⚠️ Sorry there seems to be an issue. {e}")

# -----------------------------------------------------------------------------------------------------------------
    def common_bills_display(self):
        try:
            print(h_tool.text_edit("Here are some common house hold bills -", "bold", False))
            for num, bill_list in enumerate(self.common_bill_List, start=1):
                print(f"  {num}: {' '.join(re.split(r'_', bill_list.capitalize()))}")
            print(" ")
        except Exception as e:
            print(f"⚠️ Sorry there seems to be an issue. {e}")
# -----------------------------------------------------------------------------------------------------------------

    def print_bills(self, user):
        try:
            user = self.bills_list.get(user)
            print("  "+ "-" * 74)
            print("  ID  | Name           | Cost     | Due Date | Tags                 | Active")
            print("  " + "-" * 74)
            for bill in user:
                tag_str = ", ".join(bill.bill_tags)
                print(
                    f"  {bill.bill_id:<3} | {bill.bill_name:<14} | £{float(bill.bill_cost):<7.2f} | {bill.bill_date:<8} | {tag_str:<20} | {bill.is_active}")
        except Exception as e:
            print(f"An Error occurred: {e}")
# -----------------------------------------------------------------------------------------------------------------
    def edit_bill(self, user):
        try:
            d_base = self.bills_list.get(user)                                               # get DB for user
            print(f"User: {user.upper()}")                                                   # Display the User
            self.print_bills(user)                                                           # Print the bills
            num_lst = list(range(1, self.length_of_bill_db(user)+1))                         # Get the list of nums
            print(f"Num list: {num_lst}")

            print("\nWhich bill do you want to edit?")
            bill_id_selected = h_tool.check_list("Select Bill ID: ", num_lst, int)   # Ask for ID number for Edit
            bill_id_correction = bill_id_selected - 1                                        # correct the index
            edit_bill = d_base[bill_id_correction]                                           # Get ID for Edit
            s_nm = getattr(edit_bill,'bill_name')                                            # Get the Name of bill
            print(f"  You selected:  {s_nm.capitalize()}\n")                                 # Show selection

            print("What do you want to edit: ")
            for index, cat in enumerate(self.key_list.items(),start=1):                      # Loop through the categories
                print(f"  {index}: {cat[1].split('_')[1].capitalize()}")                     # Print the categories
            print("")
            edit = h_tool.check_list(input("Please select 1,2,3,4,5: "), ["1", "2", "3", "4", "5"], str)
            selected = self.key_list[edit]
            print(f"Edit: {' '.join(selected.split('_')).capitalize()}")

            update_value = ""
            if edit == "1":
                update_value = input("Please update Name: ")
            elif edit == "2":
                update_value = input("Please update Amount: ")
            elif edit == "3":
                update_value = input("Please update Date: ")
            elif edit == "4":
                update_value = self.add_tags()
            elif edit == "5":
                ip = h_tool.check_list(f"Is {selected} still active? (Enter y or n) ", ["y", "n"], str)
                update_value = "True" if ip == "y" else "False"
            print(f"  Edit: {selected} => {update_value}")
            setattr(edit_bill, selected, update_value)
            self.print_bills(user)
        except Exception as e:
            print(f"⚠️ Sorry there seems to be an issue. {e}")


# -----------------------------------------------------------------------------------------------------------------
#                        **************************** TEST FUNCTIONS ****************************
# -----------------------------------------------------------------------------------------------------------------

c_user = "df"
b_db = BillDataBase()

def test_bill_grouping():
    """Test function to help understand bill grouping"""
    # First, let's understand how fuzzywuzzy works
    print("\nTesting string similarity:")
    test_strings = [
        ("gas & elec", "gas and electric"),
        ("council tax", "council tax bill"),
        ("water bill", "water payment"),
        ("rent", "rent payment")
    ]
    
    for str1, str2 in test_strings:
        similarity = fuzz.ratio(str1.lower(), str2.lower())
        print(f"'{str1}' vs '{str2}': {similarity}% similar")
    
    # Now let's test with actual bills
    print("\nTesting with actual bills:")
    bills = b_db.bills_list[c_user]
    
    # Let's look at each bill and find similar ones
    for i, bill1 in enumerate(bills):
        print(f"\nChecking similarities for: {bill1.bill_name}")
        for j, bill2 in enumerate(bills[i+1:], start=i+1):
            # Calculate similarity scores
            name_similarity = fuzz.ratio(bill1.bill_name.lower(), bill2.bill_name.lower())
            cost_diff = abs(bill1.bill_cost - bill2.bill_cost) / max(bill1.bill_cost, bill2.bill_cost)
            date_diff = abs(bill1.bill_date - bill2.bill_date)
            
            print(f"  Comparing with {bill2.bill_name}:")
            print(f"    Name similarity: {name_similarity}%")
            print(f"    Cost difference: {cost_diff*100:.1f}%")
            print(f"    Date difference: {date_diff} days")

# Uncomment to run the test
# test_bill_grouping()

# -----------------------------------------------------------------------------------------------------------------
    #  ********** FOR TESTING **************
    # def main_bills_funcion(self):
    #     bills_list = common_bills(common_bill_List)
    #     print("")