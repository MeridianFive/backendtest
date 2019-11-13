#problems 1, 2 and 4

import sys

def reverseletters(r): #reverses letters in a word
    answer = []
    answer = r[::-1] 
    return answer


def reversewords(r): #reverses words in a sentence
    answer = []
    x = r.split()

    for elem in x:
        answer.insert(0, elem)

    string = ' '.join(answer)
    return string


def main():

    string = sys.argv[1] #argv[0] being the py file
    switch = sys.argv[2] #an arguement for -r and -w


    if switch == '-r':
        x = reverseletters(string)
        print(x)

    if switch == "-w":
        x = reversewords(string)
        print(x)

    #this project assumes the input file is nothing but single words,
    #or words seperated by whitespace. If I were to elaborate, I would use
    # .sub(), .split(), .join() and regex to clean up the raw file input.
main()
