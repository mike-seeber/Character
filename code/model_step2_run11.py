import matplotlib
matplotlib.use('Agg')
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
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(d1_units, activation='relu'))
    model.add(Dense(d2_units, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer='sgd', metrics=['accuracy'])
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
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(d1_units, activation='relu'))
    model.add(Dense(d2_units, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer='rmsprop', metrics=['accuracy'])
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
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(d1_units, activation='relu'))
    model.add(Dense(d2_units, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer='adagrad', metrics=['accuracy'])
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
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(d1_units, activation='relu'))
    model.add(Dense(d2_units, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer='adadelta', metrics=['accuracy'])
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
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(d1_units, activation='relu'))
    model.add(Dense(d2_units, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer='adam', metrics=['accuracy'])
    history = model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                            flow_batch_size),
                                  epochs=epochs, verbose=False,
                                  validation_data=(X_val, y_val),
                                  callbacks=[earlystop])
    # Results, Report and save
    results, report = report_save(start_time, report, model_id, model, history,
                                  run_id, results, X_train, y_train_num,
                                  X_val, y_val_num)


def model_f():
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
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(d1_units, activation='relu'))
    model.add(Dense(d2_units, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer='adamax', metrics=['accuracy'])
    history = model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                            flow_batch_size),
                                  epochs=epochs, verbose=False,
                                  validation_data=(X_val, y_val),
                                  callbacks=[earlystop])
    # Results, Report and save
    results, report = report_save(start_time, report, model_id, model, history,
                                  run_id, results, X_train, y_train_num,
                                  X_val, y_val_num)


def model_g():
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
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Conv2D(filters=c1_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c2_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(Conv2D(filters=c3_filters, kernel_size=2, strides=1,
                     activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Flatten())
    model.add(Dense(d1_units, activation='relu'))
    model.add(Dense(d2_units, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer='nadam', metrics=['accuracy'])
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
    run_id = 11

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

    # Set filter/unit sizes
    c1_filters = 32
    c2_filters = 64
    c3_filters = 128
    d1_units = 100
    d2_units = 100

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
    model_f()
    model_g()

    # ### Finish and Save Report
    results_df = pd.DataFrame(results, columns=['model', 'epochs', 'time',
                                                'trainacc', 'valacc'])
    results_df = results_df.set_index('model')

    # Custom results_df - add optimizer
    results_df['optimizer'] = ['sgd', 'rmsprop', 'adagrad', 'adadelta', 'adam',
                               'adamax', 'nadam']
    results_df = results_df[['optimizer', 'epochs', 'time', 'trainacc',
                            'valacc']]

    # Continue normal report
    report_head += '#### Summary Results \n'
    report_head += results_df.to_html().replace('\n', '') + '\n'
    with open('../runs/run' + str(run_id) + '/report.md', mode='w') as f:
        f.write(report_head + report)
    K.clear_session()
