#oxirgi hw

import json
import random

results_file = "results.json"

def save_results(results):
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

def load_results():
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def random_number_game():
    computer_guess = random.randint(1, 10)
    attempts = 3
    user_guesses = []
    
    while attempts > 0:
        user_guess = int(input(f"son kiriting ( sizda {attempts}  ta imkoniyat bor): "))
        user_guesses.append(user_guess)
        
        if user_guess == computer_guess:
            print("Siz yutdingiz!")
            return {"Computer Guess": computer_guess, "User Guesses": user_guesses, "G'olib": "User"}
        else:
            print("Notogri.")
            attempts -= 1
            
    print(f"Siz yutqazdingiz. Kompyuter yutdi {computer_guess}.")
    return {"Computer Guess": computer_guess, "User Guesses": user_guesses, "G'olib": "Computer"}

def show_all_results():
    results = load_results()
    for i, result in enumerate(results, start=1):
        computer_guess = result["Computer Guess"]
        user_guesses = ", ".join(map(str, result["User Guesses"]))
        winner = result["G'olib"]
        print(f"Game {i}: Computer Guess {computer_guess} | User Guesses {user_guesses} | {winner} yutdi")

def who_won_more():
    results = load_results()
    user_wins = sum(1 for result in results if result["G'olib"] == "User")
    computer_wins = sum(1 for result in results if result["G'olib"] == "Computer")
    
    if user_wins > computer_wins:
        print(f"User koproq yutdi ({user_wins} ga qarshi {computer_wins})")
    elif computer_wins > user_wins:
        print(f"Computer koproq yutdi ({computer_wins} ga qarshi {user_wins})")
    else:
        print("durrang!")

def main():
    results = load_results()

    while True:
        print("menu:")
        print("1: tahminiy son ")
        print("2: barcha natijalar")
        print("3: koproq yutgan odam")
        print("4: exit")
        
        choice = input("shulardan birini kiriting (1/2/3/4): ")
        
        if choice == '1':
            result = random_number_game()
            results.append(result)
            save_results(results)
        elif choice == '2':
            show_all_results()
        elif choice == '3':
            who_won_more()
        elif choice == '4':
            print("exit.")
            break
        else:
            print("notog'ri raqam. iltimos shulardan birini tanlang 1, 2, 3 yoki 4.")

if __name__ == "__main__":
    main()

