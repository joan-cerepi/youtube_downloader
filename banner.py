import pyfiglet


def banner():
    '''Print out a title banner at the top of the output.'''
    RED = '\u001b[31m'
    WHITE = '\u001b[37m'
    try:
        import pyfiglet
        banner = pyfiglet.figlet_format('Youtube Video Downloader', font='slant')
        print(f'{RED}{banner}{WHITE}', end='\n\n')
    except ModuleNotFoundError:
        print('Youtube Video Downloader', end='\n\n')