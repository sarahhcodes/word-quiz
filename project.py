# TO DO:
# tests
# docstrings for all functions
# include text-to-csv utility

import argparse
import csv
from random import shuffle, randrange
from rich import box
from rich.console import Console
from rich.table import Table
from rich.text import Text

class Game:
    def __init__(self, console, rounds):
        self.console = console
        self.score = 0
        self.total_questions = 0
        self.rounds = rounds

    def reset(self, rounds):
        self.score = 0
        self.rounds = rounds

def main():
    parser = argparse.ArgumentParser(description="Generate quiz from CSV file")
    parser.add_argument("-c", "--csv", help="CSV file to act as source for quiz", required=True)
    args = parser.parse_args()

    console = Console()
    #introduction = Text("Welcome to the quiz!", justify="center")
    console.rule("Welcome to the quiz!")
    while True:
        try:
            rounds = int(input("How many words would you like to be quized on? "))
            if rounds <= 0:
                console.print("Input a number greater than 0.")
            elif rounds > 10:
                console.print("Input a number 10 or less.")
            else:
                break
        except ValueError:
            console.print("Enter a valid number between 1 and 10 inclusive.")
   
    game = Game(console, rounds)

    full_list = load_list(args.csv)

    while True:
        game.score = generate_quiz(console, full_list, generate_questions(full_list, game.rounds))
        game.total_questions += game.rounds

        console.print(f"Your total score is {game.score} out of {game.total_questions} ({int(game.score/game.total_questions*100)}%)", end="\n\n")

        if not play_again():
            console.rule("Thanks for playing!")
            break
        


def load_list(source_file):
    """Imports source from CSV file and returns the full list."""
    full_quiz_list = []

    with open(source_file) as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            full_quiz_list.append(row)
    
    return full_quiz_list


def generate_questions(full_list, rounds):
    """Generates list of words to quiz from list."""
    quiz_list = []
    quiz_index = []
    n = randrange(len(full_list))
    
    for _ in range(rounds):
        # ensuring no repetition in quiz_list
        # if n is in quiz_index, keep trying to find another random number
    
        while n in quiz_index:
            n = randrange(len(full_list))
    
        quiz_index.append(n)

        quiz_list.append(full_list[n])

    return quiz_list

def generate_quiz(console, full_list, questions):
    """Generates the quiz."""
    correct = []
    incorrect = []

    for question in questions:
        answers = []
        answers.append(list(question.values())[1])
        index = []

        for _ in range(3):
            n = randrange(len(full_list))

            while n in index and not question.values() == full_list[n].values():
                n = randrange(len(full_list))

            answers.append(list(full_list[n].values())[1])
            index.append(n)
        
        shuffle(answers)
        console.print("") # margin

        # displaying question
        table = Table(title=f"What's {list(question.values())[0]}?", show_header=False, show_lines=True, box=box.ASCII)
        table.add_column()
        table.add_column()

        for i, answer in enumerate(answers):
            table.add_row(str(i+1), answer)
        
        console.print(table)

        # getting the player's input
        while True:
            try:
                arrows = "-------> "
                console.print(arrows, end="")

                guess_index = int(input())
                if guess_index < 1 or guess_index > 4:
                    console.print("Invalid answer.")
                else:
                    break
            except ValueError:
                console.print("Invalid answer.")

        guess = answers[guess_index-1]

        if list(question.values())[1] == guess:
            colour = "green"
        else:
            colour = "red"

        your_answer = Text(f"Your answer: {guess}")
        correct_answer = Text(f"Correct answer: {list(question.values())[1]}", style=colour)

        console.print(your_answer)
        console.print(correct_answer)

        #console.print(f"Your answer: {guess}")
        #console.print(f"Correct answer: {list(question.values())[1]}")

        if list(question.values())[1] == guess:
            console.print("Correct!\n")
            correct.append(question)

        else:
            console.print("Incorrect...\n")
            incorrect.append(question)
    
    console.print(f"You got {len(correct)} questions right and {len(incorrect)} wrong.")
    console.print(f"Final score: {len(correct)}/{len(questions)}")
    if len(correct) == len(questions):
        console.print("CONGRATULATIONS!!!!!")

    return len(correct)

def play_again():
    """Determine if player wants to play another round"""
    while True:
        try:
            choice = input("Would you like to play again? y/n ").casefold()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                raise ValueError
        except ValueError:
            pass


if __name__ == "__main__":
    main()