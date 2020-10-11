# Automatic Image Captioning

Automatically describing the content of an image is a fundamental problem in artificial intelligence that connects computer vision and natural language processing. This is a generative model based on a deep recurrent architecture that combines recent advances in computer vision and machine translation and that can be used to generate natural sentences describing an image.

## Packages Used

The following packages were used:

1. numpy - For array computing
2. spacy - NLP package
3. tensorflow - ML framework
4. matplotlib, PIL, OpenCV2 - Image processing and visualizing
5. glob - To work with files

Use the package manager [pip](https://pypi.org/) to install the packages :

```bash
pip install package_name
```
## Architecture

![Architecture](https://github.com/siddarth-c/MachineLearning/blob/master/RNN/Image%20Captioning/Architecture.png "Title")

1. The image is resized into the dimension 229x229x3.
2. The reshaped image is then passed into a pre-trianed model InceptionV3(modified) to extract the feature vectors.
3. These feature vectors are passed to a LSTM.
4. Using the states of the previous LSTM as present states the sequence input are given one by one to a LSTM. ([Teacher Forcing](https://machinelearningmastery.com/teacher-forcing-for-recurrent-neural-networks/) is used)
5. Then the output of LSTM is passed through a series of Dense (red colour) and Dropout layers.
6. Finally a Dense layer (green colour) is used for the final prediction. <br>

Note that red Dense layers have 'Relu' as their activation function.<br>
The green Dense layers have 'Softmax' as their activation function.

Both the LSTM of image and captions must have the same size to share the states.

## Acknowledgements

Used the [Flicker8K](https://www.kaggle.com/shadabhussain/flickr8k) from Kaggle.

This project is loosely inspired from the [Show and Tell paper](https://arxiv.org/abs/1411.4555) by Google. 

Also refer this [link](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) for a clear understanding on LSTM. 

This model has to be trained on more data and with better hyper parameters for better results. 
