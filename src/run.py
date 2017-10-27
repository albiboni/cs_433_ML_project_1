import numpy as np
from src.ensemble_log_regression import Config, EnsembleClassifiers, LogisticClassifier
from src.utils import dataloader, standardize, create_csv_submission, build_polynomial


def main():
    x, y = dataloader(mode='train', reduced=False)
    x_test = dataloader(mode='test', reduced=False)
    '''For the dataloader there are two modes train and test, depending on the dataset loaded.'''
    x = standardize(x)
    x_test = standardize(x_test)
    config = Config(batch_size=120, num_epochs=300, learning_rate=5*10**-4,
                    lambda_=2.15443469003e-05,
                    mode='train')
    '''There are two modes for config 'train', for training,  and 'cv', for cross validation. Any other mode will 
      start the training anyway.'''
    ensemble = EnsembleClassifiers(config, build_polynomial(x), y, 50, LogisticClassifier,
                                   label='ensemble_50_log')
    ensemble.train()
    predictions_test = ensemble.predict(ensemble(build_polynomial(x_test)))
    create_csv_submission(np.arange(350000, 350000 + x_test.shape[0]), predictions_test,
                          'dataset/submission_0x.csv')

if __name__ == '__main__':
    main()
