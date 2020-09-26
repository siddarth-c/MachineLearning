# Toxic Comment Filter

Classify comments as hateful or hate free.

## Installation

Use the package manager [pip](https://pypi.org/) to install the following packages:

1. streamlit - Used to build custom web apps
2. numpy - For array computing
3. spacy - NLP package
4. tensorflow - ML framework

```bash
pip install streamlit
pip install spacy
pip install numpy
pip install tensorflow
```
## How to Run

To run the application you will be needing the following files:

1. [Streamlit file](https://github.com/siddarth-c/MachineLearning/blob/master/RNN/ToxicComments/ToxicComments%20Streamlit.py)
2. [Word to integer dictionary](https://drive.google.com/file/d/1RAHists8dDo6V1nO7CzhklmvGgeAywAr/view?usp=sharing)
3. Pre-trained Model -> Will be uploaded soon.

Download the above files and save them in same directory.
Now run the python line
```python
streamlit run ToxicComments Streamlit.py
```
## Result

This image is shows the result of the Neural Network when a hate free comment is given as input.
![Hate Free Comment](https://github.com/siddarth-c/MachineLearning/blob/master/RNN/ToxicComments/HateFreeComment.jpg?raw=true "Title")

This image is shows the result of the Neural Network when a hate/toxic comment is given as input.
![Hate Comment](https://github.com/siddarth-c/MachineLearning/blob/master/RNN/ToxicComments/HateComment.jpg?raw=true "Title")
