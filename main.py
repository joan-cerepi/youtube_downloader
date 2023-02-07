from banner import banner
from videos import Video


def main():
    '''Main body of the program.'''
    # Print out a title banner at the top of the program output.
    banner()
    user_url = input('Enter your url: ').strip()
    path = input('Enter path to download your videos to: ').strip()
    url_type = 'video'
    if url_type == 'video':
        user_video = Video(user_url, path)
        user_video.download()

    if url_type == 'playlist':
        user_playlist = Video(user_url, path)
        user_playlist.download_playlist()


if __name__ == '__main__':
    main()