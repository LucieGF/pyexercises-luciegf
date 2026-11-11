"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user types one sentence on the keyboard. It is received as text.
# 2. Process: The program applies four different string methods to the sentence.
# 3. Out: Four lines on the screen, one for each transformation.
# 4. My four transformations, and when each is useful:
#    - strip(): removes the spaces at both ends
#    - upper(): puts everything in capital letters
#    - title(): puts a capital letter on each word
#    - replace(" ", "_"): replaces spaces by underscores


# Your code below
sentence = input("Enter a sentence: ")

print("strip:", repr(sentence.strip()))
print("upper:", repr(sentence.upper()))
print("title:", repr(sentence.title()))
print("replace:", repr(sentence.replace(" ", "_")))

# Check it yourself: I tested with "  Good morning everyone  ".
# - strip(): the spaces at both ends disappeared, as expected.
# - upper(): everything is in capitals but the spaces are still there, as expected.
# - title(): each word starts with a capital, as expected.
# - replace(): each space became "_", even the ones at the ends.