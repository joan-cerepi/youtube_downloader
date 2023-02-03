from banner import banner
from videos import Video


def main():
    '''Make sure '''
    # Print out a title banner at the top of the program output.
    banner()
    user_url = input('Enter your url: ')
    path = input('Enter path to download your videos to: ')
    user_video = Video(user_url, path)
    user_video.download()


if __name__ == '__main__':
    main()