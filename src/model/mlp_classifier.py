import os
import log
import numpy as np
from model import Model
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc

from joblib import dump, load

class MyMLPClassifier(Model):
    def __init__(self):
        self.name = type(self).__name__[2:]
        self.model = MLPClassifier()

    def grid_search(self, X, y, n):
        hidden_layer_sizes = [(X.shape[1], ), (X.shape[1], X.shape[1]/2, )]
        activation = ['identity', 'logistic', 'tanh', 'relu']
        solver = ['lbfgs', 'sgd', 'adam']
        alpha = [1e-4, 1e-2, 1e+0, 1e+2]
        learning_rate = ['constant', 'invscaling', 'adaptive']
        tol = [1e-4, 1e-6, 1e-8, 1e-10, 1e-20]
        epsilon = [1e-1, 1e-2, 1e-3, 1e-5, 1e-10]

        parameters = [
            dict(hidden_layer_sizes=hidden_layer_sizes, activation=activation, solver=solver, alpha=alpha, learning_rate=learning_rate, tol=tol, epsilon=epsilon)
        ]

        self.run_grid_search(parameters, X, y, n)

    def learn(self, logger, set_list, names_list, n, engine):
        super(MyMLPClassifier, self).__init__(logger)

        for i, [[X_train, X_test, y_train, y_test], names] in enumerate(zip(set_list, names_list)):
            dump_file = './dump/%s/%s_%s' %(engine, self.name, i)
            if os.path.isfile(dump_file):
                self.model = load(dump_file)
            else:
                self.logger.log("debug", "cv(%d)" %i)
                self.grid_search(X_train, y_train, n)
                dump(self.model, dump_file)
            
            y_pred = self.model.predict(X_test)
            self.coef.append(["",""])

            self.accuracy_score.append(accuracy_score(y_test, y_pred))
            self.confusion_matrix.append(confusion_matrix(y_test, y_pred))
            self.report.append(classification_report(y_test, y_pred).replace('\n\n', '\n'))

            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            roc_auc = auc(fpr, tpr)
            self.roc_auc_score.append(roc_auc)
            self.add_tprs(fpr, tpr)
