from art import logo
from art import vs
from game_data import data
import random

print(logo)

random_profiles = random.sample(data, 2)

score = 0
game_over = False


def get_follower_count(profile):
    return profile['follower_count']

def game():
    global score  
    global game_over
    while not game_over:
      compare_A = f"Compare A: {random_profiles[0]['name']}, a {random_profiles[0]['description']}, from {random_profiles[0]['country']}"
      compare_B = f"Compare B: {random_profiles[1]['name']}, a {random_profiles[1]['description']}, from {random_profiles[1]['country']}"
  
      print(compare_A)
      print(vs)
      print(compare_B)
  
      guess = input('Who has more followers? A or B (type "stop" to end the game): ')
  
      if guess.lower() == 'stop':
        game_over = True
  
      if guess.upper() == 'A':
          if get_follower_count(random_profiles[0]) > get_follower_count(random_profiles[1]):
              score += 1
              print('You are right!')
          else:
              print(f"You are wrong! {random_profiles[0]['name']} has {random_profiles[0]['follower_count']} mi followers, and {random_profiles[1]['name']} has {random_profiles[1]['follower_count']} mi followers.")
              game_over = True
      elif guess.upper() == 'B':
          if get_follower_count(random_profiles[1]) > get_follower_count(random_profiles[0]):
              score += 1
              print('You are right!')
          else:
              print(f"You are wrong! {random_profiles[1]['name']} has {random_profiles[1]['follower_count']} mi followers, and {random_profiles[0]['name']} has {random_profiles[0]['follower_count']} mi followers. Game over.")
              game_over = True
      else:
          print('Invalid input. Please enter A or B.')
  
      
      random_profiles[0], random_profiles[1] = random.sample(data, 2)

game()
print(f'Your current score is: {score}')



