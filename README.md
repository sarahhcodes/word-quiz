# word-quiz
A quiz generator for learning vocabulary

## Introduction
This program is designed to create quizes in the command line from CSV or text file lists of vocabuary words. It is also my final project for [Harvard's CS50 Introduction to Programming with Python](https://cs50.harvard.edu/python/).

## How to Use
### Requirements
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

### Instructions
...

### Formatting Text File
To use the program properly, the text files should consist of a list of vocabuary words, one on each line and seperated by a consistant character (such as ':', '-', etc).

The sample text files included in the /txt folder were copy and pasted from websites.

## Design
My intention with the program was to make lists of words copy and pasted from the internet into something useful for study.

I opted for a command line program to keep the project simple.

## Possible extensions
- I am studying Japanese, and it would be useful to import and quiz files with multiple columns for each word. For example, it would be useful for kanji study to have the kanji, the on reading (Chinese reading), the kun reading (Japanese reading), and the English translation.
- Importing API from websites like [Wanikani](http://wanikani.com), giving an alternate way to study other vocabuary sources.
- Option to have the quiz run in the opposite direction. (From English to Japanese for instance rather than just Japanese to English)

## Credits
- INCLUDE SOURCES FOR WORD LISTS
