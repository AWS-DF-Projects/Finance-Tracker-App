from V3_5_build.x2_main_bills_folder.class_bill_set_up import CreateNewBill
from V3_5_build.x0_functions_folder.functions import calender

cne = CreateNewBill
date = calender()
print(date)
# mth  = date.split("_")[0]
# year = date.split("_")[1]
# print(f"Month: {mth}")
# print(f"Year: {year}")
# print((type(year)))
print("")

accounts = {
    'br_2024': {
        "first_name"  : "bill",
        "last_name"   : "reed",
        "password"    : "1111",
        "take_home_£" : 2145.00,
    },
    'br_2025': {
        "first_name": "bill",
        "last_name": "reed",
        "password": "2222",
        "take_home_£": 2255.00,
    },

    'kr_2025': {
        "first_name"  : "kat",
        "last_name"   : "race",
        "password"    : "3333",
        "take_home_£" : 13245.00,
    }
}

bills_db = {
    # Example Bills for 2024
    "br_2024": [
        cne(1, "housing",      545.00, 1,  ["permanent"], True),
        cne(2, "local tax",    158.00, 2,  ["permanent", "utility"], True),
        cne(3, "utilities",    149.25, 5,  ["permanent", "utility"], True),
        cne(4, "water bill",   140.00, 3,  ["permanent", "misc"], True),
        cne(5, "groceries",    210.00, 1,  ["permanent", "misc"], True),
        cne(6, "road tax",     18.10,  2,  ["permanent", "transport"], True),
        cne(7, "car insurance",42.00,  2,  ["permanent", "transport"], True),
        cne(8, "fuel",         47.00,  99, ["permanent", "transport"], True),
        cne(9, "mobile plan",  110.00, 16, ["permanent"], True),
        cne(10,"media license",13.99,  2,  ["permanent"], True),
        cne(11,"investment",   52.25,  2,  ["invest"], True),
        cne(12,"streaming 1",  49.99,  10, ["subscription"], True),
        cne(13,"healthcare",   12.00,  9,  ["subscription"], True),
        cne(14,"streaming 2",  11.99,  10, ["subscription"], True),
        cne(15,"security sub", 6.99,   10, ["subscription"], True),
        cne(16,"cloud hosting",26.00,  16, ["subscription"], False),
        cne(17,"debt plan",    270.00, 2,  ["temporary"], True),
        cne(18,"online course",240.00, 5,  ["temporary", "loan"], True),
        cne(19,"chiropractor", 65.00,  99, ["temporary", "misc"], True),
    ],

    # Example Bills for 2025
    "br_2025": [
        cne(1, "housing",      560.00, 1,  ["permanent"], True),
        cne(2, "local tax",    170.00, 2,  ["permanent", "utility"], True),
        cne(3, "utilities",    140.00, 5,  ["permanent", "utility"], True),
        cne(4, "water bill",   138.00, 3,  ["permanent", "misc"], True),
        cne(5, "groceries",    215.00, 1,  ["permanent", "misc"], True),
        cne(6, "road tax",     18.10,  2,  ["permanent", "transport"], True),
        cne(7, "car insurance",41.00,  2,  ["permanent", "transport"], True),
        cne(8, "fuel",         52.00,  99, ["permanent", "transport"], True),
        cne(9, "mobile plan",  115.00, 16, ["permanent"], True),
        cne(10,"media license",14.00,  2,  ["permanent"], True),
        cne(11,"investment",   48.50,  2,  ["invest"], True),
        cne(12,"streaming 1",  55.00,  10, ["subscription"], True),
        cne(13,"healthcare",   14.99,  9,  ["subscription"], True),
        cne(14,"streaming 2",  11.99,  10, ["subscription"], True),
        cne(15,"security sub", 6.49,   10, ["subscription"], True),
        cne(16,"cloud hosting",25.00,  16, ["subscription"], False),
        cne(17,"debt plan",    275.00, 2,  ["temporary"], True),
        cne(18,"online course",245.00, 5,  ["temporary", "loan"], True),
        cne(19,"chiropractor", 102.00, 99, ["temporary", "misc"], True),
    ],

        #   testing
    "kr_2025": [
        cne(1, 'housing rent',   565.00, 1, ['permanent'],        True),
        cne(2, 'local rates',    159.25, 2, ['permanent'],        True),
        cne(3, 'energy bill',    151.49, 5, ['permanent'],        True),
        cne(4, 'water supply',   143.00, 3, ['permanent', 'misc'],True),
    ],

}

def add_up_common_bills(bills, user):
    total_bills_for_mth = 0
    for bill in bills[user]:
        if getattr(bill,"is_active"):
            # print(bill)
            total_bills_for_mth += getattr(bill, "bill_cost")
    return total_bills_for_mth

add_up_1 = add_up_common_bills(bills_db, "br_2024")
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

access_account("br_2024", "1111", accounts)
access_account("kr_2025", "3333", accounts)
access_account("kd_2025", "2221", accounts)
access_account("br_2025", "2222", accounts)
access_account("br_2025", "2223", accounts)
print("="*100)
check_tag_cost_total("br_2025", bills_db, "subscription", "bill_cost")
check_tag_cost_total("br_2025", bills_db, "permanent", "bill_cost")
check_tag_cost_total("br_2025", bills_db, "car", "bill_cost")

print("")
print(f"Date: {date}")