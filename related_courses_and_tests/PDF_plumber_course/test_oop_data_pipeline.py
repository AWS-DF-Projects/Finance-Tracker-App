from email.header import decode_header
import imaplib
import email
import pdfplumber
import re
import os
import pandas as pd

class DataPipeline:
    def __init__(self):
        self.pdf_folder_path = r"C:\Users\User\OneDrive\Desktop\pdf_bank_statements"
        self.pdf_scrape_text = []
        self.cleaned_text    = []
        self.processed_text  = []
        self.email_app_password = "mzkp iaiz tran ihsh"
        self.start_found   = False
        self.current_date  = None
        self.hold_line = ""
        #   --------------------------------   Patterns    --------------------------------
        self.start_pattern = r"balancebroughtforward"      # Match 'balancebroughtforward' followed by any number (with or without decimals)
        self.end_pattern   = r"balancecarriedforward"      # Match 'balancecarriedforward' as the end marker
        self.bal_pattern   = r"\d{1,3}(?:,\d{3})*\.\d{2}"  # Match '23.45 1,345.00' for delete of [1] for balance
        self.rate_pattern  = r'visa\s*rate\s*\d+\.\d{2}'   # Match '@   visa rate 19.46' for delete of [1] for balance
        self.usd_pattern   = r"usd\s+\d+\.\d{2}"
        self.float_pattern = r"\d+\.\d{2}$"
        self.time_pattern = r"@\d{2}\:\d{2}"
        self.date_pattern  = r"^\d{2} [A-Za-z]{3} \d{2}"
        self.direct_debit_pattern = r"dd"
        self.credit_in_pattern = r"cr"
        self.chip_pattern = r")))"

# -----------------------------------  Fix Lines for Dates and Debit amounts -----------------------------------

    def make_file_folder(self):
        folder_path = self.pdf_folder_path
        try:
            if not os.path.exists(folder_path):
                print(f"...Folder: {folder_path} is missing. Creating folder now...\n")
                os.makedirs(folder_path)  # Only create folder if not exists
            else:
                print(f"...Folder: {folder_path} already exists\n")
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: CDF: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")

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


    @staticmethod
    def display_lines(selected_list):
        try:
            for line in selected_list:
                print(line)
            print("-"*75)
            print(f"Length = {len(selected_list)}")
            print("-"*75)
            print("-"*30 + " NEXT PROCESS " + "-"*30)
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: DL: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")

# --------------------------------  Convert USD to GBP  --------------------------------

    def convert_usd_gbp(self, line):
        # print(f"In:  {line}")
        usd_search = re.search(self.usd_pattern, line)
        exchange_rate = 0.80  # Example exchange rate (1 USD = 0.80 GBP)
        if usd_search:
            usd_amount = usd_search.group()
            usd = float(usd_amount.split()[1])
            hold = line.split(usd_amount)[0]
            # print(f"Out: {hold.strip()} {usd * exchange_rate:.2f}")
            return f"{hold.strip()} {usd * exchange_rate:.2f}"


