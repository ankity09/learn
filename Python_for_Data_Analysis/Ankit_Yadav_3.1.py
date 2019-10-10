#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT, #and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 7 DOWN 5 LEFT 2 #RIGHT 9 X
#The numbers after the direction are steps. Please write a Python program to compute the distance from the #current position after a sequence of movement and original point. If the distance is a float, then just #print the nearest integer.
#Example: If the following movements obtained from the user input are given to the program: UP 5 DOWN 3 LEFT #3 RIGHT 2 X
#Then the output of the program should be: 2 Note: X means the end of movement.

import math
position = {"x": 0, "y": 0}

while True:
    directions = input("Please give directions(X to exit) and steps: ")
    
    if directions == "X":
        break

    direction, steps = directions.split()
    if direction == "UP":
        position["y"] += int(steps)
    elif direction == "DOWN":
        position["y"] -= int(steps)
    elif direction == "LEFT":
        position["x"] -= int(steps)
    elif direction == "RIGHT":
        position["x"] += int(steps)

print(round(math.sqrt(position["y"]**2+position["x"]**2)))

#Write a Python program to compute the frequency of words from the article. The output should output after #sorting the key alphanumerically. Suppose the article is obtained from the user. The input ends until the #user sends a new line: X
#Example: Please provide the article:
#Beginner means someone who has just gone through an introductory Python course.
#He can solve some problems with 1 or 2 Python classes or functions.
#Normally, the answers could directly be found in the textbooks.
#Intermediate means someone who has just learned Python, but already has a relatively strong programming #background from before.
#X

Text = " "
print("---\nEnter Article: ")
while True:
    nline = input()
    if nline == "X":
        break
    else:
        nline += " "
        Text += nline

# Cleaning text and lower casing all words
for char in '-.,\n':
    Text=Text.replace(char,' ')
Text = Text.lower()

word_list = Text.split()
# Initializing Dictionary
d = {}

# counting number of times each word comes up in list of words (in dictionary)
for word in word_list: 
    d[word] = d.get(word, 0) + 1
    

word_freq = []
for key, value in d.items():
    word_freq.append((value, key))

word_freq.sort(reverse=False)
print(word_freq)

