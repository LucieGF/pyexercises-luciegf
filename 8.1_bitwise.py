"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: Nothing is typed by the user. The input is three permissions that I defined in the code, each one stored as one bit: VIEW, EDIT and PUBLISH.
# 2. Process: The program combines VIEW and EDIT with |, tests if PUBLISH is present with &, adds PUBLISH with |, then removes EDIT with & and ~.
# 3. Out: The value in binary after each step, and True or False for each test.
# 4. What my permissions are about: They describe what a team member may do on a marketing campaign. 
# VIEW lets them read it, EDIT lets them change it,and PUBLISH lets them put it online. 
# An intern could have VIEW and EDIT, a manager all three.

# Your code below
# Permissions on a marketing campaign, one bit each
VIEW = 0b001
EDIT = 0b010
PUBLISH = 0b100

# Shows a number in binary with 3 digits
def show(label, value):
    print(label.ljust(28), format(value, "03b"))

# Combines two permissions with OR
intern = VIEW | EDIT
show("intern = VIEW | EDIT", intern)

# Tests if a third permission is present with AND
can_publish = (intern & PUBLISH) != 0
print("Intern can publish?".ljust(28), can_publish)

# Adds the permission PUBLISH with OR
manager = intern | PUBLISH
show("manager = intern | PUBLISH", manager)

# Removes the permission EDIT with AND and NOT
manager = manager & ~EDIT
show("manager without EDIT", manager)

# Checks the final result
print("Manager can edit?".ljust(28), (manager & EDIT) != 0)
print("Manager can publish?".ljust(28), (manager & PUBLISH) != 0)

# Check it yourself : I read the binary value at each step. 011 means VIEW and
# EDIT, 111 means all three permissions, and 101 means VIEW and PUBLISH after
# EDIT was removed. The results matched what I expected.