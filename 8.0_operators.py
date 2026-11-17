"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: Nothing is typed by the user. The input is two values that I wrote in the code: the number 5 and the text "5".
# 2. Process: The program compares the two values with the comparison operators, then combines these results with and, or, not.
# 3. Out: A table of lines on the screen, each showing a comparison and its result, True or False.
# 4. My two values, and what surprised me: I picked 5 and "5". What surprised me is that 5 == "5" is False, because one is a number and the other is text. 
# Python only says they are equal after converting the number with str().

# Your code below
# Part 1: a number and the same number written as text
a = 5
b = "5"

equal = a == b
different = a != b
same_after_conversion = str(a) == b

both = equal and same_after_conversion
either = equal or same_after_conversion
not_equal = not equal

print("Value a:", repr(a), "| Value b:", repr(b))
print("-" * 40)
print("a == b                  :", equal)
print("a != b                  :", different)
print("str(a) == b             :", same_after_conversion)
print("-" * 40)
print("equal and same_converted:", both)
print("equal or same_converted :", either)
print("not equal               :", not_equal)

# Part 2: two texts with different capitals, to use < and >
c = "apple"
d = "Apple"
print("-" * 40)
print("c == d :", c == d)
print("c < d  :", c < d)
print("c > d  :", c > d)
print("c.lower() == d.lower() :", c.lower() == d.lower())

# Check it yourself : I predicted 2 results out of 10 correctly. I got wrong
# a == b, because 5 (a number) and "5" (text) are not equal in Python. I also
# got wrong c == d and c < d, because capital letters count: "apple" is not
# equal to "Apple", and capital letters come before lowercase letters. I
# assumed Python would ignore the type and the capitals. It does not, and I
# needed str() and lower() to compare them as equal.