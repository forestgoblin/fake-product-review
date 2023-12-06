# -*- coding: utf-8 -*-

import pickle

svm_classifier_loaded = pickle.load(open('/main/svm_classifier_saved.pkl', 'rb'))

naive_bayes_loaded = pickle.load(open('/main/naive_bayes_saved.pkl', 'rb'))

def main():
    st.title("Simple Streamlit Application")
    user_input = st.text_area("Enter your text here:", "")


    if st.button("Submit"):
      
        result1 = svm_classifier_loaded(user_input)
        result2 = naive_bayes_loaded(user_input)
       
        st.text("Output svm classifier:")
        st.write(result1)
        st.text("Output naive bayes:")
        st.write(result2)

if __name__ == "__main__":
    main()
