"""
Generate a database from param inputs

Copyright 2020 - Steffan Jensen
Do NOT remove this copyright
Contact:
    Github: http://github.com/steffanjensen
"""
import sys
import os
import MySQLdb
sys.path.append(os.path.join(sys.path[0], "./webcreator/"))
from scraper import scraper
from config import db_host, db_password, db_username, db_name
webscraper = scraper.Scraper()

class Database(object):

    def __init__(self):
        # Test if it works
        self.host = db_host
        self.username = db_username
        self.passwd = db_password
        self.db_name = db_name

    def connect_to_db(self):
        db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        return db

    def create_profile(self, user):
        try:
            db = MySQLdb.connect(host=self.host, user=self.username, passwd=self.passwd, db=self.db_name)
            user_id = scraper.bot.get_user_id_from_username(user)
            ig_url = "http://www.instagram.com/@" + user
            user_info = scraper.bot.get_user_info(user_id)
            try:
                full_name = user_info["full_name"]
            except:
                full_name = None
            if full_name is None:
                full_name = ""
            print(user_info)
            profile_pic_url = user_info["profile_pic_url"]
            followers_count = user_info["follower_count"]
            following_count = user_info["following_count"]
            try:
                city = user_info["city_name"]
            except:
                city = None
            if city is None:
                city = ""
#            profile_pic_url = str(profile_pic_url)
#            profile_pic_url = profile_pic_url.split("?_nc")
#            profile_pic_url = profile_pic_url[0]
#            print(profile_pic_url)
#            db = self.db
            cur = db.cursor()
            isert = cur.execute("""INSERT INTO Models (user_id, username, full_name,
                                tiktok_url, instagram_profile, profile_pic_url,
                                ig_followers, ig_following, city) VALUES('"""+user_id+"""','"""+user+"""',
                                '"""+str(full_name)+"""', 'tiktok_url', '
                                """+str(ig_url)+"""', '"""+str(profile_pic_url)+"""',
                                '"""+str(followers_count)+"""',
                                '"""+str(following_count)+"""', '"""+str(city)+
                                """')""")
            print(isert)
            db.commit()
            db.close()
        except Exception as e:
            print(e)

    def post_video(self, user, path, likes):
        db = MySQLdb.connect(host=self.host, user=self.username, passwd=self.passwd, db=self.db_name)
        cur = db.cursor()
        user_id = scraper.bot.get_user_id_from_username(user)
        user = str(user)
        photo_url = str(path)
        likes = str(likes)
        isert = cur.execute("""INSERT INTO Videos (user_id, username, video_url,
                            likes) VALUES('"""+user_id+"""', '"""+user+"""',
                            '"""+photo_url+"""', '"""+likes+"""')""")
#        isert = cur.execute("""UPDATE Photos set ig_videos = '"""+path+"""' WHERE username = '"""+user+"""'""")
        db.commit()
#        time.sleep(5)
        print(isert)
        db.close()

        pass

    def post_photo(self, user, path, likes):
        try:
            db = MySQLdb.connect(host=self.host, user=self.username, passwd=self.passwd, db=self.db_name)
            cur = db.cursor()
            user_id = scraper.bot.get_user_id_from_username(user)
            user = str(user)
            photo_url = str(path)
            likes = str(likes)
            isert = cur.execute("""INSERT INTO Photos (user_id, username, photo_url,
                                likes) VALUES('"""+user_id+"""', '"""+user+"""',
                                '"""+photo_url+"""', '"""+likes+"""')""")
#            isert = cur.execute("""UPDATE Photos set ig_videos = '"""+path+"""' WHERE username = '"""+user+"""'""")
            db.commit()
#            time.sleep(5)
            print(isert)
            db.close()
        except Exception as e:
            print(e)

    def connect_to_db(self):
        db = MySQLdb.connect(host=self.host, user=self.username, passwd=self.passwd, db=self.db_name)
        cur = db.cursor()
        return cur

    def get_profile_pic(self, user):
        db_connect = self.connect_to_db()
        isert = db_connect.execute("""SELECT FROM * in Models""")
        print(isert)
        db_connect.close()

    def get_all_profile_pic(self):
        db_connect = self.connect_to_db()
        isert = db_connect.execute("""SELECT FROM * in Models""")
        print(isert)
        db_connect.close()

