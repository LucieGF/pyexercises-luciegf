"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The input is the list of 8 numbers from exercise 4.0 (number of coffees I drink each day).
# 2. Process: The program reorders the list in four different ways, using methods that create a new list, or a copy, so that the original is never changed.
# 3. Out: The list in four different orders, then the original list at the end to prove that it has not moved.
# 4. My four orders, and which ones modify the original: 
#    - sorted(coffees): smallest to biggest, creates a new list, the original is safe.
#    - sorted(coffees, reverse=True): biggest to smallest, creates a new list, safe.
#    - coffees[::-1]: reverse of the original order, creates a new list, safe.
#    - copy + sort(): sort() modifies the list in place, so I used it on a copy and the original is safe.
# None of my four orders modifies the original. 
# If I had used coffees.sort() or coffees.reverse() directly, the original list would have been changed.


# Your code below
coffees = [2, 3, 1, 4, 2, 3, 5, 2]

print("Smallest to biggest:", sorted(coffees))
print("Biggest to smallest:", sorted(coffees, reverse=True))
print("Reverse of the original:", coffees[::-1])

copy_of_coffees = coffees.copy()
copy_of_coffees.sort()
print("Sorted copy:", copy_of_coffees)

print("The original list is still:", coffees)

# Check it yourself: the last line shows [2, 3, 1, 4, 2, 3, 5, 2], which is exactly the list from exercise 4.0.