def hint(user:int, system:int):
    if user == system:
        print(f'your guess is correct')
        return True
        
    elif user > system :
        print('Please decrease your guess')
        return False

    else :
        print('Please increase your guess')
        return False
     