#!/usr/bin/env python
# coding: utf-8

# ### Number Guessing Game
# #### Features include:
# ##### Computer picks a number
# ##### user keeps guessing
# ##### tell them "too high or too low"
# ##### stop when correct

# In[9]:


import random

number = random.randint(1, 10)
attempts = 0

print("Guess the number between 1 and 10")

while True:
    user_input = int(input("Enter your guess: "))
    attempts += 1

    if user_input < number:
        print("Number too low, try again")

    elif user_input > number:
        print("Number too high, try again")

    else:
        print("Correct!")
        break

print(f"You got the right number in {attempts} attempts")


# In[ ]:




