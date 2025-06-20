import imaplib
import email
from email.header import decode_header
import os
password = "mzkp iaiz tran ihsh"
#  THIS IS NOW WORKING WELL 25/04/205
#    NEED TO FIGURE OUT THE CODE ON THIS
#    maybe adjust the folder to simpler path?
#    create folder "data_pipeline" in th 3_5_build



# login details
EMAIL       = "darrenfawcett1980@gmail.com"                 # get email
PASSWORD    = password                 # your 16-character app password
IMAP_SERVER = "imap.gmail.com"                        # IMAP this the gmail server?
SAVE_FOLDER = "bank_statements"                       # folder to save to

# connect to the server
mail = imaplib.IMAP4_SSL(IMAP_SERVER)                 # this connects to the server?
mail.login(EMAIL, PASSWORD)                           # login to email with password
mail.select("inbox")                                  # and check the inbox

# search for all emails
status, messages = mail.search(None, 'ALL') # unpack the response Get all emails
email_ids = messages[0].split()                             # get the first list of the messages and split them
last_10_email_ids = email_ids[-20:]                         # get the last 10 emails

print("Checking emails...\n")

# loop through the last 10 emails
for index, email_id in enumerate(last_10_email_ids):                                # loop through the emails
    print(f"Index: {index} - Checking email ID: {email_id}")                       # working
    _, msg_data = mail.fetch(email_id, "(RFC822)")   # NO IDEA = gets a certain part of the email?
    for response_part in msg_data:                                 #  loop through msg_data
        if isinstance(response_part, tuple):                       # if the response part is tuple
            msg = email.message_from_bytes(response_part[1])       # return the [1]
            print(f"Raw subject: {msg['Subject']}")

            # decode the subject of the email
            subject, encoding = decode_header(msg["Subject"])[0]   # does this unpack the message further
            print(f"Subject coded: {subject}")
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")
                print(f"Decoded subject: {subject}")
            print("")

            # check if the subject contains "Bank statement"
            if "bank statement" in subject.lower():
                print("******* TEST *******")
                print(f"Found 'Bank statement' in subject: {subject.lower()}")  # Print found message

                # loop through parts to find attachments
                for part in msg.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue

                    # Check if the email part is a PDF attachment
                    filename = part.get_filename()
                    if filename:
                        print(f"Found attachment: {filename}")  # Debug attachment found
                        # Ensure the file is a PDF
                        if filename.lower().endswith(".pdf"):
                            if not os.path.exists(SAVE_FOLDER):
                                os.makedirs(SAVE_FOLDER)  # Create folder if it doesn't exist
                            filepath = os.path.join(SAVE_FOLDER, filename)
                            with open(filepath, "wb") as f:
                                f.write(part.get_payload(decode=True))
                            print(f"Saved: {filepath}")  # Only print saved files
                        else:
                            print(f"Skipped non-PDF file: {filename}")  # Debug non-PDF files
                    else:
                        print("No filename found in attachment part")  # Debug missing filename

print("\nCompleted emails processing.")
