import pyfiglet


def banner():
    '''Print out a title banner at the top of the output.'''
    try:
        import pyfiglet
        banner = pyfiglet.figlet_format('Youtube Video Downloader', font='slant')
        print(banner, end='\n\n')
    except ModuleNotFoundError:
        print('Youtube Video Downloader', end='\n\n')