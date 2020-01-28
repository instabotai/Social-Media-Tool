from . import api
from tqdm import tqdm

class Bot(object):

    def __init__(self):
        self.api = api.Api()

    def download_user_videos(self, username):
        ''' Download user videos without watermark '''
        x = 1
        videos = self.api.get_user_videos(username)

        for video in tqdm(videos):
            filename = username + str(x)
            print(str(video))
            video_urls = self.api.get_video_url(video)
            try:
                self.api.download_user_video(video_urls, filename)
                x = x + 1
            except Exception as e:
                print(e)

