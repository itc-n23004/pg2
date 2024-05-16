import random, sys

print('ROCK, PAPER, SCISSORS')
wins, losses, ties = 0, 0, 0

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    player_move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
    if player_move == 'q':
        sys.exit()
    if player_move not in ('r', 'p', 's'):
        print('Type one of r, p, s, or q.')
        continue

    print(f'{("ROCK" if player_move == "r" else "PAPER" if player_move == "p" else "SCISSORS")} versus...')
    computer_move = random.choice(['r', 'p', 's'])

    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1

