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


def url_checker(url, type):
    '''
    Make sure the entered url is valid. If it is return it.
    url: Video or Playlist url.
    type: type of url ('video', 'playlist')
    '''
    print('hello')
    if type == 'video':
        try:
            YouTube(url)
        except:
            print('\nInvalid url. Try again!')
            sys.exit(0)
    elif type == 'playlist':
        try:
            Playlist(url)
        except:
            print('\nInvalid url. Try again!')
            sys.exit(0)
    return url


def download_video(url):
    '''Download a single video and return its title.'''
    video = YouTube(url)
    video.streams.get_highest_resolution().download('Videos/')
    return video.title


def download_playlist(url):
    '''Download an entire playlist '''
    playlist = Playlist(url)

    for video in playlist.videos:
        print(f"' {video.title} ' started downloading.")
        video.streams.get_highest_resolution().download('Playlists/')
        print(f"' {video.title} ' finished downloading.")
    return playlist.title


user_choice = option_menu()
url = input('Enter your url: ')


def main():
    global url
    global user_choice

    match user_choice:
        case 1:
            url = url_checker(url, 'video') # Checks url and returns it.
            title = download_video(url)
            print(f"' {title} ' finished downloading.")
        case 2:
            url = url_checker(url, 'playlist')
            download_playlist(url)
            


if __name__ == '__main__':
    main()