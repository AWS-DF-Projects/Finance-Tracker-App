import re
# re.sub(pattern, replacement, text)

bill_list = [
    "vis int'l 0016350219 aws emea  aws.amazon.co  usd 0.44 @   visa rate 0.35",
    "vis int'l 0051896991 tbl* learn.cantril  amsterdam  usd 24.00 @   visa rate 19.46",
    "vis int'l 0051896992 tbl* learn.cantril  amsterdam  usd 24.00 @   visa rate 19.46",
    "vis google *youtube",
    "g.co/helppay# 12.99",
    "asda york 1,@13:52 30.00 85.19",
]





def remove_symbols(line):
    print(f"Before: {line}")
    time_pattern  = r"@\d{2}\:\d{2}"
    line = re.sub(time_pattern, "", line).strip()
    print(f"After:  {line}")


print("checking lines...")
time_pattern  = r"@\d{2}\:\d{2}"
for l in bill_list:
    # print(l)
    time_group = re.search(time_pattern, l)
    if time_group:
        remove_symbols(l)



def convert_usd_gbp(line):
    usd_pattern = r"usd\s+\d+\.\d{2}"
    usd_search = re.search(usd_pattern, line)

    exchange_rate = 0.80  # Example exchange rate (1 USD = 0.80 GBP)

    if usd_search:
        usd_amount = usd_search.group()
        usd     = float(usd_amount.split()[1])

        hold = line.split(usd_amount)[0]
        print(f"{hold.strip()} {usd * exchange_rate:.2f}")
        return f"{hold.strip()} {usd * exchange_rate:.2f}"






def clean_up_line_func(lst):
    checked_lines = []
    print("\nStarting to clean up lines...")
    for line in lst:
        # print(line)
        bal_pattern = r"\d{1,3}(?:,\d{3})*\.\d{2}"  # Match '23.45 1,345.00' for delete of [1] for balance
        remove_bal = re.findall(bal_pattern, line)

        if len(remove_bal) > 1:  # checks for balance
            line = line.rsplit(remove_bal[-1], 1)[0]  # if balance 23.45 [1,234.00] = delete

            line = convert_usd_gbp(line)
            # print(f"Checked: {line}")


        checked_lines.append(line)

    return checked_lines
# check_lines = clean_up_line_func(bill_list)

# print("")
# for c_line in check_lines:
#     print(f"Checked: {c_line}")






# Hold lines -----
# usd_amount = usd_s.group()
#     usd_f = float(usd_amount.split()[1])
#     gbp = usd_f * exchange_rate
#     print(f"USD: {usd_amount} GBP: {gbp}")