#---------------------------------------------------------------------------------------------------------------
# ----------------------------------- Extract Raw Text and Clean into lines -----------------------------------
#---------------------------------------------------------------------------------------------------------------

    def email_extraction_func(self):
        # login details
        EMAIL = "darrenfawcett1980@gmail.com"           # get email
        PASSWORD = self.email_app_password              # your 16-character app password
        IMAP_SERVER = "imap.gmail.com"                  # IMAP this the gmail server?
        SAVE_FOLDER = self.pdf_folder_path              # folder to save to

        # connect to the server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)           # this connects to the server?
        mail.login(EMAIL, PASSWORD)                     # login to email with password
        mail.select("inbox")                            # and check the inbox

        # search for all emails
        status, messages = mail.search(None, 'SUBJECT "Bank statement"')  # unpack the response Get all emails
        email_ids = messages[0].split()               # get the first list of the messages and split them
        last_20_email_ids = email_ids[-20:]           # get the last 10 emails

        print("\nChecking emails...\n")

        # loop through the last 10 emails`
        for email_id in last_20_email_ids:                                # loop through the emails
            _, msg_data = mail.fetch(email_id, "(RFC822)")  # NO IDEA = gets a certain part of the email?
            for response_part in msg_data:                                # loop through msg_data
                if isinstance(response_part, tuple):                      # if the response part is tuple
                    msg = email.message_from_bytes(response_part[1])      # return the [1]

                    # decode the subject of the email
                    subject, encoding = decode_header(msg["Subject"])[0]  # does this unpack the message further
                    if isinstance(subject, bytes):                        # checks if its in bytes
                        subject = subject.decode(encoding or "utf-8")     # if so converts to comp to human

                    # check if the subject contains "Bank statement"
                    if "bank statement" in subject.lower():
                        print(f"Found 'Bank statement' in subject: {subject}")  # Print found message

                        # loop through parts to find attachments
                        for part in msg.walk():
                            if part.get_content_maintype() == 'multipart':
                                continue
                            if part.get('Content-Disposition') is None:
                                continue

                            # Check if the email part is a PDF attachment
                            filename = part.get_filename()
                            if filename:
                                print(f"Found attachment: {filename}")          # Debug attachment found
                                # Ensure the file is a PDF
                                if filename.lower().endswith(".pdf"):
                                    filepath = os.path.join(SAVE_FOLDER, filename)
                                    with open(filepath, "wb") as f:
                                        f.write(part.get_payload(decode=True))
                                    print(f"Saved: {filepath}")                 # Only print saved files
                                else:
                                    print(f"Skipped non-PDF file: {filename}")  # Debug non-PDF files
                            else:
                                print("No filename found in attachment part")   # Debug missing filename

        print("\n...Completed emails processing\n")

# -----------------------------------  Extract Raw Text  ----------------------------------

    def scrape_pdf_func(self):
        try:
            print("\nStarting PDF crape...")
            for filename in os.listdir(self.pdf_folder_path):  # loop through the files in the folder
                file_path = os.path.join(self.pdf_folder_path, filename)  # create the file path by folder path + file
                if filename.lower().endswith(".pdf"):  # check if the filename endswith ".pdf"
                    with pdfplumber.open(file_path) as pdf:  # opens the file
                        for page in pdf.pages:  # lope though the pages
                            text = page.extract_text()  # get text of each page
                            if not text:  # if there's no text
                                continue  # skips the page
                            for raw_line in text.split("\n"):  # get each raw line with split
                                l = raw_line.lower().strip()  # lower the text and stipe the text
                                if l:  # if there's a line
                                    self.pdf_scrape_text.append(l)  # append the line
            print("Completed PDF scrape.\n")
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: S_PDF: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")

# -----------------------------------   Clean Text  ----------------------------------

    def clean_text_func(self):
        try:
            self.start_found = False
            self.cleaned_text = []

            print("\nStarting to clean text...")
            for line in self.pdf_scrape_text:
                if re.search(self.start_pattern, line):
                    self.start_found = True
                    continue
                if re.search(self.end_pattern, line):
                    self.start_found = False
                    continue
                if self.start_found:
                    self.cleaned_text.append(line)
            print("...Clean text completed\n")
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: CT: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")

# ---------------------------------------   Clean Text  --------------------------------------

