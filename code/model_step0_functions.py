import keras
import numpy as np
import pandas as pd
import pickle
import time
from character_data import letters
from sample_split import Xy_sample
from visuals import make_subplots


def pickle_rw(*tuples, folder='../pickle/', write=True):
    """Pickle object in each tuple to/from ../pickle folder
    tuples = the filenames and objects to pickle ('name', name)"""
    result = []
    for tup in tuples:
        fname, obj = tup
        if write:
            with open(folder + fname + '.pkl', 'wb') as f:
                pickle.dump(obj, f)
        else:
            with open(folder + fname + '.pkl', 'rb') as f:
                result.append(pickle.load(f, encoding='bytes'))
    if result == []:
        return
    elif len(result) == 1:
        return result[0]
    else:
        return result


def architecture(model):
    """Obtain the model architecture.
    Return string to add to report"""
    arch = ''
    for config in model.get_config():
        class_name = config['class_name']

        if class_name == 'Flatten':
            arch += '- ' + class_name + '  \n'

        if class_name == 'Dense':
            units = config['config']['units']
            activation = config['config']['activation']
            arch += '- ' + class_name + ' ' + str(units) + ' '
            arch += activation + '  \n'

        if class_name == 'Conv2D':
            filters = config['config']['filters']
            kernel = config['config']['kernel_size']
            stride = config['config']['strides']
            activation = config['config']['activation']
            arch += '- ' + class_name + ' ' + str(filters) + ' '
            arch += str(kernel) + ' ' + str(stride) + ' '
            arch += activation + '  \n'

        if class_name == 'MaxPooling2D':
            pool = config['config']['pool_size']
            stride = config['config']['strides']
            arch += '- ' + class_name + ' ' + str(pool) + ' '
            arch += str(stride) + '  \n'

        if class_name == 'Dropout':
            rate = config['config']['rate']
            arch += '- ' + class_name + ' ' + str(rate) + '  \n'

    return arch


def training(history, run_id, model_id):
    """Save the training/validation accuracy plot
    Return string to add to report"""
    train = ''
    plt = pd.DataFrame(history.history)[['acc', 'val_acc']].plot(ylim=(0, 1))
    file = 'model' + str(model_id) + '_training.png'
    loc = '../runs/run' + str(run_id) + '/' + file
    plt.figure.savefig(loc)
    train += '#### Training Plot \n'
    train += '![](' + file + ')\n'
    return train


def weights(model, run_id, model_id):
    """Save the visualizations of the weights in the layers
    Return string to add to report"""
    wts = ''
    for layer_id, layer in enumerate(model.layers, 1):
        if type(layer) == keras.layers.core.Dense:
            w, b = layer.get_weights()
            size = w.shape[0]**.5
            if int(size) == size:
                w_images = np.asarray([w[..., i].reshape(int(size),
                                                         int(size), 1)
                                       for i in range(w.shape[1])])
                w_sample = Xy_sample(w_images, size=15)
                file = 'model' + str(model_id)
                file += '_layer' + str(layer_id) + '_weights.png'
                loc = '../runs/run' + str(run_id) + '/' + file
                make_subplots(w_sample, save=loc)
                wts += '#### Layer ' + str(layer_id)
                wts += ' Weights (Dense) - Sample Images \n'
                wts += '![](' + file + ')\n'

        if type(layer) == keras.layers.convolutional.Conv2D:
            w, b = layer.get_weights()
            w_images = np.asarray([w[:, :, 0, i] for i in range(w.shape[3])])
            w_images = np.expand_dims(w_images, axis=3)
            w_sample = Xy_sample(w_images, size=15)
            file = 'model' + str(model_id)
            file += '_layer' + str(layer_id) + '_weights.png'
            loc = '../runs/run' + str(run_id) + '/' + file
            make_subplots(w_sample, save=loc)
            wts += '#### Layer ' + str(layer_id)
            wts += ' Weights (Conv) - Sample Images \n'
            wts += '![](' + file + ')\n'
    return wts


