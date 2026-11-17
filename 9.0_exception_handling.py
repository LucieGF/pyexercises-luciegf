"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user types a number of conversions on the keyboard. It arrives as text. 
# The budget (1000 EUR) is fixed in the code.
# 2. Process: The program converts the text into a number, then divides the budget by it to get the cost per conversion. 
# If something goes wrong, it shows a message and asks again, up to 3 attempts.
# 3. Out: The cost per conversion in euros, or a message explaining the problem.
# The program always ends normally, it never crashes.
# 4. The two failures, and whether they deserve the same message:
# - ValueError: the user types something that is not a number ("abc", empty).
# The message asks for digits.
# - ZeroDivisionError: the user types 0. The message explains that a cost per conversion cannot be computed with zero conversions.
# They deserve different messages, because the cause and the fix are not the same. 
# I catch them separately because a single catch-all except would hide which problem happened, give the user a useless message, and could also hide real bugs in my own code.
# Limit: 3 attempts, then the program stops with a message.


# Your code below
BUDGET = 1000
MAX_ATTEMPTS = 3

# Asks for a number of conversions and returns the cost per conversion,
# or None if the user failed all the attempts
def ask_cost_per_conversion():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        answer = input("Number of conversions: ")
        try:
            conversions = float(answer)
            return BUDGET / conversions
        except ValueError:
            print("That is not a number. Please type digits, for example 25.")
        except ZeroDivisionError:
            print("Zero conversions: the cost per conversion cannot be computed.")
        print("Attempt", attempt, "of", MAX_ATTEMPTS)
    return None


result = ask_cost_per_conversion()
if result is None:
    print("Too many invalid answers. The program stops here.")
else:
    print("Cost per conversion:", round(result, 2), "EUR")

# Check it yourself :
# - With 25: it printed "Cost per conversion: 40.0 EUR".
# - With 0: it showed the zero conversions message and asked again.
# - With "abc": it showed the "not a number" message and asked again.
# - With an empty line: same as "abc", because float("") is a ValueError.
# None of the four runs crashed the program.