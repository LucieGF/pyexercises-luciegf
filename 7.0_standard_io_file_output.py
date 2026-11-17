"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: The user types three pieces of information on the keyboard: the name of a client, the product bought and the amount in euros. 
# The date is added automatically by the program. Everything typed arrives as text.
# 2. Process: The program asks each question until the answer is acceptable (a text that is not empty, and an amount that is a number greater than 0).
# Then it checks if the file already exists. If not, it writes the header line first. 
# Then it adds one line at the end of the file, without erasing the previous ones.
# 3. Out, file name and columns: The file is sales.csv, with a semicolon as separator. 
# The columns are: date, client_name, product, amount. Each run adds exactly one line.
# 4. Why these columns, and what this file is for: This is a simple sales log of a boutique. 
# With two hundred rows, I could calculate the total revenue, see which products sell the most, and find which clients buy often to offer them a personal service. 
# The date lets me see sales by month.

# Decisions: the first time, the file does not exist, so the program creates it
# with the header line. If a value is not acceptable (empty text, or an amount
# that is not a positive number), the program asks again.

# Your code below
import csv
import os
from datetime import date

FILENAME = "sales.csv"
COLUMNS = ["date", "client_name", "product", "amount"]


def ask_text(question):
    answer = input(question).strip()
    while answer == "":
        answer = input("This cannot be empty. " + question).strip()
    return answer


def ask_amount(question):
    while True:
        answer = input(question).strip().replace(",", ".")
        try:
            amount = float(answer)
            if amount > 0:
                return amount
            print("The amount must be greater than 0.")
        except ValueError:
            print("Please type a number, for example 450.")


def save_entry(entry):
    is_new_file = not os.path.exists(FILENAME)
    with open(FILENAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        if is_new_file:
            writer.writerow(COLUMNS)
        writer.writerow(entry)


# Collects the information of one entry and saves it
client_name = ask_text("Client name: ")
product = ask_text("Product bought: ")
amount = ask_amount("Amount in EUR: ")

save_entry([date.today(), client_name, product, amount])
print("Entry saved in", FILENAME)


# Check it yourself : I ran the program three times. The file sales.csv has 4 lines: one header line and three entries. 
# I also typed "abc" as an amount and an empty name, and the program asked again without crashing.