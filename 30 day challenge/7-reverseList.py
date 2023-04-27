#_______Write a function that reverses a list of strings.
wordList = input('Enter some words: ').split()

def reversedList(wordList):
    r = list(wordList)
    r.reverse()
    return str(r)


print(reversedList(wordList))
