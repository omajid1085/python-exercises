from math import sqrt
# Question 4

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:

# 34,67,55,33,12,98

# Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

lst = input().split(', ')
tup = tuple(lst)

print(list(lst))
print(tup)


# Question 5

# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case

# Also please include simple test function to test the class methods.

class Strng:
    def getString(self):
        self.s = input('Enter a string: ')

    def printString(self):
        print(self.s.upper())


xx = Strng()
xx.getString()
xx.printString()

# Question 6

# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence. For example:

# Let us assume the following comma separated input sequence is given to the program:

# 100,150,180

# The output of the program should be:

# 18,22,24

C, H = 50, 30


def calc(D):
    return sqrt((2*C*D)/H)


D = input('Enter a list of numbers: ').split(', ')
D = [str(round(calc(int(i)))) for i in D]
print(", ".join(D))


# Question 7

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.

# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

# Then, the output of the program should be:

# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x, y = map(int, input().split(', '))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)
    lst.append(tmp)

print(lst)

# Question 8

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program:

# without,hello,bag,world

# Then, the output should be:

# bag,hello,without,world

words = input('Enter a few words: ').split(', ')
print(', '.join(sorted(words)))

# Question 9

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the program:

# Hello world
# Practice makes perfect

# Then, the output should be:

# HELLO WORLD
# PRACTICE MAKES PERFECT

lst = []

while True:
    x = input()
    if len(x) == 0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)