# ************ continue to fix the lines for date start and amount end ************
    def clean_up_line_func(self):
        try:
            hold_line = []
            print("\nStarting to clean up lines...")
            for line in self.cleaned_text:
                self.current_date_func(line)                                          # checks if line has current date
                date   = re.search(self.date_pattern, line)
                amount = re.search(self.float_pattern, line)
                remove_bal  = re.findall(self.bal_pattern, line)
                usd_search = re.search(self.usd_pattern, line)
                rate_findall = re.findall(self.rate_pattern, line)
                time_search = re.search(self.time_pattern, line)

                if rate_findall:
                    line = re.sub(self.rate_pattern, "", line).strip()           # swap out rates text for ""
                if len(remove_bal) > 1:
                    line = line.rsplit(remove_bal[-1])[0]                             # if balance 23.45 [1,234.00] = delete
                if  usd_search:
                    line = self.convert_usd_gbp(line)                                 # convert usd to gbp and clear "usd"
                if time_search:
                    line = re.sub(self.time_pattern, "", line).strip()           # swap time (@23.45) for ""

                if not hold_line:                                                     # checks if hold_line is empty
                    if date and amount:                                               # if had date and amount
                        self.processed_text.append(line)                              # return line
                    elif not date and amount:                                         # if it has no date but has float
                        self.processed_text.append(f"{self.current_date} {line} ")    # return date + line
                    elif date and not amount:                                         # if had date and not amount
                        hold_line.append(f"{line}")                                   # add data and send to hold_line
                    elif not date and not amount:                                     # # if had date and not amount
                        hold_line.append(f"{self.current_date} {line}")               # add data and send to hold_line
                else:
                    if amount:
                        hold_line.append(line)
                        self.processed_text.append(" ".join(hold_line))                # return date + line
                        hold_line = []
                    elif not amount:
                        hold_line.append(f"{line} ")
            print("...Clean up lines completed\n")
        except ValueError as e:
            print(f"ValueError encountered while processing line: {line}")
            print(f"Error: {e}")
        except Exception as e:
             print(f"🛑 Oops! Something went wrong: CLF: {e}")
             print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")


# ************ continue to fix the lines for date start and amount end ************


# --------------------------------------------------------------------------------------------------------------
# ---------------------------------------------  Run the Pipeline ----------------------------------------------

dpl = DataPipeline()

def run_data_pipeline():
    dpl.make_file_folder()#                  check for folder if not there make one
#            |                                                 |
#            |                                                 |
#            v                                                 v
    dpl.email_extraction_func()#                       Scrape the data
    dpl.display_lines(dpl.cleaned_text)#                     Print
#            |                                                 |
#            |                                                 |
#            v                                                 v
    dpl.scrape_pdf_func()#                               Scrape the data
    dpl.display_lines(dpl.pdf_scrape_text)#                  Print
#            |                                                 |
#            |                                                 |
#            v                                                 v
    dpl.clean_text_func()#                              Clean the text
    dpl.display_lines(dpl.cleaned_text)#                     Print
#            |                                                 |
#            |                                                 |
#            v                                                 v
    dpl.clean_up_line_func()#                         Clean lines in text
#            |                                                 |
#            |                                                 |
#            v                                                 v
    print("\nHere's the lines extracted...\n")#              Print
    dpl.display_lines(dpl.processed_text)#                  Results
    print("\nProcessing complete.\n")#                     Print End

run_data_pipeline()







# --------------------------------------------------------------------------------------------
#  ---------------------------------------- TESTING  ----------------------------------------
# --------------------------------------------------------------------------------------------
# list_to_check = [
#     "27 jan 25 vis int'l 0051896991 tbl* learn.cantril  amsterdam  usd 24.00 @   visa rate 19.46",
#     "27 jan 25 vis int'l 0051896992 tbl* learn.cantril  amsterdam  usd 24.00 @   visa rate 19.46",
# ]
# def testing_usd_rates(lst):
#     for l in lst:
#         x = dpl.convert_usd_gbp(l)
#         print(x)
# testing_usd_rates(list_to_check)



# for line in cleaned_text:
#     print(line)
# print(f"\nCurrent Date: {current_date}")

# -------------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame(processed_data, columns=["date", "name", "trans", "bal"])
# print(df)


# -----------------------------------------------------------------------------------------------------


