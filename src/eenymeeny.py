# Eeny, Meeny, Miny, Moe, by Al Sweigart al@inventwithpython.com
# More info at https://en.wikipedia.org/wiki/Eeny,_meeny,_miny,_moe
# More info at https://en.wikipedia.org/wiki/Josephus_problem

import random, time, sys

SCREEN_WIDTH = 60
RHYME = ['EENY', 'MEENY', 'MINY', 'MOE', 'CATCH A', 'TIGER', 'BY THE', 'TOE', 'IF IT', 'HOLLERS', 'LET IT', 'GO', 'EENY', 'MEENY', 'MINY', 'MOE']
NAMES = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 'George', 'Kenneth', 'Steven', 'Edward', 'Brian', 'Ronald', 'Anthony', 'Kevin', 'Jason', 'Matthew', 'Gary', 'Timothy', 'Jose', 'Larry', 'Jeffrey', 'Frank', 'Scott', 'Eric', 'Stephen', 'Andrew', 'Raymond', 'Gregory', 'Joshua', 'Jerry', 'Dennis', 'Walter', 'Patrick', 'Peter', 'Harold', 'Douglas', 'Henry', 'Carl', 'Arthur', 'Ryan', 'Roger', 'Mary', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Jennifer', 'Maria', 'Susan', 'Margaret', 'Dorothy', 'Lisa', 'Nancy', 'Karen', 'Betty', 'Helen', 'Sandra', 'Donna', 'Carol', 'Ruth', 'Sharon', 'Michelle', 'Laura', 'Sarah', 'Kimberly', 'Deborah', 'Jessica', 'Shirley', 'Cynthia', 'Angela', 'Melissa', 'Brenda', 'Amy', 'Anna', 'Rebecca', 'Virginia', 'Kathleen', 'Pamela', 'Martha', 'Debra', 'Amanda', 'Stephanie', 'Carolyn', 'Christine', 'Marie', 'Janet', 'Catherine', 'Frances', 'Ann', 'Joyce', 'Diane']
random.shuffle(NAMES)

print('Eeny, Meeny, Miny, Moe')
print()

# Get the players' names:
playerNames = []
while True:
    print('Enter a player\'s name, or nothing when done:')
    playerName = input().upper()
    if playerName != '': # Player can enter anything except a blank name.
        playerNames.append(playerName)
    else:
        break

# Get the total number of participants:
while True:
    print('How many participants total (2-' + str(len(NAMES) + len(playerNames)) + '):')
    try:
        numParticipants = int(input())
    except ValueError:
        continue # Player entered non-integer; ask again.
    if 2 <= numParticipants < len(NAMES) + len(playerNames):
        break

# Get the position of the player:
participants = NAMES[:numParticipants - len(playerNames)] # Get the required number of names.
for playerName in playerNames:
    while True:
        print('Where does ' + playerName + ' go? (1-' + str(len(participants) + 1) + '):')
        try:
            position = int(input())
        except ValueError:
            continue # Player entered non-integer; ask again.
        if 1 <= position <= len(participants) + 1:
            participants.insert(position - 1, playerName)
            break

# Start the elimination process:
while len(participants) > 1:
    # Figure out how many names to put on each row:
    rows = ['']
    for name in participants:
        if len(rows[-1]) + len(name) > SCREEN_WIDTH:
            # Start a new row:
            rows.append('')

        rows[-1] += name + ' '

    # Begin one round of elimination:
    for rhymeWordIndex, rhymeWord in enumerate(RHYME):
        currentPerson = participants[rhymeWordIndex % len(participants)]
        for row in rows:
            # Include a space at the end, so we don't match names with the
            # same prefix, i.e. 'Doug' and 'Douglas':
            if currentPerson + ' ' in row:
                print(' ' * row.index(currentPerson) + rhymeWord)
            else:
                print()
            print(row)
        print('\n')
        time.sleep(0.5)

    # Remove the eliminated person from the participants list:
    print(currentPerson.upper() + ' HAS BEEN ELIMINATED.')
    participants.remove(currentPerson)
    if currentPerson in playerNames:
        # If it's a player, remove them from playerNames:
        playerNames.remove(currentPerson)

    # If all players have been eliminated, end the game:
    if len(playerNames) == 0:
        print('ALL PLAYERS HAVE BEEN ELIMINATED.')
        print()
        print('Thanks for playing!')
        sys.exit()

    try:
        input('Press Enter to continue, or Ctrl-C to quit.')
    except KeyboardInterrupt:
        # Player pressed Ctrl-C, so end the game.
        sys.exit()

# Declare the winner:
print(participants[0] + ' IS THE WINNER!!!')
