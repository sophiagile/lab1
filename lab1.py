# Exercise 2.2
print("Hello")
name = input('Enter your name: ')
print('Hello', name)

# Exercise 2.3
xh = int(input('Enter Hours: '))
xr = int(input('Enter Rate: '))
xp = xh * xr
print("Pay:",xp)

# Project
print("Welcome to my computer quiz!")
playing = input('Do you want to play? ')
if playing.lower() != "yes": 
    quit()

print("Okay! Let's play :)")
score = 0 


# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit": 
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

# Question 2 
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit": 
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory": 
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

# Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply": 
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

print('You got ' + str(score) + " questions correct!")