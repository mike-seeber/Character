from keras.utils import to_categorical
import numpy as np


def train_val_test_strat(X, y, split=(.6, .2, .2)):
    """Stratified split into training, validation, test
    X, y expect numpy arrays"""
    # Gather indexes for each character in a dictionary
    y_index = {}
    for i, k in enumerate(y):
        if k in y_index:
            y_index[k].append(i)
        else:
            y_index[k] = [i]

    # Split indices for each attribute of y between train/val/test
    train_ind = []
    val_ind = []
    test_ind = []
    for k, v in y_index.items():
        n = len(v)
        # Shuffle v in place
        np.random.shuffle(v)
        split1 = int(n * split[0])
        split2 = int(n * (split[0] + split[1]))
        train_ind = train_ind + v[:split1]
        val_ind = val_ind + v[split1:split2]
        test_ind = test_ind + v[split2:]

    return X[train_ind], X[val_ind], X[test_ind], \
        y[train_ind], y[val_ind], y[test_ind]


def Xy_sample(X, y=None, size=5):
    """Take a random sample form X and y"""
    sample_indices = np.random.choice(range(len(X)),
                                      min(size, len(X)),
                                      replace=False)
    if y is not None:
        return X[sample_indices], y[sample_indices]
    else:
        return X[sample_indices]


def y_categorical(*y):
    """Make each y in list of y's categorical"""
    return [to_categorical(_, len(set(_))) for _ in y]
