"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The function receives a list of numbers: the number of coffees I drink each day. The list from exercise 4.0 is one of the three lists I use.
# 2. Process: The function checks that the list is not empty, then it adds all the numbers, divides the total by the number of days, and rounds the result to two decimals.
# 3. Out: The function returns one number: the average number of coffees per day. 
# If the list is empty, it returns none.
# 4. My function name, and why return rather than print: My function is called average_coffees_per_day, because the name says what it computes and on
# what, without reading the code. 
# I use return instead of print because print only shows the value on the screen and then it is lost, while return gives the value back to the program, 
# so I can store it in a variable, compare it, or use it in another calculation. 
# For example, I subtract two results to compare the busy week and the calm week. 
# This would be impossible if the function only printed.


# Your code below
def average_coffees_per_day(daily_coffees):
    if len(daily_coffees) == 0:
        return None
    return round(sum(daily_coffees) / len(daily_coffees), 2)

# List from exercise 4.0, and two other weeks:
coffees = [2, 3, 1, 4, 2, 3, 5, 2]
calm_week = [1, 1, 2, 1, 0, 1, 2]
busy_week = [5, 6, 4, 7, 5, 6, 8]

result_1 = average_coffees_per_day(coffees)
result_2 = average_coffees_per_day(calm_week)
result_3 = average_coffees_per_day(busy_week)

print("Average of my 8 days:", result_1)
print("Average of the calm week:", result_2)
print("Average of the busy week:", result_3)

if result_3 > result_2:
    print("The busy week has", round(result_3 - result_2, 2), "more coffees per day.")

# Empty list
print("Average of an empty list:", average_coffees_per_day([]))

# Check it yourself: I tried with an empty list. Without my protection, the program crashed with a ZeroDivisionError, because it divided by zero days. 
# With the protection, it returns None and does not crash. 
# I think this is acceptable, because an empty list has no average, and None clearly says "no result". 
# But the program that uses the result must be careful, because None cannot be compared or used in a calculation.