import tensorflow as tf
from tflearn import DNN
import cv2
import sys
import errno
import csv
import numpy as np

legend = []

labels_dir = "images/data/legend.csv"
with open(labels_dir, 'r') as csvfile:
    legend_reader = csv.reader(csvfile)
    headers = next(legend_reader)
    for row in legend_reader:
        user_id = row[0]
        image_name = row[1]
        emotion = row[2]
        legend.append([image_name, emotion])

print(legend[1])

img_dir = "images/images/"

for entry in legend:
    print(entry[0])
    print(entry[1])
    img = cv2.imread(img_dir + entry[0])
    res = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)
    print(len(res))
    break
