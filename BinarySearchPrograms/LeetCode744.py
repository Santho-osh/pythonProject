def nextBigLetter(letter, target):
    start = 0
    end = len(letter)-1
    while start <= end:
        middle = end-start//2
        if target>middle:
            start = middle+1
        else:
            end = middle-1
    return letter[start % len(letter)]

letters = ['']



