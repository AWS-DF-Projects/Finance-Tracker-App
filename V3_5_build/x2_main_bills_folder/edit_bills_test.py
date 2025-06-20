from V3_5_build.x2_main_bills_folder.class_bill_set_up import CreateNewBill
from V3_5_build.x2_main_bills_folder.set_up_bills import edit_bills, print_bills, add_tags
from V3_5_build.x0_functions_folder.functions import HelperTools as Ht

class BillDataBase:
    def __init__(self):
        self.bills_db = {
            "br": [
                    CreateNewBill(1, "rent", 570, 1, ["Permanent"], True),
                    CreateNewBill(2, "council tax", 161, 2, ["Permanent"], True),
                    CreateNewBill(3, "gas & elec", 157.12, 5, ["Permanent"], True),
                    CreateNewBill(4, "water", 150, 3, ["Permanent", "kt"], True),
            ],
            "kr": [
                    CreateNewBill(1, "mortgage", 670, 1, ["Permanent"], True),
                    CreateNewBill(2, "council tax", 161, 2, ["Permanent"], True),
                    CreateNewBill(3, "gas & elec", 157.12, 5, ["Permanent"], True),
                    CreateNewBill(4, "water", 150, 3, ["Permanent", "df"], True),
            ],
        }

    @staticmethod
    def edit_container(self, user_name):
        #   Get the DB for the USER
        d_base = self.db.get(user_name)
        print(f"User: {user_name.upper()}")
        print(f"Data Base: {db}\n")

        #  Input the ID number
        bill_id_selected = 1 - 1

        #  Display the line
        edit_bill = d_base[bill_id_selected]

        print(f"Edit Line ID: {edit_bill}")

        #  Bills list
        cat_list = {
            "1": "bill_name",
            "2": "bill_cost",
            "3": "bill_date",
            "4": "bill_tags",
            "5": "is_active"
        }
        # What do you want to edit?
        print("What do you want to edit: ")
        for index, cat in enumerate(cat_list.items()):
            print(f"  {index + 1}: {' '.join((cat[1].split('_'))).capitalize()}")
        print("")
        edit = Ht.check_list(input("Please select 1,2,3,4,5: "), ["1", "2", "3", "4", "5"])
        selected = cat_list[edit]
        print(f"Edit: {' '.join(selected.split('_')).capitalize()}")

        update_value = ""
        if edit   == "1":
            update_value = input("Please update Name: ")
        elif edit == "2":
            update_value = input("Please update Amount: ")
        elif edit == "3":
            update_value = input("Please update Date: ")
        elif edit == "4":
            update_value = add_tags()
        elif edit == "5":
            ip = Ht.check_list(input(f"Is {selected} still active? (Enter y or n) "), ["y", "n"])
            if ip == "y":
                update_value = "True"
            else:
                update_value = "False"

        print(f"  Edit: {selected} => {update_value}")
        setattr(edit_bill,selected, update_value)

        print(f"\nUser: {user_name}")
        for bill in d_base:
            print(f"  Bills: {bill}")


        ## ------------------- Outer Scope-------------------------------
b_db = BillDataBase()
b_db.edit_container(b_db,"br")
# edit_container(db_2, "kt")

print("")
print("-" * 78)
for user, db in bills_db.items():
    text_edit(f"Main DB User: {user}",'', 'ul')
    print_bills(db)
    print("")

