#1. Write a program that takes two numbers as input from the user and then prints the sum of these numbers.

a = 11
b= 44
print(a+b)

#2 Write a Program that takes Length and Breadth as input from user and print the Area of Rectangle.
length = float(input("Enter Length of Rectangle = "))
breadth = float(input("Enter Breadth of Rectangle = "))

area = length*breadth
print(area)

#3. Ask 3 numbers from User and Calculate the Average.

num1 = int(input("Enter a Number = "))
num2 = int(input("Enter a Number = "))
num3 = int(input("Enter a Number = "))

avg = (num1+num2+num3)/3
print(avg)

#4&5. Calculate sum of 5 subjects and Find percentage.
english = float(input("Enter marks = "))
maths = float(input("Enter marks = "))
physics = float(input("Enter marks = "))
chemistry = float(input("Enter marks = "))
biology = float(input("Enter marks = "))

total_marks = english+maths+physics+chemistry+biology
percentage = (total_marks/500)*100


#6. Ask value in Rupees and Convert into Paise.
rupees = float(input("Enter the amount = "))
paise = rupees*100
print(paise)

#7. Calculate Area of Square by taking Length from User.
length = float(input("Enter the Length of Square = "))
area_sq = length*length
print(area_sq)


#8. Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points).
games_palyed = int(input("Enter number of games played = "))
game_won = int(input("Enter number of games won = "))
game_loss = int(input("Enter number of games loss = "))
tie = games_palyed-(game_won+game_loss)
total_points = (game_won*4)+(tie*2)
print(total_points)