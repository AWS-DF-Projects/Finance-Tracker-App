import pdfplumber
import re

file_loc = r"C:\Users\User\OneDrive\Desktop\DataFiles\bank_statement_01_25.pdf"

def scrape_pdf(file):
    try:
        store = []
        with pdfplumber.open(file_loc) as pdf: # opens the file
            for page in pdf.pages: # lope though the pages
                text = page.extract_text() # get text of each page
                if not text: # if there's no text
                    continue   # what does this do?
                for raw_line in text.split("\n"): # get each raw line with split
                    l = raw_line.lower().strip() # lower the text and stipe the text
                    if l: # if there's a line
                        store.append(l) # append the line
        return store #return store
    except Exception as e:
        print(f"🛑 Oops! Something went wrong: S_PDF: {e}")
        print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")

plumber_data_store = scrape_pdf(file_loc)
print(len(plumber_data_store))

for line in plumber_data_store:
    print(line)

# -------------------------------------------  UNUSED DEF -------------------------------------------

def check_for_bill(self, check_line):
    try:
        if re.search(self.float_pattern, check_line):    # check the line has  123.00 or 1,234.00 ending
            if self.hold_line == "":                     # if the hold line is empty
                return check_line                        # if hold line is "" and has the 123.00 or 1,234.00 ending return line
            else:                                        # else if the hold line is not empty
                return f"{self.hold_line}+{check_line}"  # else if hold line not "" and the line has 123.00 or 1,234.00 ending return hold+check line
        else:                                            # else if id don't hav the 123.00 or 1,234.00 ending
            if self.hold_line == "":                     # and the check line is ""
                pass                                     # the check line == hold line eg. "so katie finch...."
    except Exception as e:
         print(f"🛑 Oops! Something went wrong: CFB: {e}")
         print("If this keeps happening, double-check the input or let the dev (aka you 😎) know.")

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

         def convert_usd_gbp(self, line):
             exchange_rate = 0.80  # Example exchange rate (1 USD = 0.80 GBP)
             usd_search = re.search(self.usd_pattern, line)
             remove_rate = re.search(self.rate_pattern, line)

             # if remove_rate:
             #     line = line.split(self.rate_pattern[0].strip())[0]
             #     print(f"RR: {line}")

             if usd_search:
                 extract = usd_search.group()
                 hold = line.split(self.usd_pattern[:3].strip())[0]
                 print(hold)
                 usd = float(extract.split()[1])
                 # print(f"USD: {usd} - GBP: {usd * exchange_rate:.2f}")
                 return f"{hold} {usd * exchange_rate:.2f}"
             return line