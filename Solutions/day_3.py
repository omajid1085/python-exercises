# Question 10

# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again

# Then, the output should be:

# again and hello makes perfect practice world

words = input('Enter a sequence of words: ').split()
for w in words:
    if words.count(w) > 1:
        words.remove(w)

words.sort()
print(' '.join(words))


# Question 11

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# **_Example:_**

# 0100,0011,1010,1001

# Then the output should be:

# 1010

# Notes: Assume the data is input by console.

data = str(input('Enter a sequence of binary numbers: ')).split()
data = list(filter(lambda i: int(i, 2) % 5 == 0, data))
print(','.join(data))


# Question 12

# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

lst = [str(i) for i in range(1000, 3001)]
# using lambda to define function inside filter function
lst = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst))
print(",".join(lst))


# Question 13

# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123

# Then, the output should be:

# LETTERS 10
# DIGITS 3

sentence = input('Enter a sentence: ')
letters, digits = 0, 0

for i in sentence:
    if i.isalpha():
        letters += 1
    if i.isnumeric():
        digits += 1

print(f'Letters: {letters}\nDigits: {digits}')
