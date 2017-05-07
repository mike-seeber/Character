# To run on ec2
import matplotlib
matplotlib.use('Agg')
from keras import backend as K
from keras.callbacks import EarlyStopping
from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPool2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import pandas as pd
import time
from model_step0_functions import pickle_rw, architecture, training, \
    weights, ltr_accuracy, validation_plots, report_save


# Set Global Variables
model_id = 0
report = ''
results = []


def model_a():
    global model_id, report, results

    rotation_range = np.arange(0, 181, 1)
    width_shift_range = np.arange(0, 0.26, 0.01)
    height_shift_range = np.arange(0, 0.26, 0.01)
    shear_range = np.arange(0, 0.41, 0.01)
    zoom_range = np.arange(0, 0.41, 0.01)

    custom_results = []
    for i in range(60):
        rotation = np.random.choice(rotation_range, 1)[0]
        width = np.random.choice(width_shift_range, 1)[0]
        height = np.random.choice(height_shift_range, 1)[0]
        shear = np.random.choice(shear_range, 1)[0]
        zoom = np.random.choice(zoom_range, 1)[0]

        start_time = time.time()
        model_id += 1
        print('start', model_id)
        flow_batch_size = 128
        datagen = ImageDataGenerator(rotation_range=rotation,
                                     width_shift_range=width,
                                     height_shift_range=height,
                                     shear_range=shear,
                                     zoom_range=zoom)
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
        model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
        history = model.fit_generator(flow,
                                      steps_per_epoch=int(X_train.shape[0] /
                                                          flow_batch_size),
                                      epochs=epochs, verbose=False,
                                      validation_data=(X_val, y_val),
                                      callbacks=[earlystop])
        # Custom Results
        end_time = time.time()
        m, s = divmod((end_time - start_time),  60)
        elapsed = str(int(m)) + 'm:' + str(int(s)) + 's'
        acc = history.history['acc'][-1]
        val_acc = history.history['val_acc'][-1]
        custom_results.append([model_id, history.epoch[-1], elapsed, rotation,
                               width, height, shear, zoom, acc, val_acc])
    cols = ['model', 'epochs', 'time', 'rotation', 'width', 'height', 'shear',
            'zoom', 'acc', 'val_acc']
    results_df = pd.DataFrame(custom_results, columns=cols)
    results_df = results_df.set_index('model')

    report_head = '# Run ' + str(run_id) + '  \n'
    report_head += results_df.to_html().replace('\n', '') + '\n'
    with open('../runs/run' + str(run_id) + '/report.md', mode='w') as f:
        f.write(report_head + report)
    results_df.to_pickle('../runs/run' + str(run_id) + '/results_df.pkl')
    K.clear_session()


if __name__ == "__main__":
    # ### MANUALLY set run_id. ###
    run_id = 9

    # ### MANUALLY set run parameters ###
    loss = 'categorical_crossentropy'
    optimizer = 'adam'
    batch_size = 128
    epochs = 1000
    earlystop = EarlyStopping(monitor='acc', min_delta=.01, patience=20)

    # create run_id folder
    # os.makedirs('../runs/run' + str(run_id))

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

    # ### Run Models
    model_a()
    K.clear_session()
    print('finished')
