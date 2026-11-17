"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - There are 2 empty lines.
# - Two lines start with extra spaces ("  alan TURING", "  linus torvalds").
# - The capitals are inconsistent: "ada LOVELACE", "grace hopper", "GUIDO van rossum".
# - One name has three words ("GUIDO van rossum"), so the last name is not obviously the last word.

# 1. In: The file names.txt, read line by line. Everything arrives as text.
# 2. Process, problem by problem: 
#.   - empty lines: the program skips them.
#    - extra spaces: split() and join() remove them.
#    - inconsistent capitals: title() puts a capital on each word, and I put
#      "van" back in lowercase.
#    - three-word name: I take everything after the first word as the last name.
# 3. Out: A new file, names_clean.txt, with the 8 cleaned names sorted by last name, one per line. names.txt is not modified.
# 4. How I decide which word is the last name: every line is a first name followed by a last name, so the last name is everything after the first word. 
# For "Guido van Rossum" it is "van Rossum", so he is sorted under V, after Turing. 
# If I took only the last word, he would be sorted under R.


# Your code below
# Cleans one line: removes extra spaces and fixes the capitals
def clean_line(line):
    words = line.split()                 # also removes spaces at both ends
    name = " ".join(words).title()
    return name.replace(" Van ", " van ")  # "van" stays in lowercase


# Returns the last name: everything after the first word (the first name)
def get_last_name(full_name):
    words = full_name.split()
    return " ".join(words[1:]).lower()


# Reads the file and returns the list of cleaned names (no empty lines)
def load_names(filename):
    names = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            name = clean_line(line)
            if name == "":
                continue                 # skips empty lines
            names.append(name)
    return names


# Writes the names in a new file, one per line
def save_names(names, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")


names = load_names("names.txt")
sorted_names = sorted(names, key=get_last_name)
save_names(sorted_names, "names_clean.txt")

print("Names kept:", len(sorted_names))
print("First:", sorted_names[0])
print("Last:", sorted_names[-1])

# Check it yourself: names.txt has 10 lines, names_clean.txt has 8 lines. The
# difference is 2 because the 2 empty lines were removed. There were no
# duplicates. The first name is Margaret Hamilton and the last is Guido van
# Rossum, which I checked by hand.