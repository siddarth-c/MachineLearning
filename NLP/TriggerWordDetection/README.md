# Trigger Word Detection


A trigger word is defined as “a word that initiates a process or course of action". <br>
Essentially, any word that gets someone to do something — anything — can be defined as a trigger word.<br>
This model is trained to respond to the word 'Marvin'.

## Used libraries

Following are the main libraries used in this notebook:<br>

1. tensorflow - deep learning frame work
2. pydub - audio pre-processing 1
3. librosa - audio pre-processing 2


## About

This model is trained to respond to the word 'Marvin'. The architecture used in this model is similar to ![here](https://github.com/siddarth-c/MachineLearning/blob/master/NLP/TriggerWordDetection/Model_architecture.png "Title").

You may have found many trigger words notebooks on GitHub which are similar to the one found in the Coursera Deeplearning specialization. But this notebook is simple and different in the following ways : <br>

1. A similar model but with different dimensions and activation functions were used.
2. The model was trained on a different dataset.
3. Different library (Vebroasa) was used for extracting features from the audio signal.

Also this model was created from scratch and is not another replica of the coursera notebook. For the sake of simplicity the notebook has been divides into 2 parts. <br>
1. TWD Part 1 - Data pre-processing and creation
2. TWD Part 2 - Model training


## Acknowledgements

APA-style citation: "Warden P. Speech Commands: A public dataset for single-word
speech recognition, 2017. Available from
http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz".

## Useful links

1. https://www.coursera.org/lecture/nlp-sequence-models/trigger-word-detection-Li4ts
2. https://www.youtube.com/watch?v=Oa_d-zaUti8
