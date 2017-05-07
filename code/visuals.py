from collections import Counter
from keras.preprocessing.image import array_to_img
from math import ceil
import matplotlib.pyplot as plt
import pandas as pd
from string import ascii_uppercase
from sample_split import Xy_sample


def letter_subplots_train_test_split(letter, X_train, X_val, X_test,
                                     y_train_num, y_val_num, y_test_num):
    """Train/Test/Split subplots for input letter"""
    uppercase = [_ for _ in ascii_uppercase]
    letter_num = uppercase.index(letter)
    letter_train_ind = y_train_num == letter_num
    letter_val_ind = y_val_num == letter_num
    letter_test_ind = y_test_num == letter_num
    train_val_test = [X_train[letter_train_ind], X_val[letter_val_ind],
                      X_test[letter_test_ind]]
    for data in train_val_test:
        sample = Xy_sample(data)
        make_subplots(sample, close=False)


def make_subplots(X_sample, y_sample=None, columns=5, save=None, close=True):
    """Make subplots for the sample"""
    n = len(X_sample)
    rows = ceil(n / columns)
    plt.figure(figsize=(columns + 3, rows + 3))
    for i, sample in enumerate(X_sample, 1):
        plt.subplot(rows, columns, i)
        plt.imshow(array_to_img(sample).resize((120, 120)), cmap='gray')
        plt.axis('off')
    if save:
        plt.savefig(save)
    if close:
        plt.close('all')

    if y_sample is not None:
        [print(_, end=' ') for _ in y_sample]

    return


def train_val_test_composition(y_train, y_val, y_test):
    """Number of samples for each class for each split"""
    y_train_c, y_val_c, y_test_c = Counter(y_train), Counter(y_val), \
        Counter(y_test)
    y_df = pd.DataFrame([y_train_c, y_val_c, y_test_c]).T
    y_df.columns = ['train', 'val', 'test']
    # y_df.to_pickle('test.pkl')
    return y_df
