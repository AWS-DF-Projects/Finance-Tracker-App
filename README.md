# Python Finance Tracker App

### ⚠️ Project Notice Work in Progress

---

**I’ve uploaded this code _as-is_ intentionally:**

1. So you can view the current structure and logic, even if incomplete or broken.  
2. To document and share my thought process, the fixes I apply, and how I approach debugging and refactoring in real time.

---

This project began as a way to showcase my Python skills with the longer-term goal of evolving it into a fully AWS-powered version to demonstrate cloud-native, secure, and automated infrastructure.

Originally, it started with a hard-coded frontend. Users could manually enter their bills, age, and monthly expenses to calculate their cash flow  a good starting point, but far from convenient. That’s when I had a realisation:

> Who's actually going to enter all that manually every month?

So I pivoted.

With my passion for automation, time-saving systems, and turning data into usable insight  I redesigned the backend. It now:

- Pulls PDF bank statements from my email inbox  
- Extracts the raw text  
- Detects and categorizes bills, wages, and expenditures  
- Cleans and structures this data using Python and pandas  
- Sends it to a database, ready for use in a frontend  

The end goal? A hands-free pipeline for financial analysis and insights paving the way for an AWS-hosted version that scales, secures, and automates all the heavy lifting.

---

### ⚠️ Disclaimer

The email-reading and PDF extraction functionality was developed with the help of AI. I wanted it included in the project as it's a realistic and valuable feature for automating workflows.

Everything else including the core logic, design decisions, data handling with pandas/SQLite, and the application's architecture was developed by me. I used a mix of online courses, docs, ChatGPT guidance, and good old-fashioned trial and error.

---
