import random

# Play number guessing game with Computer
# Computer generates random no between 1 and 5
# User asked to pick a number between 1 and 5
# If right choice selected game ends
# If not, user is asked to pick again based on whether first time was too high or low
# After second chance game ends with a win or loss 

num = random.randint(1, 5)
user = int(input('Pick a number between 1 and 5: '))

if user == num:
  print('Well done')
elif user > num:
  print('Too high')
  user = int(input('Pick another number: '))
  if user == num:
    print('You win')
  else:
    print('You lose')
else:
  print('Too low')
  user = int(input('Try again: '))
  if user == num:
    print('You win')
  else:
    print('You lose')
print(f' Computer picked {num}')