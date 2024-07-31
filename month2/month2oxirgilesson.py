import os.path
import random
import json


def save_data_to_file(user_guess, comp_guess, winner, text):
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as file:
            json.dump({}, file, indent=4)

    with open('data.json', 'r') as file:
        all_data = json.load(file)
        game_id = 1
        if len(all_data) != 0:
            game_id = str(int(list(all_data.keys())[-1]) + 1)
        all_data[game_id] = {
            'user_guess': user_guess,
            'comp_guess': comp_guess,
            'winner': winner,
            'text': text
        }
        with open('data.json', 'w') as file:
            json.dump(all_data, file, indent=4)


def get_computer_guess():
    items = ["rock", "paper", "scissors"]
    return random.choice(items)


def get_user_guess():
    items = ["rock", "paper", "scissors"]
    user_input = input("Enter your choose (rock, paper, scissors): ")
    if user_input in items:
        return user_input
    else:
        print("Wrong input !")
        get_user_guess()


def find_winner(user_guess, comp_guess):
    if user_guess == comp_guess:
        save_data_to_file(user_guess, comp_guess, 'tie', 'Tie !')
        return "Tie !"
    elif (user_guess == "rock" and comp_guess == "scissors") or \
            (user_guess == "paper" and comp_guess == "rock") or \
            (user_guess == "scissors" and comp_guess == "paper"):
        save_data_to_file(user_guess, comp_guess, 'you', 'You won !')
        return "You win!"
    else:
        save_data_to_file(user_guess, comp_guess, 'comp', 'You lose !')
        return "You lose!"


def show_all_results():
    if not os.path.exists('data.json'):
        print("You do not have any results")
        return show_menu()

    with open('data.json', 'r') as file:
        all_data = json.load(file)
        for game_id, result in all_data.items():
            print(
                f"Game: {game_id}\tYou: {result['user_guess']}\tComp: {result['comp_guess']}\tResult: {result['text']}")
    return show_menu()


def get_statistics():
    if not os.path.exists('data.json'):
        print("You do not have any results")
        return show_menu()

    user = 0
    comp = 0
    tie = 0

    with open('data.json', 'r') as file:
        all_data = json.load(file)
        for game_id, result in all_data.items():
            if result['winner'] == 'you':
                user += 1
            elif result['winner'] == 'comp':
                comp += 1
            else:
                tie += 1
    print(f"You won: {user}\nComp won: {comp}\nTies: {tie}")
    return show_menu()


def play_game():
    user_guess = get_user_guess()
    comp_guess = get_computer_guess()
    result = find_winner(user_guess, comp_guess)
    print(result)
    return show_menu()


def show_menu():
    text = """
    1: Play game:
    2. Show all results:
    3: Who won more:
    4. Exit
    """
    print(text)
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        play_game()
    elif user_input == 2:
        show_all_results()
    elif user_input == 3:
        get_statistics()

    else:
        print("Good bye !")
        return


if __name__ == "__main__":
    show_menu()
