#!/usr/bin/env python
# coding: utf-8

# In[13]:


import streamlit as st

import spacy
from spacy.lang.en.stop_words import STOP_WORDS

import numpy as np

from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.models import Sequential 
from tensorflow.keras import layers


# In[9]:


nlp = spacy.load('en_core_web_sm',disable=["tagger", "parser"])

w2s = np.load('word2seq.npy',allow_pickle='TRUE').item()

model = load_model('TC.h5')


# In[79]:


st.title('Toxic Comment Filter')
st.write('Discussing things you care about can be difficult.' 
         'The threat of abuse and harassment online means that many people stop expressing themselves and',
         'give up on seeking different opinions. Platforms struggle to effectively facilitate conversations,',
         'leading many communities to limit or completely shut down user comments.')
st.write('This application helps in detecting toxic comments. This was developed on the comments from Wikipedia’s talk page edits.')
user_input = st.text_input("Enter your comment here",'good application though.')


# In[81]:


arr = np.zeros((1,30))
i = 0
unknown = 0

doc = nlp(user_input)

for token in doc:
    if token.is_stop == False:
 
        low_txt = token.text.lower()

        if str(low_txt) in w2s:
            
            arr[0][i] = w2s[low_txt]
            i = i + 1
        else:
            st.write('The word',token,'was not found in the dictionary')
            unknown = 1
            
if unknown == 0:       
    
    toxicity = model.predict(arr)
    tox = str(int(round(toxicity[0][0] * 10)))
    if toxicity > 0.5:
        st.write("This comment is predicted to be an hate comment. On a toxic scale of 1 to 10 this comment rates",tox)
    else:
        st.write("This comment is predicted to be hate free.")
        
if unknown == 1:
    st.write("Try again.")

