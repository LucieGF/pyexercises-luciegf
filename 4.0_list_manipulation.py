"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The input is a list of 8 numbers that I wrote myself in the code: the number of coffees I drink each day.
# 2. Process: The program keeps the numbers in a list, picks one item, sorts the list, then computes the total and the average per day.
# 3. Out: The whole list, the first item, the sorted list, the total of coffees and the average per day.
# 4. What my list is about, and what I computed from it: My list is about the number of coffees I drink each day over 8 days.
# I computed the total and the average so I can see my usual habit.


# Your code below
number_1 = 2
number_2 = 4
number_3 = 6
number_4 = 8
number_5 = 10

print("The first number is : ", number_1)
print("The second number is : ", number_2)
print("The third number is : ", number_3)
print("The fourth number is : ", number_4)
print("The fifth number is : ", number_5)

# Number of coffees I drink each day (over 8 days):
numbers = [2,3,1,4,2,3,5,2]
print("The whole list is : ", numbers)

print("The second item of the list is : ", numbers[1])
print("The first item of the list is : ", numbers[0])

sorted_list = sorted(numbers)
print("The sorted list is : ",  sorted_list)

total = sum(numbers)
average = total / len(numbers)

print("Total coffees:", total)
print("Average per day:", average)

removed_number = numbers.pop()
print("The removed item is : ", removed_number)
print("The list after removing the last item is : ", numbers)
print("The sorted list after removing the last item is : ", sorted_list)
removed_number_last = sorted_list.pop()
print("The removed item from the sorted list is : ", removed_number_last)
print("The sorted list after removing the last item is : ", sorted_list)

# Check it yourself:
# I added the first three days by hand (2 + 3 + 1 = 6) and the program gave the same result. 
# The total is 22 and the average is 2.75, which matches what I calculated by hand.