# Name : Lucie GROUARD-FANG
# Group : CL10
# Scenario C

# My feature: d (difficulty). I chose it because it is simple and reliable:
# one question at the start changes the starting budget, so the player can
# choose between an easy and a hard game.
#
# 1. What goes in?
#    The game reads my group's file, scenarios_C.csv.
#    - Separator: a comma. Some cells contain commas, but they are inside
#      quotation marks, so I read the file with the csv module.
#    - Columns (14): Event (the situation), Day (the scenario number, 1 to 30),
#      Decision 1/2/3 (the text of options A, B, C), Reputation 1/2/3 and
#      Budget 1/2/3 (the impact of each option), Outcome 1/2/3 (the feedback
#      of each option).
#    - Numbers: they are written as text with a unit, like "-800 EUR" or
#      "+15 pts", so I must remove the unit and convert to int before computing.
#    - Option B: its text is in Decision 2, its impacts in Reputation 2 and
#      Budget 2, and its feedback in Outcome 2.
#    The player also types their name, then the difficulty, then A, B or C
#    each day.
#
# 2. What happens?
#    - The program asks the player's name and the difficulty (easy or hard),
#      which sets the starting budget.
#    - It loads all the scenarios, shuffles them and plays 10 days.
#    - Each day it shows the day number, both gauges, the situation and the
#      options A, B, C.
#    - It asks for A, B or C until the answer is valid (a, b, c are accepted).
#    - It applies the budget and reputation changes and shows the feedback line.
#    - It caps the reputation at 100 and keeps the move in the history.
#    - If budget or reputation is 0 or less, the game stops at once.
#    - At the end it computes the score and the title, shows the best and the
#      worst move, and saves one line in results.csv.
#
# 3. What comes out?
#    The player sees either "fired" and the reason (which gauge hit zero), or
#    "Quarter survived!" with the budget left, the reputation, the score, the
#    title, and the best and worst move.
#    One line of results.csv looks like this:
#    Lucie,6350,100,CMO Material,2026-11-16
#    (name, budget, reputation, title, date)
#
# 4. What could go wrong?
#    - The player types something other than A, B or C: the program cleans the
#      answer and asks again until it is valid.
#    - The scenario file is missing: the program shows a clear message and
#      stops without crashing.
#    - A number is written like "-800 EUR": the program removes the unit
#      before converting it to an integer.
#    - Budget or reputation goes to 0 or below: the game stops immediately and
#      shows that the player is fired.
#    - The reputation goes above 100: the program sets it back to 100.
#    - results.csv does not exist yet: the program creates it the first time.


# Code
import csv
import random
from datetime import date

def clean_number(text):
    return int(text.replace("EUR", "").replace("pts", "").strip())


def load_scenarios(filename):
    scenarios = []
    with open(filename, encoding="utf-8") as file:
        for row in csv.DictReader(file):
            options = []
            for i in ("1", "2", "3"):
                option = (row["Decision " + i],
                          clean_number(row["Budget " + i]),
                          clean_number(row["Reputation " + i]),
                          row["Outcome " + i])
                options.append(option)
            scenarios.append((row["Event"], options))
    return scenarios


# Asks A, B or C until the answer is valid, returns 0, 1 or 2
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().lower()
    while answer not in ("a", "b", "c"):
        answer = input("Please type A, B or C: ").strip().lower()
    return "abc".index(answer)


# Applies the option to the gauges and returns the new values (a tuple)
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(100, reputation + reputation_change)
    return budget, reputation


# Returns the title for a final score
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"


# Feature d: asks the difficulty and returns the starting budget
def ask_starting_budget():
    level = input("Difficulty: easy (15000 EUR) or hard (6000 EUR)? ").strip().lower()
    if level == "easy":
        return 15000
    elif level == "hard":
        return 6000
    return 10000


# Saves one line in results.csv (the file is created if it does not exist)
def save_result(name, budget, reputation, title):
    with open("results.csv", "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([name, budget, reputation, title, date.today()])


# Main game
def play():
    name = input("Your name: ").strip()
    budget = ask_starting_budget()
    reputation = 50

    try:
        scenarios = load_scenarios("scenarios_C.csv")
    except FileNotFoundError:
        print("The file scenarios_C.csv was not found.")
        return
    random.shuffle(scenarios)

    history = []
    fired = False

    for day in range(1, 11):
        situation, options = scenarios[day - 1]
        print("\n--- Day", day, "---")
        print("[Budget:", budget, "EUR | Reputation:", str(reputation) + "/100]")
        print(situation)
        for letter, option in zip("ABC", options):
            print(" ", letter + ":", option[0])

        index = ask_choice()
        option = options[index]
        budget, reputation = apply_choice(budget, reputation, option)
        print(option[3])
        print("Budget", option[1], "EUR, Reputation", option[2])

        # History: one tuple per day, reputation change first
        history.append((option[2], day, option[0]))

        if budget <= 0 or reputation <= 0:
            fired = True
            break

    print("\n==============================")
    if fired:
        if budget <= 0:
            print("You are fired: the budget hit zero.")
        else:
            print("You are fired: the reputation hit zero.")
        title = "Fired"
    else:
        score = reputation + budget // 200
        title = get_title(score)
        print("Quarter survived!")
        print("Budget left:", budget, "EUR, reputation:", str(reputation) + "/100")
        print("Final score:", score)
        print(name + ", your title:", title)

    best = max(history)
    worst = min(history)
    print("Best move: day", best[1], ",", best[2], "(" + str(best[0]) + ")")
    print("Worst move: day", worst[1], ",", worst[2], "(" + str(worst[0]) + ")")

    save_result(name, budget, reputation, title)
    print("Saved in results.csv")


play()
