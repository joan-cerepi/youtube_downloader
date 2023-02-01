from menu import option_menu
import sys

# Handle ModuleNotFoundError messages.
try:
    from pytube import YouTube, Playlist
except ModuleNotFoundError:
    print('Please install the required dependencies before running this program.')
    sys.exit(0)

# If pyfiglet is not found, print out banner in regular text.
try:
    import pyfiglet
    banner = pyfiglet.figlet_format('Youtube Video Downloader', font="slant")
    print(banner, end='\n\n')
except ModuleNotFoundError:
    print('Youtube Video Downloader', end='\n\n')
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

user_choice = option_menu()
url = input('Enter your video url: ')


def url_checker(url):
    '''Make sure the entered url is valid. If it is return it.'''
    try:
        YouTube(url)
    except:
        print('\nInvalid url. Try again!')
        sys.exit(0)
    return url


def download_video(url):
    '''Download a single video and return its title.'''
    video = YouTube(url)
    video.streams.get_highest_resolution().download('Videos/')
    return video.title


def main():
    global url
    global user_choice

    match user_choice:
        case 1:
            url = url_checker(url) # checks url and returns it
            title = download_video(url)
            print(f"' {title} ' finished downloading.")


if __name__ == '__main__':
    main()