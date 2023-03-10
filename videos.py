from pytube import YouTube, Playlist
from pytube.exceptions import *
import progressbar
import sys


class Video:
    '''Create a youtube video class.'''
    def __init__(self, url: str, path: str):
        '''Initialize url and path to the Video class.'''
        self.url = url
        self.path = path


    def get_url(self):
        '''Access and return your video url.'''
        return self.url


    def download_video(self):
        '''Download Video into the provided path.'''
        try:
            yt_video = YouTube(self.url)
        except VideoUnavailable:
            print('Video is not available.')
            sys.exit(0)
        except RegexMatchError:
            print()
            print('The link does not seem to be quite right.')
            print('Correct the link and run the code again.')
            sys.exit(0)
        YouTube(self.url).streams.get_highest_resolution().download(self.path)


    def download_playlist(self):
        '''Download Playlist into the provided path.'''
        playlist = Playlist(self.url)
        try:
            for video in playlist.videos:
                try:
                    video.streams.get_highest_resolution().download(self.path)
                except VideoUnavailable:
                    print('Video is unavailable. Skipping...')
        except KeyError:
            print()
            print('Please check your link and try again.')
            sys.exit(0)