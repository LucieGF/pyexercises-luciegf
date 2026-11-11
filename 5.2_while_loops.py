"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user types an answer on the keyboard, again and again.
# 2. Process: The program cleans each answer, keeps it in a list, and counts the attempts. 
#    It stops when the answer is "yes" or when the maximum number of attempts is reached.
# 3. Out: A message after each wrong answer, then a summary: the number of attempts, the list of answers, and the result (yes, or limit reached)
# 4. My stop condition, my attempt limit, my summary: The stop condition is the answer "yes".
#    The limit is 5 attempts, so the program can never run forever. 
#    "Yes", "yes" and " yes " count as the same answer, because a person can easily type a capital or an extra space by mistake. 
#    The summary contains the number of attempts, all the answers, and how the loop ended.


# Your code below
# Safety limit: 5 attempts
max_attempts = 5
attempts = 0
answers = []
success = False

# Keeps asking until the user says yes (or until the limit is reached)
while attempts < max_attempts:
    answer = input("Do you want to continue? (yes/no): ")
    attempts = attempts + 1

    # Removes extra spaces and capitals, so "Yes", "yes" and " yes " are the same
    cleaned = answer.strip().lower()
    answers.append(cleaned)

    if cleaned == "yes":
        success = True
        break
    else:
        print("Not accepted. Please type 'yes'.")

print("--- Summary ---")
print("Attempts used:", attempts, "out of", max_attempts)
print("Answers given:", answers)
if success:
    print("Result: the user said yes.")
else:
    print("Result: limit reached, the program stopped without a yes.")

# Check it yourself: when I never typed "yes", the program stopped after 5 attempts and showed "limit reached", so it does not run forever.
# When I typed "  YES  ", it was accepted as "yes" because of strip() and lower().
