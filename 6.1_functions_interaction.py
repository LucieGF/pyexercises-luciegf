"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The input is the list of 8 numbers from exercise 4.0 (coffees per day) and a limit that I chose: 3 coffees.
# 2. Process, function by function:
#.   - count_days: counts how many days are in the list.
#    - count_heavy_days: counts the days with more coffees than the limit.
#    - to_percentage: turns a part and a total into a percentage.
#    - heavy_days_summary: calls the three functions above, in this order, and
#      returns the two results.
# 3. Out: heavy_days_summary returns two values: the number of heavy days and their percentage. The program prints them in one sentence.
# 4. The question my fourth function answers: "How many days did I drink more than 3 coffees, and what share of the days is that?" 
# Splitting it into three makes it easier to check, because I can test each small function on its own with a result I know by hand. 
# If the final answer is wrong, I know which function to look at.


# Your code below
def count_days(daily_coffees):
    return len(daily_coffees)

def count_heavy_days(daily_coffees, limit):
    heavy = 0
    for coffees in daily_coffees:
        if coffees > limit:
            heavy = heavy + 1
    return heavy

def to_percentage(part, total):
    if total == 0:
        return 0
    return round(part / total * 100, 1)


# Uses the three functions above to answer the question
def heavy_days_summary(daily_coffees, limit):
    total_days = count_days(daily_coffees)
    heavy_days = count_heavy_days(daily_coffees, limit)
    percentage = to_percentage(heavy_days, total_days)
    return heavy_days, percentage


# List from exercise 4.0
coffees = [2, 3, 1, 4, 2, 3, 5, 2]

print(count_days(coffees))               # expected: 8
print(count_heavy_days(coffees, 3))      # expected: 2 (the days with 4 and 5)
print(to_percentage(2, 8))               # expected: 25.0

days, share = heavy_days_summary(coffees, 3)
print("Days with more than 3 coffees:", days, "(" + str(share) + "% of the days)")

# Check it yourself : 
# - count_days([2, 3, 1, 4, 2, 3, 5, 2]) -> expected 8, got 8.
# - count_heavy_days([2, 3, 1, 4, 2, 3, 5, 2], 3) -> expected 2 (the days with
#   4 and 5 coffees), got 2.
# - to_percentage(2, 8) -> expected 25.0, got 25.0.
# - Combined: 2 heavy days out of 8 = 25.0%, as expected.