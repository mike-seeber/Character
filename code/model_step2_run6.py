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


# Set Global Variables
model_id = 0
report = ''
results = []


def model_a():
    global model_id, report, results
    start_time = time.time()
    model_id += 1
    flow_batch_size = 128
    datagen = ImageDataGenerator(rotation_range=20,
                                 width_shift_range=0.15,
                                 height_shift_range=0.15,
                                 shear_range=0.2,
                                 zoom_range=0.2)
    flow = datagen.flow(X_train, y_train, batch_size=flow_batch_size)
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=2, strides=1, activation='relu',
                     padding='same', input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=32, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
    history = model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                            flow_batch_size),
                                  epochs=epochs, verbose=False,
                                  validation_data=(X_val, y_val),
                                  callbacks=[earlystop])
    # Results, Report and save
    results, report = report_save(start_time, report, model_id, model, history,
                                  run_id, results, X_train, y_train_num,
                                  X_val, y_val_num)


def model_b():
    global model_id, report, results
    start_time = time.time()
    model_id += 1
    flow_batch_size = 128
    datagen = ImageDataGenerator(rotation_range=20,
                                 width_shift_range=0.15,
                                 height_shift_range=0.15,
                                 shear_range=0.2,
                                 zoom_range=0.2)
    flow = datagen.flow(X_train, y_train, batch_size=flow_batch_size)
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=2, strides=1, activation='relu',
                     padding='same', input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=32, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
    history = model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                            flow_batch_size),
                                  epochs=epochs, verbose=False,
                                  validation_data=(X_val, y_val),
                                  callbacks=[earlystop])
    # Results, Report and save
    results, report = report_save(start_time, report, model_id, model, history,
                                  run_id, results, X_train, y_train_num,
                                  X_val, y_val_num)


def model_c():
    global model_id, report, results
    start_time = time.time()
    model_id += 1
    flow_batch_size = 128
    datagen = ImageDataGenerator(rotation_range=20,
                                 width_shift_range=0.15,
                                 height_shift_range=0.15,
                                 shear_range=0.2,
                                 zoom_range=0.2)
    flow = datagen.flow(X_train, y_train, batch_size=flow_batch_size)
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=2, strides=1, activation='relu',
                     padding='same', input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=32, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(200, activation='relu'))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
    history = model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                            flow_batch_size),
                                  epochs=epochs, verbose=False,
                                  validation_data=(X_val, y_val),
                                  callbacks=[earlystop])
    # Results, Report and save
    results, report = report_save(start_time, report, model_id, model, history,
                                  run_id, results, X_train, y_train_num,
                                  X_val, y_val_num)


def model_d():
    global model_id, report, results
    start_time = time.time()
    model_id += 1
    flow_batch_size = 128
    datagen = ImageDataGenerator(rotation_range=20,
                                 width_shift_range=0.15,
                                 height_shift_range=0.15,
                                 shear_range=0.2,
                                 zoom_range=0.2)
    flow = datagen.flow(X_train, y_train, batch_size=flow_batch_size)
    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same', input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=256, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=256, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(200, activation='relu'))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
    history = model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                            flow_batch_size),
                                  epochs=epochs, verbose=False,
                                  validation_data=(X_val, y_val),
                                  callbacks=[earlystop])
    # Results, Report and save
    results, report = report_save(start_time, report, model_id, model, history,
                                  run_id, results, X_train, y_train_num,
                                  X_val, y_val_num)


def model_e():
    global model_id, report, results
    start_time = time.time()
    model_id += 1
    flow_batch_size = 128
    datagen = ImageDataGenerator(rotation_range=20,
                                 width_shift_range=0.15,
                                 height_shift_range=0.15,
                                 shear_range=0.2,
                                 zoom_range=0.2)
    flow = datagen.flow(X_train, y_train, batch_size=flow_batch_size)
    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same', input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=64, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=256, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=256, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(Conv2D(filters=256, kernel_size=2, strides=1, activation='relu',
                     padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(200, activation='relu'))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
    history = model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                            flow_batch_size),
                                  epochs=epochs, verbose=False,
                                  validation_data=(X_val, y_val),
                                  callbacks=[earlystop])
    # Results, Report and save
    results, report = report_save(start_time, report, model_id, model, history,
                                  run_id, results, X_train, y_train_num,
                                  X_val, y_val_num)


if __name__ == "__main__":
    # ### MANUALLY set run_id. ###
    run_id = 6

    # ### MANUALLY set run parameters ###
    report_head = '# Run ' + str(run_id) + '  \n'
    report_head += "- loss = 'categorical\_crossentropy'  \n"
    report_head += "- optimizer = 'adam'  \n"
    report_head += "- batch\_size = 128  \n"
    report_head += "- epochs = 1000  \n"
    report_head += "- earlystop = EarlyStopping(monitor='val\_acc',"
    report_head += "min\_delta=.01, patience=20)  \n"

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
    model_b()
    model_c()
    model_d()
    model_e()

    # ### Finish and Save Report
    results_df = pd.DataFrame(results, columns=['model', 'epochs', 'time',
                                                'trainacc', 'valacc'])
    results_df = results_df.set_index('model')
    report_head += '#### Summary Results \n'
    report_head += results_df.to_html().replace('\n', '') + '\n'
    with open('../runs/run' + str(run_id) + '/report.md', mode='w') as f:
        f.write(report_head + report)
    K.clear_session()
