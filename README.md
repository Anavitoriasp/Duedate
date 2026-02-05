# Duedate
A small Python program that reads a list of clients and their payment due days from a text file and identifies payments that are overdue (up to 7 days) or due today.


Requirements:
- Python 3
- Linux or Windows

Files:
- duedate.py : main program
- clients.txt : input data (day of month, client name)

How to run:
1. Place all files in the same directory
2. Open a terminal in that directory
3. Run: python3 duedate.py

Notes:
- The program uses the current month and year to calculate due dates.
- It lists clients whose payments are overdue by up to 7 days or due today.
