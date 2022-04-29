# import time
#
# # stats
# mental = 0
# popular = 0
# relationships = 0
#
# user_choice = ''
#
#
# # Define 'Situation' class
# class Situation:
#     def __init__(self, statement, choice):
#         # Shows what happened in the story
#         self.statement = statement
#         # List; shows the available choices and their consequences
#         self.choice = choice
#
#     # Define play_game function - Shows the situation, allows player to choose their fate
#     def play_game(self):
#         global mental
#         global popular
#         global relationships
#         global user_choice
#         # If the player's mental health is >= -4,
#         # in other words if the player does not fulfill the requirement of a bad ending,
#         # show the situation
#         if mental >= -4:
#             print(self.statement)
#             time.sleep(2)
#             print('Your choices are:')
#             time.sleep(1)
#             print('1 ' + self.choice[0][0])
#             time.sleep(0.5)
#             print('or')
#             print('2 ' + self.choice[1][0])
#             time.sleep(1)
#             # enable the choosing
#             choosing = True
#         else:
#             # if the player fulfills the requirement of a bad ending, disable the choosing
#             choosing = False
#         while choosing:
#             # user input for choice
#             user_choice = input('What do you choose, 1 or 2? ')
#             print('------------')
#             # if the user chooses the 1st option
#             if user_choice == '1':
#                 # disable choosing
#                 choosing = False
#                 # reiterate player's choice
#                 print('You chose to ' + self.choice[0][0].lower() + '.')
#                 # tweak player's stats according to situation and choice
#                 mental += self.choice[0][1][0]
#                 popular += self.choice[0][1][1]
#                 relationships += self.choice[0][1][2]
#                 # print the text consequences of the choice
#                 time.sleep(2)
#                 print(self.choice[0][1][3])
#                 user_choice = ''
#             # else if the user chooses the 2nd option
#             elif user_choice == '2':
#                 # disable choosing
#                 choosing = False
#                 # reiterate player's choice
#                 print('You chose to ' + self.choice[1][0].lower() + '.')
#                 # tweak player's stats according to situation and choice
#                 mental += self.choice[1][1][0]
#                 popular += self.choice[1][1][1]
#                 relationships += self.choice[1][1][2]
#                 # print the text consequences of the choice
#                 time.sleep(2)
#                 print(self.choice[1][1][3])
#                 user_choice = ''
#             else:
#                 # if the player input something that is not 1 or 2, tell them it's not valid
#                 print('That\'s not a valid option!')
#         time.sleep(6)
#
#
# # define a function that shows the player's stats
# def show_stats():
#     time.sleep(2)
#     print('Your stats are: \nMental health: ' + str(mental))
#     time.sleep(1)
#     print('Popularity: ' + str(popular))
#     time.sleep(1)
#     print('Relationships: ' + str(relationships))
#
#
# # Define the 'Story' class
# class Story:
#     def __init__(self, situations, good_ending, game_over):
#         # Contains the situations that belong to this story
#         self.situations = situations
#         # Boolean; shows if the player has the requirements for the good ending of the story
#         self.good_ending = good_ending
#         # List of strings; shows the different possible 'game over' messages
#         self.game_over = game_over
#
#     # define a function that resets necessary game values
#     def reset_values(self):
#         global mental
#         global popular
#         global relationships
#         mental = 0
#         popular = 0
#         relationships = 0
#         self.good_ending = True
#
#     # define a function that checks player stats to determine
#     # whether the player satisfies the requirement for a good/bad ending
#     def check_values(self):
#         if mental <= -4:
#             self.good_ending = False
#         else:
#             self.good_ending = True
