import sys

# Handle ModuleNotFoundError messages.
try:
    import pytube
except ModuleNotFoundError:
    print('Please install the required dependencies before running this program.')
    sys.exit(0)

try:
    import pyfiglet
    banner = pyfiglet.figlet_format('Youtube Video Downloader', font="slant")
    print(banner, end='\n\n')
except ModuleNotFoundError:
    print('Youtube Video Downloader', end='\n\n')


def main():
    pass


if __name__ == '__main__':
    main()