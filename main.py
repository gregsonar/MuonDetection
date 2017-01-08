# coding=utf-8

"""
По материалам статьи: https://geektimes.ru/post/283914/
Скрипт для обработки фотографий с целью поиска следов элементарных заряженных частиц - мюонов
Script for processing images in order to find traces of elementary particles - muons μ"""


import os
import datetime
from PIL import Image


# Get all files in a folder and subfolders
def get_media_files_list(path_to_folder):
    file_paths = []
    for root, directories, files in os.walk(path_to_folder):
        for filename in files:
            if ".jpg" in filename.lower() or ".png" in filename.lower() or ".tif" in filename.lower():
                # Save full file path
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
    return file_paths


# Analyze content of the image files
def analyze_files(files_list, threshold_time):
    for index, path in enumerate(files_list):
        start_time = datetime.datetime.now()
        photo = Image.open(path)
        photo = photo.convert('L')
        b = max(set(photo.getdata()))
        d_t = (datetime.datetime.now() - start_time).total_seconds()
        if b > threshold_time:
            print("{}, {}, {}, {};    !!!".format(index, b, path, d_t))
        else:
            print("{}, {}, {}, {};".format(index, b, path, d_t))

folder = "data/images/"
threshold = 130

filesList = get_media_files_list(folder)

print("Analyze {} files:".format(len(filesList)))

analyze_files(filesList, threshold)

print("Done")
