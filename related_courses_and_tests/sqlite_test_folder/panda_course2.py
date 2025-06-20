import pdfplumber
import pandas as pd
import re
import os

class DataPipeline:
    def __init__(self):
        self.file_loc = r"C:\Users\User\OneDrive\Desktop\DataFiles\bank_statement_01_25.pdf"
        self.pdf_scrape_text = []
        self.cleaned_text    = []
        self.processed_text  = []
        self.start_found   = False
        self.current_date  = None
        self.hold_line = ""
        #   --------------------------------   Patterns    --------------------------------
        self.start_pattern = r"balancebroughtforward"  # Match 'balancebroughtforward' followed by any number (with or without decimals)
        self.end_pattern   = r"balancecarriedforward"    # Match 'balancecarriedforward' as the end marker
        self.bal_pattern   = r"\d{1,3}(?:,\d{3})*\.\d{2}"    # Match '23.45 1,345.00' for delete of [1] for balance
        self.float_pattern = r"\d+\.\d{2}$"
        self.date_pattern  = r"^\d{2} [A-Za-z]{3} \d{2}"
        self.direct_debit_pattern = r"dd"
        self.credit_in_pattern = r"cr"
        self.chip_pattern = r")))"

    # -----------------------------------  Fix Lines for Dates and Debit amounts -----------------------------------

    def current_date_func(self, check_line):
        try:
            if re.search(self.date_pattern, check_line):
               match = re.match(self.date_pattern, check_line)
               self.current_date = match.group()
            else:
               return self.current_date
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: CDF: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")



    def display_lines(self):
        try:
            print(f"Length = {len(self.processed_text)}")
            for line in self.processed_text:
                print(line)
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: DL: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")



# ----------------------------------- Extract Raw Text and Clean into lines -----------------------------------
    def scrape_pdf(self):
        try:
            self.pdf_scrape_text = []
            with pdfplumber.open(self.file_loc) as pdf:     # opens the file
                for page in pdf.pages:                      # lope though the pages
                    text = page.extract_text()              # get text of each page
                    if not text:                            # if there's no text
                        continue                            # skips the page
                    for raw_line in text.split("\n"):       # get each raw line with split
                        l = raw_line.lower().strip()        # lower the text and stipe the text
                        if l:                               # if there's a line
                            self.pdf_scrape_text.append(l)  # append the line
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: S_PDF: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")

    def clean_text(self):
        try:
            self.start_found = False
            self.cleaned_text = []

            for line in self.pdf_scrape_text:
                if re.search(self.start_pattern, line):
                    self.start_found = True
                    continue
                if re.search(self.end_pattern, line):
                    self.start_found = False
                    continue
                if self.start_found:
                    self.cleaned_text.append(line)
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: CT: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")

# ************ continue to fix the lines for date start and amount end ************
    def clean_line_function(self):
        try:
            hold_line = []
            for line in self.cleaned_text:
                self.current_date_func(line)                                          # checks if line has current date
                date   = re.search(self.date_pattern, line)
                amount = re.search(self.float_pattern, line)
                remove_bal= re.findall(self.bal_pattern, line)

                if len(remove_bal) > 1:                                               # checks for balance
                    line = line.rsplit(remove_bal[-1], 1)[0]                          # if balance 23.45 [1,234.00] = delete
                if not hold_line:                                                     # checks if hold_line is empty
                    if date and amount:                                               # if had date and amount
                        self.processed_text.append(line)                              # return line
                    elif not date and amount:                                         # if it has no date but has float
                        self.processed_text.append(f"{self.current_date} {line} ")    # return date + line
                    elif date and not amount:                                         # if had date and not amount
                        hold_line.append(f"{line}")                                   # add data and send to hold_line
                    elif not date and not amount:                                      # # if had date and not amount
                        hold_line.append(f"{self.current_date} {line}")                # add data and send to hold_line
                else:
                    if amount:
                        hold_line.append(line)
                        self.processed_text.append(" ".join(hold_line))                 # return date + line
                        hold_line = []
                    elif not amount:
                        hold_line.append(f"{line} ")
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: CLF: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")


# ************ continue to fix the lines for date start and amount end ************


# --------------------------------------------------------------------------------------------------------------
# ---------------------------------------------  Run the Pipeline ----------------------------------------------

dpl = DataPipeline()

dpl.scrape_pdf()      # Scrape the data
#      |
#      |
#      v
dpl.clean_text()      # Clean the text
#      |
#      |
#      v
dpl.clean_line_function()
dpl.display_lines()





# for line in cleaned_text:
#     print(line)
# print(f"\nCurrent Date: {current_date}")

# -------------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame(processed_data, columns=["date", "name", "trans", "bal"])
# print(df)


# -----------------------------------------------------------------------------------------------------


