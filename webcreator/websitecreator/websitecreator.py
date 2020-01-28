import time
from scraper import scraper
from database import database

#bot = ai.Bot(do_logout=True)
#bot = ai.Bot()
#bot.api.login(username=ig_username, password=ig_password, is_threaded=True, use_cookie=True)
#time.sleep(2)
db = database.Database()

class webcreator(object):

    def __init__(self):
        pass

    def start(self, profile):
        db.create_profile(profile)
        scraper.Scraper.ig_photo_and_video_scraper(profile)

    def multi_user_poster(self, profiles):
        for profile in profiles:
            try:
                user_id = scraper.bot.get_user_id_from_username(profile)
                followers = scraper.bot.get_user_following(user_id)
                print(followers)
                for follower in followers:
#                    user_id = scraper.bot.get_user_id_from_username(follower)
#                    print(user_id)
                    print("test")
                    print(follower)
                    follow_count = scraper.Scraper().get_ig_followers_count(follower)
                    follow_count = int(follow_count)
                    time.sleep(2)
                    if follow_count > 500:
                        print("it's over 10.000")
                        print(str(follow_count))
                        user = scraper.bot.get_username_from_user_id(follower)
                        self.start(user)
                    else:
                        print("not over 5000")
                        print(str(follow_count))
            except Exception as e:
                    print(e)

