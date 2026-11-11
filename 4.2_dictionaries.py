"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user types five pieces of information on the keyboard: a name, an age, a city, a country and a favorite brand.
# 2. Process: The program stores the five answers in a dictionary. Then it reads some fields, changes the city, removes the age and goes through the remaining fields one by one.
# 3. Out: The information typed by the user, the new city, the removed age, then every remaining field with its value, and a message for a field that does not exist.
# 4. My object, my five fields, and why those: a client card, as in a luxury boutique. Name is used to greet the client, age and city help to
# know the client's profile, country tells which language or currency to use, and favorite brand helps the advisor suggest products they will like.


# Your code below
name = input("Enter your name: ")
age = input("Enter your age: ") 
city = input("Enter your city: ")
country = input("Enter your country: ")
favorite_brand = input("Enter your favorite brand: ")

print("My name is ", name)
print("My age is ", age)
print("My city is ", city)
print("My country is ", country)
print("My favorite brand is ", favorite_brand)

person = {
    "name": name,
    "age": age,
    "city": city,
    "country": country
    "favorite_brand": favorite_brand
    }


print("The person's age is: ", person["age"])
print("The person's name is: ", person["name"])
print("The person's city is: ", person["city"])
print("The person's country is: ", person["country"])
print("The person's favorite brand is: ", person["favorite brand"])

