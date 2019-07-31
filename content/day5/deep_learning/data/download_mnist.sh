#!/bin/bash

wget https://github.com/zalandoresearch/fashion-mnist/blob/master/data/fashion/t10k-images-idx3-ubyte.gz?raw=true
wget https://github.com/zalandoresearch/fashion-mnist/blob/master/data/fashion/t10k-labels-idx1-ubyte.gz?raw=true
wget https://github.com/zalandoresearch/fashion-mnist/blob/master/data/fashion/train-images-idx3-ubyte.gz?raw=true
wget https://github.com/zalandoresearch/fashion-mnist/blob/master/data/fashion/train-labels-idx1-ubyte.gz?raw=true
mv t10k-images-idx3-ubyte.gz\?raw\=true  t10k-images-idx3-ubyte.gz
mv t10k-labels-idx1-ubyte.gz\?raw\=true t10k-labels-idx1-ubyte.gz
mv train-images-idx3-ubyte.gz\?raw\=true train-images-idx3-ubyte.gz
mv train-labels-idx1-ubyte.gz\?raw\=true train-labels-idx1-ubyte.gz