def ltr_accuracy(model, X_train, y_train_num, X_val, y_val_num):
    """Calculuate train/validation accuracy by letter
    Return string to add to report"""
    acc = ''
    # Train
    train_correct_ = (model.predict_classes(X_train, verbose=False) ==
                      y_train_num).tolist()
    train_ltrs = letters(y_train_num)

    train_df = pd.DataFrame([train_ltrs, train_correct_]).T
    train_count = train_df.groupby(by=0).count()
    train_count.columns = ['TrainCount']
    train_correct = train_df.groupby(by=0).sum()
    train_correct.columns = ['TrainCorrect']
    accuracy_df = train_count.join(train_correct)
    accuracy_df['Train%Correct'] = round(accuracy_df.TrainCorrect /
                                         accuracy_df.TrainCount, 2)

    # Test
    val_correct_ = (model.predict_classes(X_val, verbose=False) ==
                    y_val_num).tolist()
    val_ltrs = letters(y_val_num)

    val_df = pd.DataFrame([val_ltrs, val_correct_]).T
    val_count = val_df.groupby(by=0).count()
    val_count.columns = ['ValCount']
    val_correct = val_df.groupby(by=0).sum()
    val_correct.columns = ['ValCorrect']

    # Join Test to Train
    accuracy_df = accuracy_df.join(val_count).join(val_correct)
    accuracy_df['Val%Correct'] = round(accuracy_df.ValCorrect /
                                       accuracy_df.ValCount, 2)

    # Add DataFrame to
    acc += '#### Letter Accuracy \n'
    acc += accuracy_df.to_html().replace('\n', '') + '\n'
    return acc


def validation_plots(model, X_val, y_val_num, run_id, model_id):
    pass
    """Save random correct/incorrect letter images from validation set
    Return string to add to report"""
    val = ''
    val_predict = model.predict_classes(X_val, verbose=False)

    val_correct = (val_predict == y_val_num)
    X_val_correct = X_val[val_correct]
    images = Xy_sample(X_val_correct, size=15)
    file = 'model' + str(model_id) + '_correct.png'
    loc = '../runs/run' + str(run_id) + '/' + file
    make_subplots(images, save=loc)
    val += '#### Accurate Validation Prediction - Sample Images \n'
    val += '![](' + file + ')\n'

    val_incorrect = (val_predict != y_val_num)
    X_val_incorrect = X_val[val_incorrect]
    images = Xy_sample(X_val_incorrect, size=15)
    file = 'model' + str(model_id) + '_incorrect.png'
    loc = '../runs/run' + str(run_id) + '/' + file
    make_subplots(images, save=loc)
    val += '#### Inaccurate Validation Prediction - Sample Images \n'
    val += '![](' + file + ')\n'

    return val


def report_save(start_time, report, model_id, model, history, run_id, results,
                X_train, y_train_num, X_val, y_val_num):
    """Update results/report and save model"""
    end_time = time.time()
    m, s = divmod((end_time - start_time),  60)
    elapsed = str(int(m)) + 'm:' + str(int(s)) + 's'
    results.append(['model' + str(model_id), history.epoch[-1], elapsed,
                    history.history['acc'][-1],
                    history.history['val_acc'][-1]])
    report += '## Model' + str(model_id) + '\n'
    report += '#### Architecture \n'
    report += architecture(model)
    report += training(history, run_id, model_id)
    report += weights(model, run_id, model_id)
    report += ltr_accuracy(model, X_train, y_train_num, X_val, y_val_num)
    report += validation_plots(model, X_val, y_val_num, run_id, model_id)
    # Save
    # model.save('../runs/run' + str(run_id) + '/model' +
    #            str(model_id) + '.h5')
    print('model' + str(model_id) + ' complete')
    return results, report
