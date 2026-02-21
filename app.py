#import all the modules you need, below this line


#write any functions you need, below this line


#use the main() function for your program, define all other functions above main
def main ():

from collections import defaultdict


def interpret_score(score):
    """
    Pure function that interprets a numeric score
    and returns a descriptive label.
    """
    if score >= 12:
        return "High"
    elif 6 <= score <= 11:
        return "Moderate"
    else:
        return "Low"


def get_valid_input(prompt):
    """
    Prompts the user until a valid integer between 0 and 7 is entered.
    Uses exception handling to avoid crashing.
    """
    while True:
        try:
            value = int(input(prompt))

            if 0 <= value <= 7:
                return value
            else:
                print("Error: Please enter a number between 0 and 7.")

        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")


def run_quiz():
    """
    Runs the habit tracker quiz and prints results.
    """

    questions = [
        # SleepRoutine (3)
        {"text": "How many days per week do you go to bed at a consistent hour? ", "habit": "SleepRoutine"},
        {"text": "How many days per week do you sleep at least 7-8 hours? ", "habit": "SleepRoutine"},
        {"text": "How many days per week do you avoid screens before bedtime? ", "habit": "SleepRoutine"},

        # PhysicalActivity (3)
        {"text": "How many days per week do you exercise for at least 20 minutes? ", "habit": "PhysicalActivity"},
        {"text": "How many days per week do you walk at least 30 minutes? ", "habit": "PhysicalActivity"},
        {"text": "How many days per week do you stretch or do strength exercises? ", "habit": "PhysicalActivity"},

        # HealthyEating (3)
        {"text": "How many days per week do you eat at least one healthy meal? ", "habit": "HealthyEating"},
        {"text": "How many days per week do you eat fruits and vegetables? ", "habit": "HealthyEating"},
        {"text": "How many days per week do you avoid fast food? ", "habit": "HealthyEating"},

        # Mindfulness (3)
        {"text": "How many days per week do you practice mindfulness or meditation? ", "habit": "Mindfulness"},
        {"text": "How many days per week do you take time to relax? ", "habit": "Mindfulness"},
        {"text": "How many days per week do you journal or reflect? ", "habit": "Mindfulness"},

        # SocialConnection (3)
        {"text": "How many days per week do you spend meaningful time with others? ", "habit": "SocialConnection"},
        {"text": "How many days per week do you talk with friends or family? ", "habit": "SocialConnection"},
        {"text": "How many days per week do you participate in social activities? ", "habit": "SocialConnection"},
    ]

    scores = defaultdict(int)

    print("=== Weekly Habit Tracker ===")
    print("Please answer each question with a number between 0 and 7.\n")

    for item in questions:
        answer = get_valid_input(item["text"])
        scores[item["habit"]] += answer

    print("\n=== Results ===")

    for habit, total in scores.items():
        interpretation = interpret_score(total)
        print(f"{habit}: Score {total} → {interpretation}")


if __name__ == "__main__":
    run_quiz()
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()
