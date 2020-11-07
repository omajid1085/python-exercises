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

# > **_Define a class which has at least two methods:_**
# >
# > - **_getString: to get a string from console input_**
# > - **_printString: to print the string in upper case._**

# > **_Also please include simple test function to test the class methods._**

class Strng:
    def getString(self):
        self.s = input('Enter a string: ')

    def printString(self):
        print(self.s.upper())


xx = Strng()
xx.getString()
xx.printString()

# Question 6

# > **_Write a program that calculates and prints the value according to the given formula:_**

# > **_Q = Square root of [(2 _ C _ D)/H]_**

# > **_Following are the fixed values of C and H:_**

# > **_C is 50. H is 30._**

# > **_D is the variable whose values should be input to your program in a comma-separated sequence.For example
# > Let us assume the following comma separated input sequence is given to the program:_**

# 100,150,180

# > **_The output of the program should be:_**

# 18,22,24

C, H = 50, 30


def calc(D):
    return sqrt((2*C*D)/H)


D = input('Enter a list of numbers: ').split(', ')
D = [str(round(calc(int(i)))) for i in D]
print(", ".join(D))


# Question 7

# > **_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.\***

# > **_Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5_**

# > **_Then, the output of the program should be:_**

# ```
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

# > **_Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically._**

# > **_Suppose the following input is supplied to the program:_**

# ```
# without,hello,bag,world
# ```

# > **_Then, the output should be:_**

# ```
# bag,hello,without,world

words = input('Enter a few words: ').split(', ')
print(', '.join(sorted(words)))

# Question 9

# > **_Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized._**

# > **_Suppose the following input is supplied to the program:_**

# ```
# Hello world
# Practice makes perfect
# ```

# > **_Then, the output should be:_**

# ```
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
