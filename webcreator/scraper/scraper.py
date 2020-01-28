"""
This scraper is created by steffan jensen.

Copyright 2020 - All rights reserved
"""
import time
import shutil
#from tiktokapi import downloader
import json
import re
from tqdm import tqdm

import sys
import os
sys.path.append(os.path.join(sys.path[0], "../"))
from instabotai import ai
from instabot import Bot
from config import ig_username, ig_password

bot = Bot()

bot.api.login(username=ig_username, password=ig_password, is_threaded=True, use_cookie=True)


class Scraper(object):
    """ Many different social media scrapers """
    def __init__(self):
        all_profiles = []
        user_videos_with_face = []
        self.all_profiles = all_profiles

    def ig_photo_and_video_scraper(user):
        """ This scraped images and videos and post them """
        try:
            os.system("instagram-scraper " + "'"+user+"'" + " --media-metadata --media-types none --maximum 200 --retry-forever")
            time.sleep(1)
            with open(user + "/" + user + ".json") as json_file:
                data = json.load(json_file)
                for p in tqdm(data['GraphImages']):
                    try:
                        display_url = p['display_url']
                        urls = p['urls']
                        is_video = p['is_video']
                        likes = p['edge_media_preview_like']['count']
                        likes = str(likes)
                        display_url = str(display_url)
                        urls = str(urls)
                        urls = urls.replace("['", "")
                        urls = urls.replace("']", "")
                        if is_video == True:
                            print("this is a video")
                            display_url = re.sub(r'(.*?)/', '', urls)
                            display_url = display_url.split("?")
                            display_url = display_url[0]
                            file_path = user + "/" + display_url
                            print(file_path)
                            try:
                                database.post_video(user, urls, likes)
                            except:
                                pass
                    except:
                        pass
    #
    #                    try:
    #                        detect = Ai.face_detection_video(file_path)
    #                    except:
    #                        pass
    #                    try:
    #                        if not detect:
    #                            print("no face detected")
    #                            shutil.os.remove(file_path)
    #                        elif detect:
    #                            print(user)
    #                            print(urls)
    #                            print(likes)
    #                            try:
    #                                database.post_video(user, urls, likes)
    #                            except Exception as e:
    #                                print(e)
    #                            shutil.os.remove(file_path)
    #                            print("face detected")
    #                    except:
    #                        pass

                    if is_video == False:
                        print("not a video")
                        display_url = re.sub(r'(.*?)/', '', display_url)
                        display_url = display_url.split("?")
                        display_url = display_url[0]
                        file_path = user + "/" + display_url
                        file_path = str(file_path)
                        print(file_path)
                        try:
                            database.post_photo(user, urls, likes)
                        except:
                            pass
    #                    try:
    #                        detect = Ai.face_detection_photo(file_path)
    #                    except:
    #                        pass
    #                    try:
    #                        if not detect:
    #                            print("no face detected")
    #                            shutil.os.remove(file_path)
    #                        elif detect:
    #                            print(user)
    #                            print(urls)
    #                            print(likes)
    #                            try:
    #                                database.post_photo(user, urls, likes)
    #                            except Exception as e:
    #                                print(e)
    #                            shutil.os.remove(file_path)
    #                            print("face detected")
    #
    #                    except:
    #                        pass
    #                    print(is_video)
    #                    print(likes)
        except Exception as e:
            print(e)

    def download_media(self, url):
         response = requests.get(url, allow_redirects=True)
         open('1.jpg', 'w+').write(response.content)
         url = str(url)
         url = url.split("/")
         url = url.split("/")
         url = url.split("/")
         return url

    def scrape_user_id(username):
        """ Get user_id from username """
        user_id = bot.get_user_id_from_username(username)
        return user_id


#    def tiktok_videos_scraper(self, user):
#        tiktok = downloader.Downloader()
#        videos = tiktok.download_user_videos(user)
#        return videos

    def instagram_photos_scraper(self, user):
        """ Scrapes Instagram photos """
        medias = bot.get_total_user_medias(user)
        for media in medias:
            try:
                print(media)
                bot.download_photo(media, folder=user)
                path_file = "./" + user + "/" + user + "_" + str(media) + ".jpg"
                ai = Ai()
                detect = ai.face_detection_photo(path_file)
                print(detect)
                if not detect:
                    print("no face detected")
                    shutil.os.remove(path_file)
                elif detect:
                    print("face detected")
            except Exception as e:
                print(e)

    def instagram_videos_scraper(self, user):
        """ Scrapes instagram videos """
        user_id = bot.get_user_id_from_username(user)
        time.sleep(1)
        user_medias = bot.get_total_user_medias(user_id)
        for media_id in user_medias:
            bot.api.media_info(media_id)
            json = bot.api.last_json
            media_type = json["items"][0]["media_type"]
            if media_type == 2:
                print("Downloading Video")
                bot.download_video(media_id, folder=user)
                self.all_profiles.append(str(media_id))
                print(self.all_profiles)
            else:
                print("Not a video")
        return self.all_profiles

    def get_user_profile_picture(self, user):
        pass

    def get_ig_followers_count(self, user_id):
        ''' Get user_id followers count '''
        user_info = bot.get_user_info(user_id)
        followers = user_info["follower_count"]
        return followers

