# Question 20

# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:

# 7
# Then, the output should be:

# 0
# 7
# 14

from math import sqrt


class Divisible:

    def by_seven(self, n):
        for number in range(1, n + 1):
            if number % 7 == 0:
                yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)


# Question 21

# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

# Example:
# If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# Then, the output of the program should be:

# 2

lst = []
position = [0, 0]
while True:
    a = input()
    if not a:
        break
    lst.append(a)
for i in lst:
    if 'UP' in i:
        position[0] -= int(i.strip('UP '))
    if 'DOWN' in i:
        position[0] += int(i.strip('DOWN '))
    if 'LEFT' in i:
        position[1] -= int(i.strip('LEFT '))
    if 'RIGHT' in i:
        position[1] += int(i.strip('RIGHT '))
        
print(round(sqrt(position[1] ** 2 + position[0] ** 2)))
