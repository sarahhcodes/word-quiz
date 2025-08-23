# TO DO:
# more introductions
# generate quiz
# end screen with option to repeat or save
# save function
# load function
# error handling
# tests
# docstrings for all functions
# include text-to-csv utility

import argparse
import csv
from random import randrange
import sys

class Player:
    def __init__(self, rounds):
        self.introduction() # automatically introduces game if player is initalized

        self.score = 0
        self.rounds = rounds
    
    def introduction(self):
        # introduce player to the quiz
        print("Welcome to the quiz!")
        # explain quiz...

    def reset(self, rounds):
        self.scoure = 0
        self.rounds = rounds

def main():
    parser = argparse.ArgumentParser(description="Generate quiz from CSV file")
    parser.add_argument("-c", "--csv", help="CSV file to act as source for quiz", required=True)
    parser.add_argument("-l", "--load", help="Load save file of words to study.", required=False)
    args = parser.parse_args()

    player = Player(int(input("How many rounds? ")))
    full_list = load_list(args.csv)

    if not args.load:
        questions = generate_questions(full_list, player.rounds)
    else:
        # load save state
        ...


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


def load():
    """Load list from save file."""
    ...

def generate_quiz():
    """Generates the quiz."""
    ...


def save():
    """Saves the quiz for future study."""
    ...


if __name__ == "__main__":
    main()