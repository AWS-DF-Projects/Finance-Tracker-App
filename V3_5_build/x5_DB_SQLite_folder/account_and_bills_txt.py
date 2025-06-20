from V3_build.x2_main_bills_folder.class_bill_set_up import CreateNewBill as Cne
from V3_build.x0_functions_folder.functions import HelperTools as Ht

date = Ht.calender()
mth  = date.split("_")[0]
year = date.split("_")[1]
print(f"Month: {mth}")
print(f"Year: {year}")
# print((type(year)))
print("")

accounts = {
    'df_2024': {
        "first_name"  : "darren",
        "last_name"   : "fawcett",
        "password"    : "1111",
        "take_home_£" : 2345.00,
    },
    'df_2025': {
        "first_name": "darren",
        "last_name": "fawcett",
        "password": "2222",
        "take_home_£": 2345.00,
    },

    'kf_2025': {
        "first_name"  : "katie",
        "last_name"   : "finch",
        "password"    : "3333",
        "take_home_£" : 1345.00,
    }
}
    # ****  NEED TO UPDATE THE CLSSS FOR YEAR, MONTH, USER ID ECT ****
bills_db = {
    #                    bills 2024
    "df_2024": [
        Cne(1, "rent",        550.00,1, ["permanent"           ],True),
        Cne(2, "council tax", 161.69,2, ["permanent", "utility"],True),
        Cne(3, "gas & elec",  157.82,5, ["permanent", "utility"],True),
        Cne(4, "water",       150.00,3, ["permanent", "kt"     ],True),
        Cne(5, "kt food",     200.00,1, ["permanent", "kt"     ],True),
        Cne(6, "car tax",     16.62, 2, ["permanent", "car"    ],True),
        Cne(7, "car insure",  42.40, 2, ["permanent", "car"    ],True),
        Cne(8, "fuel",        50.00, 99,["permanent", "car"    ],True),
        Cne(9, "tesco mob",   113.0, 16,["permanent"           ],True),
        Cne(10,"tv license",  15.00, 2, ["permanent"           ],True),
        Cne(11,"foresters",   51.00, 2, ["invest"              ],True),
        Cne(12,"sky tv",      51.60, 10,["subscription"        ],True),
        Cne(13,"dentist",     15.00, 9, ["subscription"        ],True),
        Cne(14,"youtube",     12.99, 10,["subscription"        ],True),
        Cne(15,"ring sub",    7.99,  10,["subscription"        ],True),
        Cne(16,"aws S/B",     28.00, 16,["subscription"        ],False),
        Cne(17,"IVA",         279.00,2, ["temporary"           ],True),
        Cne(18,"course",      250.00,5, ["temporary", "loan"   ],True),
        Cne(19,"chiro",       70.00, 99,["temporary", "kt"     ],True),
    ],

    #                           Current Bills after April 2025
"df_2025": [
        Cne(1, "rent",        570.00,1, ["permanent"           ],True),
        Cne(2, "council tax", 173.69,2, ["permanent", "utility"],True),
        Cne(3, "gas & elec",  148.82,5, ["permanent", "utility"],True),
        Cne(4, "water",       150.00,3, ["permanent", "kt"     ],True),
        Cne(5, "kt food",     200.00,1, ["permanent", "kt"     ],True),
        Cne(6, "car tax",     16.62, 2, ["permanent", "car"    ],True),
        Cne(7, "car insure",  42.40, 2, ["permanent", "car"    ],True),
        Cne(8, "fuel",        50.00, 99,["permanent", "car"    ],True),
        Cne(9, "tesco mob",   113.0, 16,["permanent"           ],True),
        Cne(10,"tv license",  15.00, 2, ["permanent"           ],True),
        Cne(11,"foresters",   50.00, 2, ["invest"              ],True),
        Cne(12,"sky tv",      57.60, 10,["subscription"        ],True),
        Cne(13,"dentist",     16.96, 9, ["subscription"        ],True),
        Cne(14,"youtube",     12.99, 10,["subscription"        ],True),
        Cne(15,"ring sub",    7.99,  10,["subscription"        ],True),
        Cne(16,"aws S/B",     28.00, 16,["subscription"        ],False),
        Cne(17,"IVA",         279.00,2, ["temporary"           ],True),
        Cne(18,"course",      250.00,5, ["temporary", "loan"   ],True),
        Cne(19,"chiro",       109.00,99,["temporary", "kt"     ],True),
    ],
        #   testing
    "kf_2025": [
        Cne(1, 'Rent',        570.00,1,['permanent'],           True),
        Cne(2, 'council tax', 161.00,2,['permanent'],           True),
        Cne(3, 'gas & elec',  157.12,5,['permanent'],           True),
        Cne(4, 'water',       150.00,3,['permanent, kt'],       True),
    ],
}

def add_up_common_bills(bills, user):
    total_bills_for_mth = 0
    for bill in bills[user]:
        if getattr(bill,"is_active"):
            # print(bill)
            total_bills_for_mth += getattr(bill, "bill_cost")
    return total_bills_for_mth

add_up_1 = add_up_common_bills(bills_db, "df_2024")
add_up_2 = add_up_common_bills(bills_db, "df_2025")
print(f"Total Active Bills for {int(year) -1} come to: £{add_up_1:.2f}")
print(f"Total Active Bills for {int(year)} come to: £{add_up_2:.2f}")
print("=" * 100)
print(f"Total Difference between {int(year) -1} and {int(year)}: £{(add_up_2 - add_up_1):.2f}\n")


def access_account(user, pass_w, acc):
    try:
        if accounts[user]["password"] == pass_w:
            print(f"Welcome {(acc[user]['first_name']).capitalize()} {(acc[user]['last_name']).capitalize()} here's your bills:")
            print(bills_db.get(user, []))
            print("")
        else:
            print("User or Password dont match!!!!")
    except KeyError:
            print(f"There seems to be an error, User: '{user}' may not exist!!\n")

def check_tag_cost_total(user, bills, tag, field):
    total_tag_cost = 0
    print(f"Here's the '{' '.join(tag.split('_')).capitalize()}'tag bills:")
    for bill in bills[user]:
        if getattr(bill,"is_active"):
            if tag in getattr(bill,"bill_tags"):
                total_tag_cost += getattr(bill, field)
                print(f"  - {getattr(bill, 'bill_name')}: £{getattr(bill, 'bill_cost'):.2f}")
    print("_"*28)
    print(f"Totaling £{total_tag_cost:.2f} per month.")
    print("_"*28)


    return total_tag_cost

access_account("df_2024", "1111", accounts)
access_account("kf_2025", "3333", accounts)
access_account("kd_2025", "2221", accounts)
access_account("df_2025", "2222", accounts)
access_account("df_2025", "2223", accounts)
print("="*100)
check_tag_cost_total("df_2025", bills_db, "subscription", "bill_cost")
check_tag_cost_total("df_2025", bills_db, "permanent", "bill_cost")
check_tag_cost_total("df_2025", bills_db, "car", "bill_cost")

print("")
print(f"Date: {date}")