from __future__ import unicode_literals
import time
from webcreator import 
#from ..mtcnn.mtcnn import MTCNN
#from ..mtcnn.mtcnn import MTCNN
import sys
import os
#sys.path.append(os.path.join(sys.path[0], "/home/steffan/devenv/webcreator/"))
sys.path.append(os.path.join(sys.path[0], "./webcreator/"))
# sys.path.append('..')   #path to directory that contains outdir
print(sys.path)
from mtcnn.mtcnn import MTCNN
import cv2
from ..instabotai import ai
import shutil
#from tiktokapi import downloader
import numpy as np
import json
import MySQLdb
import pdb
import re
from tqdm import tqdm
import tensorflow as tf
import multiprocessing
from multiprocessing import Process
import timeit

tf.config.threading.set_intra_op_parallelism_threads(24)


class Ai(object):
    def __init__(self):
        pass

    def face_detection_photo(self, path):

        start = time.time()
        path = str(path)
#        img = cv2.imread(path)
        img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
        scale_percent = 10  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        detector = MTCNN()
        detected = detector.detect_faces(img)
        end = time.time()
        print(f"Runtime of the program is {end - start}")
        return detected

    def face_detection_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        success, image = cap.read()
        count = 0
        frame = 0
        while success:
            for frame in range(1):
                try:
                    cv2.imwrite("frame%d.jpg" %
                                count, image)  # save frame as JPEG file
                    success, image = cap.read()
                    print('Read a new frame: ', success)
                    img_file = "frame" + str(count) + ".jpg"
                    img = cv2.cvtColor(cv2.imread(img_file), cv2.COLOR_BGR2RGB)
                    detector = MTCNN()
                    detected = detector.detect_faces(img)
                    shutil.os.remove(img_file)
                    count += 1
                    frame += 1
                except Exception as e:
                    print(e)

            return detected

    def ig_video_scraper_and_face_detector(self, username):
        scraper = Scraper()
        videos = scraper.instagram_videos_scraper(username)
        for video in videos:
            video_path = profiles + "/0_" + \
                profiles + "_" + str(video) + ".mp4"
            try:
                Ai.face_detection_video(video_path)
            except Exception as e:
                print(e)
                pass

    def tiktok_video_scraper_and_face_detector(self, username):
        scraper = Scraper()
        videos = scraper.tiktok_videos_scraper(username)
        for video in videos:
            video_path = profiles + "/0_" + \
                profiles + "_" + str(video) + ".mp4"
            try:
                Ai.face_detection_video(video_path)
            except Exception as e:
                print(e)
