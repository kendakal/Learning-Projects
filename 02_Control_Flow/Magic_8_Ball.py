'''
Project: Magic 8-Ball

The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
'''


import random

name = "Matthew"
question = "Will I win the lottery?"
answer = ""
random_number = random.randint(1,12) #random function to generate a random number between 1 and 9
print(random_number)

if random_number == 1:
  answer = "Yes - defintely"
elif random_number == 2:
  answer = "It is decidely so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Nah mate"
elif random_number == 11:
  answer = "Potentially"
elif random_number == 12:
  answer = "Absolutely not"
else:
  answer = "Error"

if name == "":
  print("Question: ", question)
elif question == "":
  print("What is the question?")
else:
  print(name, "asks: " + question)
  print("Magic 8-Ball's answer: ", answer)