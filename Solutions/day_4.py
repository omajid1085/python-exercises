# Question 14

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!

# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

sentence = input('Enter a sentence: ')

upper = 0
lower = 0

for l in sentence:
    if l.isupper():
        upper += 1
    if l.islower():
        lower += 1

print(f'UPPER CASE {upper}\nLOWER CASE {lower}')


# Question 15

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program:

# 9

# Then, the output should be:

# 11106

a = input('Enter a number: ')
aa = int(a+a)
aaa = int(a+a+a)
aaaa = int(a+a+a+a)

print(int(a)+aa+aaa+aaaa)
