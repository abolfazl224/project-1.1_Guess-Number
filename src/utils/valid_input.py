def valid_input(start, end):
    while True:
        user_input = input("please enter a number(for ending enter 'q'):")
        if not user_input.isdigit():
            if user_input == 'q':
                print('Thank you for choose my game. Good By.')
                break
    
            else:
                print('please enter valid input')
                continue

        user_input = int(user_input)
        if (user_input < start) or (user_input > end):
            print(f'please enter a number between {start} and {end}')
            continue
        
        return user_input