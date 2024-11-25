print("Welcome to Fibonacci Series Generator")
global num1
global num2
global num_inputs
global z
z = 0
while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num_inputs = int(input("How many numbers do you want in the series?: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
print(num1)
print(num2)

while(z< num_inputs):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3
    z+=1

while True:
    try:
        rating = int(input("Rate This program from 1 to 10: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")  

if(rating>10):
    print("Amazing review, I will make another project for you!!")
elif(rating >= 7):
    print("Thanks for the Feedback!")
elif(rating < 7 and rating > 3):
    print("Okay Thanks....")
elif(rating <= 3 and rating>0):
    print("Sorry for hearing that, How may I improve my project?")
else:
    print("Usually Morons Give this rating.?")