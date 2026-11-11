"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user types one number N on the keyboard.
# 2. Process: The program goes through every number from 1 to N and says if each number is odd or even.
# 3. Out: One line per number from 1 to N, saying if it is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0 or negative number: the program displays a message and does not count, because there is no number between 1 and 0 or -4.
#    - A very large number: the program refuses and displays a message, because printing thousands of lines would flood the screen.


# Your code below
N = int(input("Enter number N: "))

# Checks for 0, negative or very large number :
if N < 1:
    print("N must be at least 1, nothing to display.")
elif N > 100:
    print("N is too large, nothing to display.")
else:
    # Goes through every number from 1 to N
    for i in range(1, N + 1):
        # If the remainder of the division by 2 is 0, the number is even
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

# Check it yourself : 
#  For N=6 I got : 1 is odd, 2 is even, 3 is odd, 4 is even, 5 is odd, 6 is even
#  For N=0 I got "N must be at least 1, nothing to display."
#  For N=-4 I got "N must be at least 1, nothing to display."
#  For N=300 I got "N is too large, nothing to display."