from banner import banner
from videos import Video
import sys


def main():
    '''Main body of the program.'''
    # Print out a title banner at the top of the program output.
    banner()
    user_url = input('Enter your url: ').strip()
    path = input('Enter path to download your videos to: ').strip()
    url_type = 'video' # input('Enter the url type (video or playlist): ').strip().lower()
    if url_type in ['video', 'playlist']:
        if url_type == 'video':
            user_video = Video(user_url, path)
            user_video.download_video()

        if url_type == 'playlist':
            user_playlist = Video(user_url, path)
            user_playlist.download_playlist()
    else:
        print('Invalid url type. Please try again.')
        sys.exit(0)


if __name__ == '__main__':
    main()