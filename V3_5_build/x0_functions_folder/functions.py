import sys
import datetime

class HelperTools:

    @staticmethod
    def check_list(inp_text, valid_list, typ):
        tries = 3                                                                  # Tries remaining
        while tries > 0:                                                           # Loop while tries greater than 0
            try:
                raw = input(f"{inp_text}{tuple(valid_list)}: ").strip().lower()   # get input answer in raw
                inp = typ(raw)                                                     # inp into required value str/int
                if inp in valid_list:                                              # Check if inp is in the list
                    return inp                                                     # if so then return that inp in desired format
                else:
                    raise ValueError(f"❌ {inp} not in valid list {valid_list}")   # manual error message = e
            except ValueError as e:
                print(f"😵 OOPS {e}")                                              # display if error with  e
            except Exception as e:
                print(f"⚠️ Unexpected error: {e}")                                 # catches another un expected errors
            finally:
                tries  -= 1                                                        # remove 1 try
        print("Sorry there seems to be an issue.")                                 # if tries at 0 then print this message
        return                                                                     # If tries 0 return None (back to menu to be added)
    # te.check_input(input_text_1, len_of_db, int)
    # te.check_input(input_text_2, ["a", "b", "c"], str)

    @staticmethod
    def check_number(input_text, num_type):
        tries = 3  # Tries remaining
        while tries > 0:  # Loop while tries greater than 0
            try:
                raw = input(f"{input_text}: ").strip()                             # get input answer in raw
                inp = num_type(raw)                                                # inp into required value int/float
                return inp                                                         # if so then return that inp in desired format
            except ValueError:
                print(f"⚠️ Unexpected error: is not a valid number!")              # Display Manual error message
            finally:
                tries -= 1                                                          # remove 1 try
        print("Sorry there seems to be an issue.")                                  # if tries at 0 then print this message
        return                                                                      # If tries 0 return None (back to menu to be added)

    # print(f"Int   = {te.check_number(num_1, int)}")
    # print(f"Float = {te.check_number(num_2, float)}")

    @staticmethod
    def check_blank_input(text_input):
        error_count = 3
        while error_count > 0:
            try:
                inpt = input(f"{text_input}: ")
                if inpt  != "":
                    return inpt
                else:
                    error_count -= 1
                    raise ValueError("Please enter a value.")
            except ValueError as e:
                print(f"⚠️  {e}")
            except Exception as e:
                print(f"😵 OOPS, sorry something has gone wrong: {e}")
                return None

    @staticmethod
    def check_input_len(input_text, len_min, len_max):
        tries = 3                                                                    # Tries remaining
        while tries > 0:                                                             # Loop while tries greater than 0
            try:
                inpt = input(f"{input_text}: ").strip()                              # Asks for input
                if len_min  <= len(inpt) <= len_max :                           # Checks if text over length min-max
                    return inpt                                                      # if so then returns input
                else:
                    raise ValueError(f"Please make at min {len_min}-{len_max} characters long.")  # Manual error message
            except ValueError as e:
                print(f"⚠️  {e}")                                                    # prints manual e message if value incorrect
            except Exception as e:
                print(f"😵 OOPS, sorry something has gone wrong: {e}")               # Catches all other errors
            finally:
                tries -= 1                                                           # Removes one try after ValueError
        print("Sorry there seems to be an issue!")                                   # If try's run out prints this
        return None                                                                  # and returns None

    # text_1 = "please add tag (3 min)"
    # print(te.check_input_len(text_1, 3))

    @staticmethod
    def field_func(acc):
        field = {}
        for index, value in enumerate(acc, start=1):
            field[str(index)] = value
        return field


    @staticmethod
    def text_edit(text, effect, underline):
        start = ""
        if effect == "bold":
            start += "\033[1m"
        else:
            start += ""
        if underline == "ul":
            start += "\033[4m"
        end = "\033[0m"
        return f"{start}{text}{end}"

    @staticmethod
    def calender():
        today = datetime.date.today()
        # cur_day = today.day
        cur_month = today.month
        cur_year = today.year
        return f"{cur_month}_{cur_year}"
