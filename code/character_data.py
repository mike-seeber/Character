import glob
from keras.preprocessing.image import array_to_img, img_to_array
import numpy as np
import pandas as pd
from PIL import Image
import re
from string import ascii_uppercase


def read_bengali():
    """Read bengali digit images and labels in from file"""
    # Import X
    X_folder = '/Users/michaelseeber/Documents/Projects/'
    X_folder += 'Data/Bengali_Digit/images/'
    X_files = glob.glob(X_folder + '*')
    X_id_pattern = '\/digit_(\d*).jpg'
    X_id = [int(re.findall(X_id_pattern, X_file)[0]) for X_file in X_files]
    X_color = np.asarray([img_to_array(Image.open(X_file).resize((20, 20)))
                          for X_file in X_files])
    # Convert to grayscale and scale between 0 and 1
    X_gray = np.asarray([img_to_array(array_to_img(_).convert('L'))
                         for _ in X_color]) / 255

    # Import y
    y_file = '/Users/michaelseeber/Documents/Projects/'
    y_file += 'Data/Bengali_Digit/labels2.csv'
    y_dict = pd.read_csv(y_file, index_col='ID').to_dict()
    y_digit = np.asarray([y_dict['Class']['digit_' + str(i)] for i in X_id])

    return X_gray, y_digit


def read_characters():
    """Read character images and labels in from file"""
    # Import X
    X_folder = '/Users/michaelseeber/Documents/Projects/'
    X_folder += 'Data/characters/images/'
    X_files = glob.glob(X_folder + '*')
    X_id_pattern = '\/(\d*).Bmp'
    X_id = [int(re.findall(X_id_pattern, X_file)[0]) for X_file in X_files]
    X_color = np.asarray([img_to_array(Image.open(X_file))
                          for X_file in X_files])
    # Convert to grayscale and scale between 0 and 1
    X_gray = np.asarray([img_to_array(array_to_img(_).convert('L'))
                         for _ in X_color]) / 255

    # Import y
    y_file = '/Users/michaelseeber/Documents/Projects/'
    y_file += 'Data/characters/Labels.csv'
    y_dict = pd.read_csv(y_file, index_col='ID').to_dict()
    y_ltr = np.asarray([y_dict['Class'][i] for i in X_id])

    # Limit to Uppercase
    uppercase = [ltr for ltr in ascii_uppercase]
    X = []
    y_upper = []
    for i, ltr in enumerate(y_ltr):
        if ltr in uppercase:
            X.append(X_gray[i])
            y_upper.append(ltr)

    # Convert ltr to number (A=0, B=1, etc.)
    y = [uppercase.index(_) for _ in y_upper]

    return np.asarray(X), np.asarray(y)


def letters(y_sample):
    """Obtain ltrs for y_sample"""
    uppercase = [ltr for ltr in ascii_uppercase]
    return [uppercase[_] for _ in y_sample]
