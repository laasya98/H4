# H4

## Overview

H4 is a project created for CS 4701: Practicum in Artificial Intelligence at Cornell University, created by Andrea Benson, Laasya Renganathan, and Saachi Gopal.

H4 is a Python-based HTR (Handwritten Text Recognition) system utilizing principles of CV, AI, and ML to transcribe handwritten Hiragana characters, a phonetic alphabet of the Japanese writing system, digitally and provide machine translations of the results.

Our project consists of CV preprocessing using [OpenCV](https://opencv.org/), a two-layer CNN using [Keras](https://keras.io/), and a Machine Translation module implemented using the [googletrans](https://py-googletrans.readthedocs.io/en/latest/) library. Our project accepts custom inputs for test data, but our primary dataset comes from the [Kuzushiji](https://towardsdatascience.com/kuzushiji-mnist-japanese-literature-alternative-dataset-for-deep-learning-tasks-d48ae3f5395b) project.

## Usage
Download the K-49 training and test data from the Kuzushiji [repository](https://github.com/rois-codh/kmnist/) prior to running this code. All required imports are listed at the top of the h4.ipynb file. Please pip install them if not already downloaded.

## Files

h4.ipynb: main code source.
hi.png; thanks.png: test images used in for custom input.
cm.csv: contains the results of our confusion matrix used in evaluation.
