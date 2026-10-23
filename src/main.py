import random
from utils.valid_input import valid_input
from utils.hint import hint
from utils.score import score

def main():
    my_score = score(100)
    random_number = random.randint(1, 100)
    while True:
        user_number = valid_input(1, 100)
        if not user_number:
            break
        
        if hint(user_number, random_number):
            print(f"your score is {my_score.result()}")
            break

        else:
            my_score.decrease_score() 


if __name__ == "__main__":
    main()
