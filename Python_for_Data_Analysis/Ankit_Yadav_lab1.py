from __future__ import print_function

# Write a Python program that prints each item and its corresponding type from the following list.
datalist = [1452, 11.23, 1+2j, True, 'University of Maryland', (0, -1), [5, 12], {"class":'404', "section":'A'}]

for i in range(0, len(datalist)):
    print(datalist[i])

#Create a calculator that can add, subtract, multiply or divide depending upon the input from the user, using loop and conditional statements.
print("Select operation:1.Add 2.Subtract 3.Multipy 4.Divide")
choice = input('''Enter Choice(1/2/3/4):''')

first_number = int(input('''Enter First Number:'''))
second_number = int(input('''Enter Second Number:'''))

if choice == '1':
    print("{} + {} = ".format(first_number, second_number),first_number + second_number)
    run = input('''Do you want to do another calculation(y/n)?  ((if ‘y’, run your program again))''')
    if run == 'n':
        print('Bye')
elif choice == '2':
    print("{} - {} = ".format(first_number, second_number),first_number - second_number)
    run = input('''Do you want to do another calculation(y/n)?  ((if ‘y’, run your program again))''')
    if run == 'n':
        print('Bye')
elif choice == '3':
    print("{} * {} = ".format(first_number, second_number),first_number * second_number)
    run = input('''Do you want to do another calculation(y/n)?  ((if ‘y’, run your program again))''')
    if run == 'n':
        print('Bye')
elif choice == '4':
    print("{} / {} = ".format(first_number, second_number),first_number / second_number)
    run = input('''Do you want to do another calculation(y/n)?  ((if ‘y’, run your program again))''')
    if run == 'n':
        print('Bye')







#Write a Python program to construct the following pattern, using a nested loop. The longest line (n) is from user input (e.g., n=5 for the following pattern).

n = int(input('''Enter Number:'''))

for i in range(0, n):
    for j in range(0,i+1):
        print("*", end = " ")
    print("\r") 
for i in range (n-1, -1, -1):
    for j in range(i, 0, -1):
        print("*", end = " ")
    print("\r")