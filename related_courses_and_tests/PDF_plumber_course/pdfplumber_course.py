import pdfplumber
import os

folder_loc = r"C:\Users\User\OneDrive\Desktop\DataFiles"

pdf_scrape_text = []
print("\nStarting PDF crape...")
for filename in os.listdir(folder_loc):                      # loop through the files in the folder
    file_path = os.path.join(folder_loc, filename)           # create the file path by folder path + file
    if filename.lower().endswith(".pdf"):                    # check if the filename endswith ".pdf"
        with pdfplumber.open(file_path) as pdf:              # opens the file
            for page in pdf.pages:                           # lope though the pages
                text = page.extract_text()                   # get text of each page
                if not text:                                 # if there's no text
                    continue                                 # skips the page
                for raw_line in text.split("\n"):            # get each raw line with split
                    l = raw_line.lower().strip()             # lower the text and stipe the text
                    if l:                                    # if there's a line
                        pdf_scrape_text.append(l)            # append the line
print("Completed PDF scrape.")

for line in pdf_scrape_text:
    print(line)

