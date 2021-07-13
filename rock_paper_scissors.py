import random
choice_list = ['rock', 'paper', 'scissors']
player_choice = input('Lets play rock, paper, scissors shoot! Which one do you choose? ')
random_choice = random.choice(choice_list)

if player_choice == 'rock':
    print('My choice was : ', random_choice)
    if random_choice == 'rock':
        print('Wow that was a draw!')
    elif random_choice == 'paper':
        print('Haha! I win! That was a fun game!')
    elif random_choice == 'scissors':
        print('Aww you beat me. Good game though')
else:
    if player_choice == 'paper':
        print('My choice was : ', random_choice)
        if random_choice == 'rock':
            print('Aww you beat me. Good game though')
        elif random_choice == 'paper':
            print('Wow that was a draw!')
        elif random_choice == 'scissors':
            print('Haha! I win! That was a fun game!')
    else:

        if player_choice == 'scissors':
            print('My choice was : ', random_choice)
            if random_choice == 'rock':
                print('Haha! I win! That was a fun game!')
            elif random_choice == 'paper':
                print('Aww you beat me. Good game though')
            elif random_choice == 'scissors':
                print('Wow that was a draw!')


        else:
            print('Oh I\'m sorry I didn\'t understand that!')
