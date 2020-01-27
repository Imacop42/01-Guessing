import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 50

while not quit:
    random_number = random.randint(1,range)
    print("\n\nA chasm filled with lava lies before you, and a stone bridge stretches out across it.")
    print("A guard stands vigilant in front of the bridge.")
    number = input("\nGuard: 'Guess the correct number between 1 and {} and you may pass.' You: ".format(range))
    number = int(number)
    count = 1
    while number != random_number:
        print("Guard: 'That is not the correct number!'")
        if number > random_number:
            print("Guard: 'It would do you good to guess a lower number...'")
        else:
            print("Guard: 'Only fools would select such a small number...'")
        number = input("\nGuard: 'Once more! Guess a number!' You: ")
        number = int(number)
        count = count + 1
    print("\nGuard: 'That is correct... You have successfuly guessed my number...")
    if count <= 6:
        print("Guard: 'And in {} tries, no less! This is impressive!'".format(count))
    elif count == 7:
        print("Guard: 'It took you {} tries. That is satisfactory, but not impressive...'".format(count))
    elif count == 8:
        print("Guard: 'It took you {} tries. That is satisfactory, but not impressive...'".format(count))
    elif count == 9:
        print("Guard: 'It took you {} tries. That is satisfactory, but not impressive...'".format(count))
    elif count >= 10:
        print("Guard: 'It took you {} tries? That is not very good...".format(count))
    elif count == 1:
        print("Guard: 'You guessed it on your first try! that is astounding!'")
    print("Guard: 'You have guessed the number, thus you may now pass.'")
    play_again = input("\nCongratulations! You succesfully passed the guard! would you like to play again? ")
    play_again = play_again.lower()
    if play_again == "yes":
        quit = False
    else:
        quit = True


