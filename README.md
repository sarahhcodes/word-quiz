# word-quiz
A quiz generator for learning vocabulary

## Introduction
This program is designed to create quizes in the command line from CSV or text file lists of vocabuary words. It is also my final project for [Harvard's CS50 Introduction to Programming with Python](https://cs50.harvard.edu/python/).

## Requirements
- argparse
    - Parses command line arguments
- csv
    - Handles CSV import
- num2words
    - Converts numbers to words for readability when asking for columns
- random
    - Chooses random questions for the quiz
- rich
    - Aids in readability and clarity in the program
- sys
    - Quits when appropriate


## Instructions
### Installing Libraries
To install pip-installable libraries, use the command:

`pip install -r requirements.txt`


### Running from command line
To use the program, type:
python project.py *optional flags*

Optional Flags:
*Using these flags will bypass a default import menu*
- -c or --csv
    - CSV file to act as source for quiz
- -t or --text
    - Text file to input
- -l or --columns
    - Columns for list
- -s or --split_on
    - Character to split on (examples: ':', '-', etc)

For example, to import the included vocabulary csv, run:

`python project.py -c csv/vocab.csv`

or to import the included vocabulary text file, run:

`python project.py -t txt/JLPTN3vocab.txt -l Japanese English -s :`

If you do not use these flags, the program will run an import menu for the user to import their csv or text file.
    

### Generating Quiz
After importing the file, the user will be prompted to enter how many words they would like to be quized on. (Up to a maximum of 10)

The program will then generate a randomly generated quiz of however many words the user selected.

After the round is finished, the user will see their final score and will be prompted to run the quiz again.

If the quiz is run again, after the quiz is finished, the user's new score will be added to their total score and the user will be prompted to run the quiz again.

This process will continue until the user quits by declining to play again.

### Formatting Text File
To use the program properly, the text files should consist of a list of vocabuary words, one on each line and seperated by a consistant character (such as ':', '-', etc) that is ONLY used between each vocabuary term.

For example:

```赤い (akai): red```

The sample text files included in the /txt folder were copy and pasted from websites.

## Design
My intention with the program was to make lists of words copy and pasted from the internet into something useful for study.

I opted for a command line program to keep the project simple.

To improve readability in the terminal, I used the Rich library to add colour and formatting to the program.

## Possible extensions
- I am studying Japanese, and it would be useful to import and quiz files with multiple columns for each word. For example, it would be useful for kanji study to have the kanji, the on reading (Chinese reading), the kun reading (Japanese reading), and the English translation.
- Importing API from websites like [Wanikani](http://wanikani.com), giving an alternate way to study other vocabuary sources.
- Option to have the quiz run in the opposite direction. (From English to Japanese for instance rather than just Japanese to English)

## Credits
The included source file for the test vocabuary is from [JTest4You](http://japanesetest4you.com/jlpt-n3-vocabulary-list/) and was downloaded August 16, 2025.

Special thank you to the [CS50P](https://cs50.harvard.edu/python/) course team!