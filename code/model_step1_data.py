from character_data import letters, read_characters
from model_step0_functions import pickle_rw
from sample_split import train_val_test_strat, Xy_sample, y_categorical
from visuals import letter_subplots_train_test_split, make_subplots, \
    train_val_test_composition


if __name__ == "__main__":
    # Read in X, y
    X, y = read_characters()

    # Take 5 sample images and plot
    X_sample, y_sample = Xy_sample(X, y, 5)
    make_subplots(X_sample)

    # Stratified split into training/validation/test
    X_train, X_val, X_test, y_train_num, y_val_num, y_test_num = \
        train_val_test_strat(X, y)

    # Create composition visual (dataframe) for train/test/split
    # ### Commented out, since incorporated elsewhere in the report
    # train_val_test_composition(letters(y_train_num), letters(y_val_num),
    #                            letters(y_test_num))

    # Turn y into categorical
    y_train, y_val, y_test = y_categorical(y_train_num, y_val_num, y_test_num)

    # Train/Test/Split subplots for input letter
    # ### Commented out, since incorporated elsewhere in the report
    # letter_subplots_train_test_split('K', X_train, X_val, X_test,
    #                                  y_train_num, y_val_num, y_test_num)

    pickle_rw(('X_train', X_train),
              ('X_val', X_val),
              ('X_test', X_test),
              ('y_train_num', y_train_num),
              ('y_val_num', y_val_num),
              ('y_test_num', y_test_num),
              ('y_train', y_train),
              ('y_val', y_val),
              ('y_test', y_test))
