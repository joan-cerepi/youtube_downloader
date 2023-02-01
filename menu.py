def option_menu():
    '''A list of all the available options for the Youtube Video Downloader.'''
    print('1. Download Youtube Video in highest resolution.')
    print('2. Download Youtube Video Playlist.')
    print()

    # Make sure to handle any possible invalid user input.
    while True:
        try:
            user_option = int(input('Please pick a number from the above menu: '))
            if user_option < 1 or user_option > 5:
                raise ValueError
            break
        except ValueError:
            print('Please try entering a valid numeric value.\n')
    return user_option