# -*- coding: utf-8 -*-
"""Dataset 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RHW4qsQ1uMWHhJ6IF1clBMYZ0_brywfo
"""

import pandas as pd
import numpy as np
import streamlit as st


import pickle

svm_classifier_loaded = pickle.load('/svm_classifier_saved')

naive_bayes_loaded = pickle.load('/naive_bayes_saved')

random_forest_classifier_loaded = pickle.load('/random_forest_classifier_saved')


def main():
    st.title("Simple Streamlit Application")

    # Input area
    user_input = st.text_area("Enter your text here:", "")

    # Button to trigger processing
    if st.button("Submit"):
        # Call a function to process the user input (you can replace this with your own logic)
        result1 = svm_classifier_saved(user_input)
        result2 = naive_bayes_saved(user_input)
        # Display the result
        st.text("Output svm classifier:")
        st.write(result1)
        st.text("Output naive bayes:")
        st.write(result2)

if __name__ == "__main__":
    main()
