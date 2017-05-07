import numpy as np
import pandas as pd
from character_data import letters, read_bengali, read_characters
from sample_split import train_val_test_strat, Xy_sample, y_categorical
from visuals import letter_subplots_train_test_split, make_subplots, \
    train_val_test_composition


if __name__ == "__main__":
    # ### Test character data module ###
    # Test read_bengali()
    X, y = read_bengali()
    assert X.shape == (1393, 20, 20, 1)
    assert y.shape == (1393,)

    # Test letters()
    assert letters([0, 1, -1]) == ['A', 'B', 'Z']

    # Test read_characters()
    X, y = read_characters()
    # Confirm X, y shapes are correct
    assert X.shape == (4147, 20, 20, 1)
    assert y.shape == (4147,)

    # ### Test sample_split module ###
    # Test train_val_test_strat()
    split = (.7, .15, .15)
    X_train, X_val, X_test, y_train_num, y_val_num, y_test_num = \
        train_val_test_strat(X, y, split)
    # Confirm X and y lengths match
    assert (len(X_train), len(X_val), len(X_test)) == \
        (len(y_train_num), len(y_val_num), len(y_test_num))
    # Confirm X lengths are within 1% (not exact due to stratification)
    assert abs(split[0] - (len(X_train) / len(X))) < .01
    assert abs(split[1] - (len(X_val) / len(X))) < .01
    assert abs(split[1] - (len(X_test) / len(X))) < .01

    # Test Xy_sample()
    n = 5
    X_sample = Xy_sample(X, size=n)
    # Confirm sample shape is correct
    assert X_sample.shape == tuple([n] + [i for i in X.shape[1:]])
    X_sample, y_sample = Xy_sample(X, y, n)
    # Confirm sample shapes are correct
    assert X_sample.shape == tuple([n] + [i for i in X.shape[1:]])
    assert y_sample.shape == tuple([n] + [i for i in y.shape[1:]])

    # Test y_categorical()
    test_a, = y_categorical(np.asarray([0, 1, 2]))
    test_b, test_c = y_categorical(np.asarray([0, 1, 2]),
                                   np.asarray([0, 1, 2]))
    # Confirm test_a is correct
    assert (test_a == np.asarray([[1, 0, 0], [0, 1, 0], [0, 0, 1]])).all()
    # Confrim test_a, test_b, and test_c are all equal
    assert (test_a == test_b).all() and (test_b == test_c).all()
    # Confirm y_train has 26 letters
    assert y_categorical(y_train_num)[0].shape[1] == 26

    # ### Test visuals module ###
    # Test make_subplots()
    try:
        message = 'pass'
        make_subplots(X_sample)
        make_subplots(X_sample, letters(y_sample))
        make_subplots(X_sample, letters(y_sample), 10)
    except:
        message = 'fail'
    # Confirm function didn't fail
    assert message != 'fail'

    # Test train_val_test_composition()
    df = train_val_test_composition(y_train_num, y_val_num, y_test_num)
    assert df.shape[0] == 26

    # Test letter_subplots_train_test_split()
    try:
        message = 'pass'
        letter_subplots_train_test_split('K', X_train, X_val, X_test,
                                         y_train_num, y_val_num, y_test_num)
    except:
        message = 'fail'
    assert message != 'fail'
