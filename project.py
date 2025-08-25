# TO DO:
# add & adjust text w/focus on player experience
# error handling
# tests
# docstrings for all functions
# include text-to-csv utility

import argparse
import csv
from random import shuffle, randrange
import sys

class Game:
    def __init__(self, rounds):
        self.introduction() # automatically introduces game if player is initalized

        self.score = 0
        self.total_questions = 0
        self.rounds = rounds
    
    def introduction(self):
        # introduce player to the quiz
        print("Welcome to the quiz!")
        # explain quiz...

    def reset(self, rounds):
        self.score = 0
        self.rounds = rounds

def main():
    parser = argparse.ArgumentParser(description="Generate quiz from CSV file")
    parser.add_argument("-c", "--csv", help="CSV file to act as source for quiz", required=True)
    args = parser.parse_args()

    game = Game(int(input("How many rounds? ")))
    full_list = load_list(args.csv)

    while True:
        game.score = generate_quiz(full_list, generate_questions(full_list, game.rounds))
        game.total_questions += game.rounds

        print(f"Your total score is {game.score} out of {game.total_questions} ({int(game.score/game.total_questions*100)}%)")

        if not play_again():
            print("Thanks for playing!")
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

def generate_quiz(full_list, questions):
    """Generates the quiz."""
    correct = []
    incorrect = []

    for question in questions:
        answers = []
        answers.append(list(question.values())[1])
        index = []

        for _ in range(3):
            n = randrange(len(full_list))

            while n in index:
                n = randrange(len(full_list))

            answers.append(list(full_list[n].values())[1])
            index.append(n)
        
        shuffle(answers)
        print(f"What's {list(question.values())[0]}?")

        for i, answer in enumerate(answers):
            print(f"{i+1}) {answer}")
        
        guess_index = int(input("????? "))

        guess = answers[guess_index-1]
        print(f"Your answer: {guess}")
        print(f"Correct answer: {list(question.values())[1]}")

        if list(question.values())[1] == guess:
            print("Correct!\n")
            correct.append(question)

        else:
            print("Incorrect...\n")
            incorrect.append(question)
    
    print(f"You got {len(correct)} questions right and {len(incorrect)} wrong.")
    print(f"Final score: {len(correct)}/{len(questions)}")
    if len(correct) == len(questions):
        print("CONGRATULATIONS!!!!!")

    return len(correct)

def play_again():
    """Determine if player wants to play another round"""
    no_choice = True

    while no_choice:
        try:
            choice = input("Would you like to play again? y/n ").casefold()
            if choice == 'y':
                no_choice = False
                return True
            elif choice == 'n':
                no_choice = False
                return False
            else:
                raise ValueError
        except ValueError:
            pass


if __name__ == "__main__":
    main()