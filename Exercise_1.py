# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.
import datetime as dt
nm = input('Please Enter your Name\n')
print('Hello ' + nm + '!')
ag = int(input('How old are you ?\n'))
y = dt.datetime.now()
z = (y.year) + (100 - ag)
print('You will turn 100 in the year ' + str(z))
