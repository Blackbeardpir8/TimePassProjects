#1. Take two numbers as input from User and print which one is greater or are they equal.
num1 = int(input("Enter a Number = "))
num2 = int(input("Enter a Number = "))
if num1 > num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")


#2. Take three numbers as input from User and print which one is greater or are they equal.
# 2. Take three numbers as input from the user and print which one is greater or if they are equal.

numbr1 = int(input("Enter the first number: "))
numbr2 = int(input("Enter the second number: "))
numbr3 = int(input("Enter the third number: "))


if numbr1 > numbr2 and numbr1 > numbr3:
    print(f"{numbr1} is the greatest.")
elif numbr2 > numbr1 and numbr2 > numbr3:
    print(f"{numbr2} is the greatest.")
elif numbr3 > numbr1 and numbr3 > numbr2:
    print(f"{numbr3} is the greatest.")
else:
    print("All numbers are equal or there is a tie between the greatest numbers.")

"""3. Take Salary as input from User and Update the salary of an employee
a. salary less than 10,000, 5 % increment
b. salary between 10,000 and 20, 000, 10 % increment
c. salary between 20,000 and 50,000, 15 % increment
d. salary more than 50,000, 20 % increment"""

salary = int(input("Enter your Salary = "))
if salary < 10000:
    new_salary = salary + (salary * 0.05)
    print(f"Your salary of {salary} after a 5% increment is {new_salary}")
elif 10000 <= salary <= 20000:
    new_salary = salary + (salary * 0.10)
    print(f"Your salary of {salary} after a 10% increment is {new_salary}")
elif 20000 < salary <= 50000:
    new_salary = salary + (salary * 0.15)
    print(f"Your salary of {salary} after a 15% increment is {new_salary}")
elif salary > 50000:
    new_salary = salary + (salary * 0.20)
    print(f"Your salary of {salary} after a 20% increment is {new_salary}")
else:
    print("Invalid salary input.")


#4. Ask the number from User and print whether the number is Odd or Even.
number = int(input("Enter a Number = "))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


"""5. A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 – A
Ask user to enter marks and print the corresponding grade."""

marks = int(input("Enter your Marks = "))
if marks>=80:
    print("You Grade = A")
elif marks>=60 and marks<=80:
    print("your Grade = B")
elif marks>=50 and marks<=60:
    print("your Grade = C")
elif marks>=45 and marks<=50:
    print("your Grade = D")
elif marks>=25 and marks<=45:
    print("your Grade = E")
else :
    print("your Grade = F")

"""6. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
a. Take following input from user
i. Number of classes held
ii. Number of classes attended.
b. Print percentage of class attended
c. Print Is student is allowed to sit in exam or not."""

Number_of_classes_held = int(input("Enter Number of classes held = "))
Number_of_classes_attended = int(input("Enter Number of classes attended = "))

percentage_of_class_attended = (Number_of_classes_attended/Number_of_classes_held)*100
print(percentage_of_class_attended)

if percentage_of_class_attended >= 75:
    print("You are Allowed to Sit in Exam")
else:
    print("You are not Allowed to Sit in Exam")


"""7. Calculate the purchase amount after deduction criteria on printed price
a. printed price between 500 and 1000, allow 5% discount
b. printed price between 1000 and 5000, allow 10% discount
c. printed price between 5000 and 10000, allow 15% discount
d. printed price more than 10000, allow 20% discount"""