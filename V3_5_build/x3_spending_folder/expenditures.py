from class_expenditures import CreateNewExpenditure
from V2_build.x0_functions_folder.functions import calender
cne = CreateNewExpenditure

expenditures_db = {
    "df": {
        "3_2025": {
            "take_home": 2388.33,
            "spending": [
                cne("1",  "Kt",            15.00, 1,  ["owed", "transfer", "kt"]),
                cne("2",  "Tesco Kt",      20.00, 2,  ["food", "kt", "transfer"]),
                cne("3",  "AWS",           0.03,  3,  ["course", "aws", "learn"]),
                cne("4",  "Cash machine",  40.00, 12, ["take_away", "cash_withdrawal"]),
                cne("5",  "Sainsbury's",   40.00, 13, ["fuel", "car"]),
                cne("6",  "Tesco Kt",      20.00, 15, ["food", "kt", "transfer"]),
                cne("7",  "Tesco Kt",      40.00, 15, ["food", "kt", "transfer"]),
                cne("8",  "Cash machine",  30.00, 19, ["take_away", "cash_withdrawal"]),
                cne("9",  "Farm foods",    47.93, 20, ["food"]),
                cne("10", "Audible",       0.99,  24, ["e_book"]),
                cne("11", "Funky Pigeon",  7.29,  27, ["event_card"]),
                cne("12", "Taco Bell",     19.37, 27, ["take_away"]),
                cne("13", "Simply Chiro",  35.00, 27, ["chiro"]),
                cne("14", "YT film",       3.49,  31, ["entertainment"]),
                cne("15", "Tesco Express", 4.00,  31, ["store", "junk_food"]),
            ],
        },
        "4_2025": {
            "take_home": 2389.95,
            "spending": [
                cne("1",  "Cash",          30.00, 2,  ["takeaway", "cash_withdrawal"]),
                cne("2",  "Tesco Express", 6.75,  4,  ["store", "junk_food"]),
                cne("3",  "Decathlon",     25.97, 6,  ["maintenance", "bicycle"]),
                cne("4",  "Sainsbury's",   50.00, 6,  ["fuel", "car"]),
            ],
        }
    },
# ----------------------------------------------------------------------------------------------------------------#
    "kt": {
        "3_2025": {
            "take_home": 1388.33,
            "spending": [
                cne("12", "Taco Bell",     19.37, 27, ["take_away"]),
                cne("13", "Simply Chiro",  35.00, 27, ["chiro"]),
                cne("14", "YT film",       3.49,  31, ["entertainment"]),
                cne("15", "Tesco Express", 4.00,  31, ["store", "junk_food"]),
            ],
        },
        "4_2025": {
            "take_home": 1389.95,
            "spending": [
                cne("1",  "Cash",          30.00, 2,  ["takeaway", "cash_withdrawal"]),
                cne("2",  "Tesco Express", 6.75,  4,  ["store", "junk_food"]),
                cne("3",  "Decathlon",     25.97, 6,  ["maintenance", "bicycle"]),
                cne("4",  "Sainsbury's",   50.00, 6,  ["fuel", "car"]),
                cne("5",  "Sainsbury's",   50.00, 6,  ["fuel", "car"]),
                cne("6",  "Sainsbury's",   50.00, 6,  ["fuel", "car"]),
            ],
        }
    }
}
#
# *************************    ^^ DB ^^   *******************************
#-------------------------------------------------------------------------------------------------------------#
# ************************ vv FUNCTIONS vv ******************************
def test_display(us, dt, ad):
    print("_________________________________________>")
    print(f"Date: {us}")
    print(f"Month data: {dt}")
    print(f"Expenditures: {ad}")
    print("_________________________________________>")


def test_add_expense(add_id, add_name, add_cost, add_date, add_tags):
    return cne(add_id, add_name, add_cost, add_date, add_tags)


def sum_up_exp_per_mth(expend_data):
    print(expend_data)
    last_3_mth_expend = []
    total_exp_mth = 0
#  ------------------------------------------- needs fix

    for lst in expend_data:
        total_exp_mth += (getattr(lst, "exp_cost"))
    last_3_mth_expend.append(total_exp_mth)
    # print(f"Total: {total_exp_mth:.2f}")
    return last_3_mth_expend

#-------------------------------------------------------------------------------------------------------------#
cur_user = "df"
# date = "3_2025"
date = calender()

user     = expenditures_db[cur_user]
mth_bd   = user[date]
expenses = mth_bd["spending"]
test_display(user, mth_bd, expenses)    ## Prints

# test_add_expense(expenses)
print(f"\nExp List for Month {date}  : {expenses[-1]}\n")


e_id   = len(expenses) + 1
ex_nm  = "TEST"
ex_cst = 99.99
ex_dt  = 10
ex_tgs = ["test", "testing"]

expenses.append(test_add_expense(e_id, ex_nm, ex_cst, ex_dt, ex_tgs))
test_display(user, mth_bd, expenses)    ## Prints
print(expenses[-1])





def display(db):
    last_3_wages      = []

    current_user = "df"
    dis_user = expenditures_db[current_user]

    for dis_date, info in dis_user.items():

        wage    = info.get("take_home")
        expend  = info.get("spending")
        mth_fmat = " ".join(dis_date.split("_"))
        last_3_wages.append(wage)

        print(f"{mth_fmat} Wage: {wage}")
        print(f"Wage: £{'{:.2f}'.format(wage)}")
        # print(f"Expends:   £{expend}")
        print("")


def lock():
    print("-" * 75)
    for index,wage in enumerate(last_3_wages, start=1):
        print(f"Wage {index}: {wage}")
    print("")
    for index,mth in enumerate(last_3_mth_exp, start=1):
        print(f"Expenditure month {index}: £{mth:.2f}")

# display(expenditures_db)


