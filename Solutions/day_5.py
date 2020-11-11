# Question 16

# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

# Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9

# Then, the output should be:

# 1,9,25,49,81

lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))

# Question 17

# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200

# - D means deposit while W means withdrawal.

# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100

# Then, the output should be:

# 500

total = 0
while True:
    s = input().split()
    if not s:            # break if the string is empty
        break
    # two inputs are distributed in cm and num in string data type
    cm, num = map(str, s)

    if cm == 'D':
        total += int(num)
    if cm == 'W':
        total -= int(num)

print(total)

