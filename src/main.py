from src.utils.number_validate import input_validator
from src.game_logic.check_num import check_number
from src.game_logic.generate_rand import generate_num

def main():
    number_to_guess = generate_num(1,100)
    score = 100
    while True:
        guess = input_validator(1,100)
        if guess == number_to_guess:
            print(f"Congratulations! Your final score is: {score}")
            break
        else:
            check_number(number_to_guess, guess)
            score -= 10


if __name__ == '__main__':
    main()