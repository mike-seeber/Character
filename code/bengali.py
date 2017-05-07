from keras import backend as K
from keras.callbacks import EarlyStopping
from keras.layers import Dense, Flatten
from keras.models import load_model, Model, Sequential
from keras.preprocessing.image import ImageDataGenerator
from character_data import read_bengali
from sample_split import train_val_test_strat, y_categorical


def accuracy(model):
    """Compute accuracy and add to report"""
    global report
    _, trainacc = model.evaluate(X_train, y_train, verbose=False)
    _, valacc = model.evaluate(X_val, y_val, verbose=False)
    _, testacc = model.evaluate(X_test, y_test, verbose=False)
    report += '- Training Data: {0:.1%} \n'.format(trainacc)
    report += '- Validation Data: {0:.1%}  \n'.format(valacc)
    report += '- Test Data: {0:.1%}  \n'.format(testacc)


def model_bengali():
    """Model on bengali data"""
    model = Sequential()
    model.add(Flatten(input_shape=X_train.shape[1:]))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
    model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                  flow_batch_size),
                        epochs=epochs, verbose=False,
                        callbacks=[earlystop])
    accuracy(model)


def model_character(pooln):
    """Model bengali with features from character model
    Select character features from pool #n"""
    pool = char_model.get_layer('max_pooling2d_' + pooln).output
    flatten_1 = Flatten()(pool)
    dense_1 = Dense(100, activation='relu')(flatten_1)
    dense_2 = Dense(100, activation='relu')(dense_1)
    dense_3 = Dense(y_train.shape[1], activation='softmax')(dense_2)
    model = Model(inputs=char_model.input, outputs=dense_3)

    # Freeze Layers
    for layer in model.layers:
        if 'dense' in layer.name:
            pass
        else:
            layer.trainable = False

    # Compile, Run, Report
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
    model.fit_generator(flow, steps_per_epoch=int(X_train.shape[0] /
                                                  flow_batch_size),
                        epochs=epochs, verbose=False,
                        callbacks=[earlystop])
    accuracy(model)


if __name__ == "__main__":
    # Read in data
    X, y = read_bengali()

    # Strat split
    X_train, X_val, X_test, y_train_num, y_val_num, y_test_num = \
        train_val_test_strat(X, y)
    y_train, y_val, y_test = y_categorical(y_train_num, y_val_num, y_test_num)

    # Set model parameters
    loss = 'categorical_crossentropy'
    optimizer = 'adam'
    batch_size = 128
    epochs = 1000
    earlystop = EarlyStopping(monitor='acc', min_delta=.001, patience=50)

    # Define Image Datagenerator
    flow_batch_size = 128
    datagen = ImageDataGenerator(rotation_range=20,
                                 width_shift_range=0.15,
                                 height_shift_range=0.15,
                                 shear_range=0.2,
                                 zoom_range=0.2)
    flow = datagen.flow(X_train, y_train, batch_size=flow_batch_size)

    # Dense Model on Bengali Data
    report = '# Bengali Results  \n'
    report += '#### Dense Model  \n'
    model_bengali()

    # Bengali Model with Character Model Features
    char_model = load_model('../runs/final_model.h5')

    report += '\n#### Features from Character Model Pool #1  \n'
    model_character('1')
    report += '\n#### Features from Character Model Pool #2  \n'
    model_character('2')
    report += '\n#### Features from Character Model Pool #3  \n'
    model_character('3')

    # Save report
    with open('../runs/bengali_accuracy.md', mode='w') as f:
            f.write(report)
    K.clear_session()
