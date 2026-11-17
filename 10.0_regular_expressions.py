"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user types three pieces of information: a postal code, a phone number and a product reference. 
# Everything arrives as text.
# 2. Process: Each value is compared with a pattern (a regular expression).
# If one value does not match, the program shows which field is invalid and stops. 
# The values are kept only if the three of them are valid.
# 3. Out: Either the three valid values, or a message saying which field was refused and "Nothing saved".
# 4. My three fields and rules:
#    - Postal code: exactly 5 digits. "7500" is refused (too short).
#    - Phone number: 10 digits, the first one is 0, no spaces. "06 12 34 56 78"
#      is refused, even if a human would understand it: a borderline case, I
#      decided that the form must be clean to make the file easy to use.
#    - Product reference: 3 capital letters, a dash, 3 digits, like BAG-001.
#
# My own explanation of the patterns:
# ^ and $ mean the whole text must match, from start to end.
# 0-9] is one digit, [A-Z] is one capital letter, {5} means "exactly 5 times". 
# So ^[0-9]{5}$ means "exactly five digits and nothing else".

# Your code below
import re

# One rule per field: the pattern the whole text must match
RULES = {
    "postal code": r"^[0-9]{5}$",
    "phone number": r"^0[0-9]{9}$",
    "product reference": r"^[A-Z]{3}-[0-9]{3}$",
}


# Returns True if the text matches the pattern entirely
def is_valid(pattern, text):
    return re.match(pattern, text) is not None


# Asks the three fields, and returns them only if all are valid
def ask_and_validate():
    values = {}
    for field, pattern in RULES.items():
        value = input("Enter the " + field + ": ").strip()
        if not is_valid(pattern, value):
            print("Invalid", field + ":", repr(value))
            return None
        values[field] = value
    return values


result = ask_and_validate()
if result is None:
    print("Nothing saved.")
else:
    print("All fields are valid. Saved:", result)

# Tests: one value that must pass and two that must fail, for each field
tests = [
    ("postal code", "75008", True), ("postal code", "7500", False), ("postal code", "750A8", False),
    ("phone number", "0612345678", True), ("phone number", "612345678", False), ("phone number", "06 12 34 56 78", False),
    ("product reference", "BAG-001", True), ("product reference", "bag-001", False), ("product reference", "BAG001", False),
]
for field, text, expected in tests:
    got = is_valid(RULES[field], text)
    print(field, repr(text), "->", got, "OK" if got == expected else "SURPRISE")

# Check it yourself : I ran 9 values, one valid and two invalid for each field.
# All of them gave the expected result, no surprise.