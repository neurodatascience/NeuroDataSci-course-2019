#!/usr/bin/env python
from copy import copy
from sklearn.preprocessing import OneHotEncoder
import gzip
import matplotlib.pyplot as plt
import numpy as np
import os
import pickle
import sys
import time
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def load_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)

    return(data)


def load_mnist_raw(path, kind='train'):
    """Load Fashion MNIST data from path."""
    labels_path = os.path.join(path, '%s-labels-idx1-ubyte.gz' % kind)
    images_path = os.path.join(path, '%s-images-idx3-ubyte.gz' % kind)

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)

    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8,
            offset=16).reshape(len(labels), 784)

    return(images, labels)


def get_circles_data():
    """Loads circles data. A simple dataset."""
    data = np.loadtxt(open('data/circles.txt','r'))
    X = data[:, :2]
    y = data[:, 2]

    X_train = X[:800, :]
    X_valid = X[800:950, :]
    X_test  = X[950:, :]
    y_train = y[:800]
    y_valid = y[800:950]
    y_test  = y[950:]

    data = {"X": {"train": X_train, "valid": X_valid, "test": X_test},
            "y": {"train": y_train, "valid": y_valid, "test": y_test}}

    return(data)


def make_mnist_proc(output):
    """Make a preprocessed version of fashion MNIST data."""
    if os.path.isfile(output):
        print('preprocessed MNIST already exists, skipping preprocessing')
        return(None)

    split = 50000
    X_train, y_train = load_mnist_raw('data/', kind='train')
    X_test, y_test = load_mnist_raw('data/', kind='t10k')

    X_valid = X_train[split:, :]
    X_train = X_train[:split, :]
    y_valid = y_train[split:]
    y_train = y_train[:split]

    # NORMALIZE DATA HERE

    data = {"X": {"train": X_train, "valid": X_valid, "test": X_test},
            "y": {"train": y_train, "valid": y_valid, "test": y_test}}

    print('saving preprocessed MNIST data at {}'.format(output))
    with open(output, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


class MLP:
    def __init__(self, **kwargs):

        hyperparameters = {
            'n_i'    : 784,
            'n_h'    : 10,
            'n_o'    : 10,
            'epochs' : 10,
            'k'      : 50,
            'lr'     : 0.01,
            'l1'     : 0,
            'l2'     : 0,
            'stupid_loop': False
        }

        hyperparameters.update(kwargs)

        print('MLP initialized with parameters:')
        for hp in hyperparameters.items():
            print('    {} = {}'.format(hp[0], hp[1]))

        self.n_i = hyperparameters['n_i']       # input dimensions
        self.n_h = hyperparameters['n_h']       # number of hidden units
        self.n_o = hyperparameters['n_o']       # number of output units
        self.epochs = hyperparameters['epochs'] # n epochs
        self.k   = hyperparameters['k']         # minibatch size
        self.lr  = hyperparameters['lr']        # learning rate
        self.l1 = hyperparameters['l1']         # lambda l1
        self.l2 = hyperparameters['l2']         # lambda l2
        self.stupid_loop = hyperparameters['stupid_loop'] # do something stupid

        # negative values of k run in BATCH mode
        if self.k <= 0:
            self.minibatch = False
            print('k={}, using BATCH mode'.format(self.k))
        else:
            self.minibatch = True
            print('using batch size k={}'.format(self.k))

        # construct network and initialize weights
        self.W1 = self._init_W(self.n_i, self.n_h)
        self.W2 = self._init_W(self.n_h, self.n_o)
        self.b1 = np.zeros(self.n_h)
        self.b2 = np.zeros(self.n_o)

        # for softmax loss
        self.onehot = OneHotEncoder(sparse=False, n_values=self.n_o)

        # gradients
        self.dL_W1 = 0
        self.dL_b1 = 0
        self.dL_W2 = 0
        self.dL_b2 = 0

    def _get_params(self):
        return(zip([self.W1, self.W2, self.b1, self.b2],
                   [self.dL_W1, self.dL_W2, self.dL_b1, self.dL_b2]))

    def _init_W(self, n_in, n_out):
        """Initializes weight matrix."""
        # Xavier initialization (pros only): sample weights uniformly from
        # [-1/sqrt(n_previous_layer), 1/np.sqrt(n_previous_layer)].
        W = None
        return(W)

    def _get_minibatches(self, X, shuffle=True):
        """use the number of samples in X and k to determine the batch size"""
        idx = np.arange(X.shape[0])
        if shuffle:
            np.random.shuffle(idx)

        # if the final batch size is smaller than k, append -1s for reshape
        if self.k > 1 and self.k != X.shape[0]:
            rem = len(idx) % self.k
            idx = np.hstack((idx, np.repeat(-1, (self.k-rem))))

        idx = idx.reshape(int(len(idx) / self.k), self.k)

        # load minibatches as a list of numpy arrays
        mbs = []
        for mb in np.arange(idx.shape[0]):
            mbs.append(idx[mb, :])

        # if -1's are in the final batch, remove them
        mbs[-1] = np.delete(mbs[-1], np.where(mbs[-1] == -1)[0])
        if len(mbs[-1]) == 0:
            mbs = mbs[:-1]

        return(mbs)

    def _softmax(self, X):
        """Numerically stable softmax."""
        exps = np.exp(X - np.max(X, axis=1).reshape(-1, 1))
        return(exps / np.sum(exps, axis=1).reshape(-1, 1))

    def _softmax_backward(self, y_hat, y):
        """Backprop of softmax."""
        y_one = self.onehot.fit_transform(y.reshape(-1,1))
        return(y_hat - y_one)

    def _relu(self, n):
        """Calculates rectifier activation for all elements of n."""
        return(np.maximum(np.zeros(n.shape), n))

    def _relu_backward(self, z):
        """If previous layer pre-activated vals were <= 0, also set z to 0."""
        z[z <= 0] = 0
        z[z > 0] = 1
        return(z)

    def _nll_loss(self, x, y):
        y_hat = self.fprop(x, train=False)
        y_one = self.onehot.fit_transform(y.reshape(-1,1))

        prob = np.einsum('ky,ky->k', y_hat, y_one)
        loss = -np.log(prob)

        # add regularization
        if any ([self.l1, self.l2]):
            loss += self.l1 * np.sum(np.abs(self.W1))
            loss += self.l2 * np.sum(np.square(self.W1))
            loss += self.l1 * np.sum(np.abs(self.W2))
            loss += self.l2 * np.sum(np.square(self.W2))

        loss = np.mean(loss)

        return(loss)

    def fprop(self, X, train=True):
        """take inputs, and push them through to produce a prediction y"""

        ha = None  # hidden layer pre-activations
        hs = None  # hidden layer activations
        oa = None  # output pre-activations
        os = None  # this is y_hat

        assert(ha.shape == (X.shape[0], self.W1.shape[1]))
        assert(os.shape == (hs.shape[0], self.W2.shape[1]))

        if train == True:
            self.ha, self.hs, self.oa, self.os = ha, hs, oa, os

        return(os)

    def bprop(self, X, y_hat, y, train=True):
        """
        backpropogate error between y_hat and y to update all parameters
        dL_b and dL_W are both normalized by batch size
        """
        # NB: divide gradients by self.this_k here!
        # gradients for output --> hidden layer
        dL_oa = None  # act wrt err
        dL_hs = None  # prev_activations
        self.dL_W2 = None  # weights wrt err
        self.dL_b2 = None  # bias wrt error

        # gradients for hidden --> input layer
        dhs_ha = None  # act wrt error
        dL_ha  = None  # pre/post act
        self.dL_W1  = None  # weights wrt err
        self.dL_b1  = None  # bias wrt err

        assert(self.dL_W2.shape == self.W2.shape)
        assert(self.dL_W1.shape == self.W1.shape)
        assert(self.dL_b1.shape == self.b1.shape)
        assert(self.dL_b2.shape == self.b2.shape)

        # calculate regularization
        reg_l11 = self.l1 * np.sign(self.W1)  # derivative of abs(x) = sign(x)
        reg_l21 = self.l1 * np.sign(self.W2)  #
        reg_l12 = self.l2 * 2 * self.W1       # derivative of x**2 = 2x
        reg_l22 = self.l2 * 2 * self.W2       #

        # update all parameters via gradient descent with regularization
        self.W1 -= None
        self.W2 -= None
        self.b1 -= None
        self.b2 -= None

    def predict(self, X):
        y_hat = self.fprop(X, train=False)
        return(np.argmax(y_hat.T, axis=0))

    def accuracy(self, X, y):
        correct, total = 0, 0
        y_hat = self.predict(X)
        correct += (y_hat == y).sum()
        total += len(y)
        acc = correct / total

        return(round(acc*100, 4))

    def plot_decision(self, X, y, ax=None, h=0.07):
        """plot the decision boundary. h controls plot quality."""
        if ax is None:
            fig, ax = plt.subplots(figsize=(7, 6))

        # https://stackoverflow.com/a/19055059/6027071
        # sample a region larger than our training data X
        x_min = X[:, 0].min() - 0.5
        x_max = X[:, 0].max() + 0.5
        y_min = X[:, 1].min() - 0.5
        y_max = X[:, 1].max() + 0.5
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))

        # plot decision boundaries
        x = np.concatenate(([xx.ravel()], [yy.ravel()]))
        pred = self.predict(x.T).reshape(xx.shape)
        ax.contourf(xx, yy, pred, alpha=0.8,cmap='RdYlBu')

        # plot points (coloured by class)
        ax.scatter(X[:, 0], X[:, 1], alpha=0.8, c=y, cmap='RdYlBu')
        ax.axis('off')

        title = "nh={}_lr={}_l1={}_l2={}_epochs={}".format(
            self.n_h, self.lr, self.l1, self.l2, self.epochs)
        ax.set_title(title)

        output = 'img/decision_boundary_nh-{}_lr-{}_l1-{}_l2-{}_epochs-{}.jpg'.format(
            self.n_h, self.lr, self.l1, self.l2, self.epochs)
        plt.savefig(output)
        plt.close()

    def grad_check(self, X, y, name):
        """
        finite differences to check for correct gradient computation for each
        scalar parameter theta_k ,change the parameter value by adding a small
        perturbation (10^-5 and calculate the new value of the loss, then set
        the value of the parameter back to its original value. The partial
        derivative with respect to this parameter is estimated by dividing the
        change in the loss function by the pertubation. The ratio of your
        gradient computed by backpropagation and your estimate using finite
        difference should be between 0.99 and 1.01.
        """
        X = np.atleast_2d(X)     # order is crucial for k=1 case
        self.this_k = X.shape[0] #
        smol_eps = sys.float_info.min*sys.float_info.epsilon

        # initialized all parameters with some values
        y_hat = self.fprop(X, train=True)
        self.bprop(X, y_hat, y)

        loss_raw = self._nll_loss(X, y)

        grad_fds = []
        grad_bprops = []

        for param, grad in self._get_params():
            param = np.atleast_2d(param)
            grad = np.atleast_2d(grad)

            for theta_i in range(param.shape[0]):
                for theta_j in range(param.shape[1]):

                    eps = np.random.uniform(10e-6, 11e-4)
                    param[theta_i, theta_j] += eps
                    loss_mod = self._nll_loss(X, y)
                    param[theta_i, theta_j] -= eps

                    # do NOT normalize finite difference gradient by batch size!
                    # grad_bprop normalized by batch size in bprop function
                    grad_fd = (loss_mod - loss_raw) / (eps)
                    grad_bprop = grad[theta_i, theta_j]

                    # handle some edge cases, add smol_eps for stability
                    if np.abs(grad_fd - grad_bprop) < 10e-4:
                        ratio = 1
                    elif grad_bprop == 0:
                        ratio = 1
                    elif grad_fd == 0:
                        ratio = 1
                    else:
                        ratio = (grad_fd + smol_eps) / (grad_bprop + smol_eps)

                    grad_fds.append(grad_fd)
                    grad_bprops.append(grad_bprop)

                    if ratio < 0.99 or ratio > 1.01:
                        print('gradient checking failed: loss_raw={}, loss_mod={}, fd={}, bprop={}'.format(
                            loss_raw, loss_mod, grad_fd, grad_bprop))
                        raise Exception('check ur grads bra')

        plt.plot(grad_fds, linewidth=2, alpha=0.7, color='r')
        plt.plot(grad_bprops, linewidth=1.8, alpha=0.7, linestyle='--', color='black')
        plt.legend(['finite differences', 'backpropagation'])
        plt.xlabel('parameter number')
        plt.ylabel('gradient')
        plt.savefig('img/gradient_differences_{}_k{}.jpg'.format(name, self.this_k))
        plt.close()

    def eval(self, X, y):

        if self.minibatch == False:
           self.k = X.shape[0]

        # Split data into minibatches (incl. stochastic and batch case).
        minibatches = self._get_minibatches(X)

        total_acc, total_loss = 0, 0

        for j, batch in enumerate(minibatches):
            total_acc += self.accuracy(X[batch, :], y[batch])
            total_loss += self._nll_loss(X[batch, :], y[batch])

        total_acc /= len(minibatches)
        total_loss /= len(minibatches)

        return(total_acc, total_loss)

    def train(self, data):

        results = {'loss':     {'train': [], 'valid': [], 'test': []},
                   'accuracy': {'train': [], 'valid': [], 'test': []}
        }

        # Training data.
        X = None
        y = None

        for i in range(self.epochs):

            # Handles batch gradient descent.
            if self.minibatch == False:
               self.k = X.shape[0]

            # split data into minibatches (incl. stochastic and batch case)
            minibatches = self._get_minibatches(X)

            # TRAIN THE MODEL HERE
            for j, batch in enumerate(minibatches):
                self.this_k = len(batch)
                y_hat = None
                self.bprop(None, None, None)
                acc_train, loss_train = self.eval(None, None)

                if j % 25 == 0:
                    print('TRAIN [epoch {}: batch {}/{}]: accuracy={}, loss={}'.format(
                        i+1, j+1, len(minibatches), acc_train, loss_train))

            # EVALUATE THE MODEL HERE
            acc_valid, loss_valid = self.eval(None)
            acc_test, loss_test = self.eval(None)

            print('VALID [epoch {}: batch {}/{}]: accuracy={}, loss={}'.format(
                i+1, j+1, len(minibatches), acc_valid, loss_valid))
            print('TEST  [epoch {}: batch {}/{}]: accuracy={}, loss={}'.format(
                i+1, j+1, len(minibatches), acc_test, loss_test))

            # store end-of-epoch results for train, valid, test
            results['loss']['train'].append(loss_train)
            results['loss']['valid'].append(loss_valid)
            results['loss']['test'].append(loss_test)
            results['accuracy']['train'].append(acc_train)
            results['accuracy']['valid'].append(acc_valid)
            results['accuracy']['test'].append(acc_test)

        return(results)


