from keras import backend as K
from keras.callbacks import EarlyStopping
from keras.layers import Conv2D, Dense, Flatten, MaxPool2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import os
import pandas as pd
import time
from model_step0_functions import pickle_rw, architecture, training, \
    weights, ltr_accuracy, validation_plots, report_save


if __name__ == "__main__":
    # Set run parameters
    loss = 'categorical_crossentropy'
    optimizer = 'adam'
    batch_size = 128
    epochs = 1000
    earlystop = EarlyStopping(monitor='acc', min_delta=.01, patience=20)

    # Load data
    X_train, X_val, X_test, y_train_num, y_val_num, y_test_num, \
        y_train, y_val, y_test = pickle_rw(('X_train', 0),
                                           ('X_val', 0),
                                           ('X_test', 0),
                                           ('y_train_num', 0),
                                           ('y_val_num', 0),
                                           ('y_test_num', 0),
                                           ('y_train', 0),
                                           ('y_val', 0),
                                           ('y_test', 0), write=False)

    # Run model
    earlystop = EarlyStopping(monitor='acc', min_delta=.01, patience=20)

    flow_batch_size = 128
    datagen = ImageDataGenerator(rotation_range=20,
                                 width_shift_range=0.15,
                                 height_shift_range=0.15,
                                 shear_range=0.2,
                                 zoom_range=0.2)
    flow = datagen.flow(X_train, y_train, batch_size=flow_batch_size)

    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=2, strides=1,
                     activation='relu', padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=32, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer='adam', metrics=['accuracy'])
    model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                  flow_batch_size),
                        epochs=epochs, verbose=False,
                        validation_data=(X_val, y_val),
                        callbacks=[earlystop])

    # Compute Accuracy and Create Report
    _, trainacc = model.evaluate(X_train, y_train, verbose=False)
    _, valacc = model.evaluate(X_val, y_val, verbose=False)
    _, testacc = model.evaluate(X_test, y_test, verbose=False)

    report = '# Final Model - Accuracy Results  \n'
    report += '- Training Data: {0:.1%} \n'.format(trainacc)
    report += '- Validation Data: {0:.1%}  \n'.format(valacc)
    report += '- Test Data: {0:.1%}  \n'.format(testacc)
    with open('../runs/final_model_accuracy.md', mode='w') as f:
            f.write(report)

    # Save Model
    model.save('../runs/final_model.h5')
    K.clear_session()
