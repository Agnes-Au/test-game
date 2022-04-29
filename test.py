import time

# stats
mental = 0
popular = 0
relationships = 0

user_choice = ''


# Define 'Situation' class
class Situation:
    def __init__(self, statement, choice):
        # Shows what happened in the story
        self.statement = statement
        # List; shows the available choices and their consequences
        self.choice = choice

    # Define play_game function - Shows the situation, allows player to choose their fate
    def play_game(self):
        global mental
        global popular
        global relationships
        global user_choice
        # If the player's mental health is >= -4,
        # in other words if the player does not fulfill the requirement of a bad ending,
        # show the situation
        if mental >= -4:
            print(self.statement)
            time.sleep(2)
            print('Your choices are:')
            time.sleep(1)
            print('1 ' + self.choice[0][0])
            time.sleep(0.5)
            print('or')
            print('2 ' + self.choice[1][0])
            time.sleep(1)
            # enable the choosing
            choosing = True
        else:
            # if the player fulfills the requirement of a bad ending, disable the choosing
            choosing = False
        while choosing:
            # user input for choice
            user_choice = input('What do you choose, 1 or 2? ')
            print('------------')
            # if the user chooses the 1st option
            if user_choice == '1':
                # disable choosing
                choosing = False
                # reiterate player's choice
                print('You chose to ' + self.choice[0][0].lower() + '.')
                # tweak player's stats according to situation and choice
                mental += self.choice[0][1][0]
                popular += self.choice[0][1][1]
                relationships += self.choice[0][1][2]
                # print the text consequences of the choice
                time.sleep(2)
                print(self.choice[0][1][3])
                user_choice = ''
            # else if the user chooses the 2nd option
            elif user_choice == '2':
                # disable choosing
                choosing = False
                # reiterate player's choice
                print('You chose to ' + self.choice[1][0].lower() + '.')
                # tweak player's stats according to situation and choice
                mental += self.choice[1][1][0]
                popular += self.choice[1][1][1]
                relationships += self.choice[1][1][2]
                # print the text consequences of the choice
                time.sleep(2)
                print(self.choice[1][1][3])
                user_choice = ''
            else:
                # if the player input something that is not 1 or 2, tell them it's not valid
                print('That\'s not a valid option!')
        time.sleep(6)


# define a function that shows the player's stats
def show_stats():
    time.sleep(2)
    print('Your stats are: \nMental health: ' + str(mental))
    time.sleep(1)
    print('Popularity: ' + str(popular))
    time.sleep(1)
    print('Relationships: ' + str(relationships))


# Define the 'Story' class
class Story:
    def __init__(self, situations, good_ending, game_over):
        # Contains the situations that belong to this story
        self.situations = situations
        # Boolean; shows if the player has the requirements for the good ending of the story
        self.good_ending = good_ending
        # List of strings; shows the different possible 'game over' messages
        self.game_over = game_over

    # define a function that resets necessary game values
    def reset_values(self):
        global mental
        global popular
        global relationships
        mental = 0
        popular = 0
        relationships = 0
        self.good_ending = True

    # define a function that checks player stats to determine
    # whether the player satisfies the requirement for a good/bad ending
    def check_values(self):
        if mental <= -4:
            self.good_ending = False
        else:
            self.good_ending = True


# available situations
situation1 = Situation(
    'My friend Flora is going to crank-text her nemesis Mikey as Mikey\'s crush Donald just because they had some '
    'misunderstandings in the past.\nThat’s really mean and we may even get in trouble! Should I stop her?',
    [['Go along with it', [-1, +1, -1,
                           'You went along with Flora\'s plans.']],
     ['Tell Flora to stop', [+1, -1, 0,
                             'You tried to stop Flora, but she refused to listen to you.']]])
situation2 = Situation(
    'Impersonating Donald, Flora flirted with Mikey through text and even...\nwait...is Flora asking for '
    'Mikey’s...nudes?\nThis is going way too far, what should I do?',
    [['Go along with it', [-1, +1, -1,
                           'You went along with it, even though you feel like something is really wrong.']],
     ['Tell Flora to stop', [+1, -1, 0,
                             'Flora got angry at you for your warnings. Your friendship was damaged, and you decide '
                             'not to partake in this anymore.']]])

situation3 = Situation(
    'Every day, Flora runs to the park to impersonate Donald.\nAt school, I see Mikey looking at '
    'Donald at school,\ntwisting her hair at him like he was actually texting her. \nI think Mikey\'s thoroughly '
    'embarrassed and\nFlora\'s really done something wrong...\nshould I just report her?',
    [['Ignore it', [-1, +1, -1,
                    'You ignored what Flora was doing. You think that improved your friendship a little bit.']],
     ['Report Flora to the teacher', [+1, -1, 0,
                                      'You reported Flora\'s actions to the teacher. She punished her and had a good '
                                      'talk with Mikey. You doubt your friendship with Flora can be recovered, '
                                      'but you\'re glad you did the right thing.']]])

# available stories
story1 = Story([situation1, situation2, situation3], True,
               ['Game over! Congratulations, you figured out how to face bullying.',
                'Game over! You failed to face bullying.'])

# playing is not true by default, the good ending is enabled by default
playing = False
story1.good_ending = True
# reset stats
story1.reset_values()
# Ask the player if they would like to play the game
play = input('Play game? (Y) ')
# If the player inputs y, set playing to true
if play.upper() == 'Y':
    playing = True
# Game loop
while playing:
    print('------------')
    # For each situation in story1, play the game
    for situation in story1.situations:
        # Change the good_ending variable according to the player's stats
        story1.check_values()
        # If the player satisfies the requirements for a good ending, show the next situation
        if story1.good_ending:
            situation.play_game()
            print('------------')
        # If the player satisfies the requirements for a bad ending, show them the bad ending game over
        else:
            print('------------')
            print(story1.game_over[1])
    # If the player satisfies the requirement for a good ending and there are no more situations,
    # show the good ending game over
    if story1.good_ending:
        print(story1.game_over[0])
    # Show stats and reset values when there are no more situations
    show_stats()
    story1.reset_values()
    # Play again?
    again = input('Input Y to play again and anything else to quit: ')
    # If the player inputs y, set playing to true
    if again.upper() == 'Y':
        playing = True
    else:
        # Otherwise set playing to false
        playing = False