def exp1():
    """
    Compare gradients of SGD, minibatch SGD, and batch GD. Also, note
    execution time.
    """
    data = get_circles_data()

    mlp = MLP(n_i=2, n_h=2, n_o=2, lr=5e-6, epochs=1, k=1)
    mlp.train(data)
    mlp.grad_check(data['X']['train'][1, :], data['y']['train'][1],
        'stochastic gradient descent')

    mlp = MLP(n_i=2, n_h=2, n_o=2, lr=5e-6, epochs=1, k=100)
    mlp.train(data)
    mlp.grad_check(data['X']['train'][:10, :], data['y']['train'][:10],
        'minibatch stochastic gradient descent')

    mlp = MLP(n_i=2, n_h=2, n_o=2, lr=5e-6, epochs=1, k=-1)
    mlp.train(data)
    mlp.grad_check(data['X']['train'][:10, :], data['y']['train'][:10],
        'batch gradient descent')


def exp2():
    """
    Two circles: grid search showing effect on decision bondary, capacity.
    """
    data = get_circles_data()

    options = {'n_h': 3, 'lr': 10e-3, epochs: 5, 'k': 256,
               'l11': 0, 'l12': 0.001, 'l21': 0, 'l22': 0.001}
    mlp = MLP(n_i=2, n_o=2, **options)
    results = mlp.train(data)
    mlp.plot_decision(data['X']['train'], data['y']['train'])


def exp3():
    """
    Plot accuracy and average loss per epoch for train / valid / test.
    Hyperparameter selection is up to you. You should be able to get less than
    20% test error.
    """
    data = load_pickle('data/fashion_mnist.pkl')

    options = {'n_h': 10, 'lr': 10e-2, 'epochs': 5, 'k': 256,
               'l11': 0, 'l12': 0, 'l21': 0, 'l22': 0.001}
    mlp = MLP(n_i=784, n_o=10, **options)
    results = mlp.train(data)

    # Plotting here

if __name__ == '__main__':

    exp1() # Gradient checking / execution time of SGD, minibatch SGD, GD.
    exp2() # Effects of network parameters and regularizers on network capacity.
    exp3() # Experiment tracking (plotting of loss / accuracy curves).
