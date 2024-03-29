from instream import InStream
from symboltable import SymbolTable
import stdio
import sys


# Entry point.
def main():
    # Accept filename (str) as command-line argument.
    filename = str(sys.argv[1])

    # Set inStream to an input stream built from filename.
    instream = InStream(filename)

    # Set words to the list of strings read from inStream.
    words = instream.readAllStrings()
    # Set occurrences to a new symbol table object.
    occurences = SymbolTable()

    for i, word in enumerate(words):
        # For each word (having index i) in words...

        # If word does not exist in occurrences, insert it with an empty list as the value.
        if word not in occurences:
            occurences[word] = []

        # Append i to the list corresponding to word in occurrences.
        occurences[word].append(i)

    while not stdio.isEmpty():
        # As long as standard input is not empty...

        # Set word to a string read from standard input.
        word = stdio.readString()

        # If word exists in occurrences, write the word and the corresponding list to standard
        # output, separated by the string '->'. Otherwise, write the message 'Word not found'.
        if word in occurences:
            stdio.writeln(word + ' -> ' + str(occurences[word]))
        else:
            stdio.writeln('Word not found')


if __name__ == '__main__':
    main()
