"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The input is a list of 8 first names like the example given in class.
# 2. Process: The program goes through the list one name at a time. For each name, it keeps its position, counts the letters, and compares the length to a limit that I chose (4 letters).
# 3. Out: Eight lines, one per name, each showing the position, the name, its number of letters and a verdict: "long" or "short".
# 4. What I compute for each item, and why it is worth showing: I compute the length of each name, because it is a simple number that can be checked by counting the letters. 
# The reader quickly sees which names are long(more than 4 letters) without counting them one by one.


# Your code below
names = ["Lucie", "Capucine", "Alice", "Eve", "Charlie", "David", "Lea", "Hugo"]

print("List of names and their lengths:", names)
print("First item of the list is: ", names[0])
print("Second item of the list is: ", names[1])
print("Third item of the list is: ", names[2])

for position, name in enumerate(names, 1):
    length = len(name)
    # Checks if the name is long (> 4 letters) or short
    if length > 4:
        verdict = "long"
    else:
        verdict = "short"
    print("Position", position, ":", name, length, "letters ->", verdict)

# Check it yourself : my program printed 8 lines 
# (+ 4 lines for the beginning of the code printing list of names, first, second and third items).
