"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user types two numbers on the keyboard. They are received as text, so the program must convert them into numbers.
# 2. Process: The program converts the two texts into integers, then computes the sum, the difference, the product and the division.
# 3. Out: Four lines on the screen, one for each operation and the result.
# 4. What happens when the second number is zero, and why: The program displays a message instead of a result for the division because dividing by zero is impossible.


# Your code below
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

print("The first number is : ",number_1)
print("The second number is : ", number_2)

# Sum of two numbers
sum = number_1 + number_2
print("The sum of two numbers is: ", sum)

# Difference of two numbers
diff = number_1 - number_2
print("The diff of two numbers is: ", diff)

# Produt of two numbers
product = number_1 * number_2
print("The product of two numbers is:", product)

# Division of two numbers

if number_2 != 0:
    division = number_1 / number_2
    print("The division of two numbers is:", division)
else:
    print("The second number is zero")

# Check it yourself:
# With 7 and 2, I got 9, 5, 14 and 3.5. I expected 3.5 because 7 / 2 = 3.5.
# My program doesn't show 3, because "/" gives the exact result. If I use "//" instead, I get 3, because "//" keeps only the whole part of the division.
# With 0 as the second number, the program shows the message "The second number is zero"