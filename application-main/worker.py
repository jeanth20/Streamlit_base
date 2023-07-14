import streamlit as st
import os
import time
import numpy as np


def one():
    st.title(":flag-za: One function")
    st.title(":do_not_litter:")
    st.write(":flag-za:")

def two():
    st.title(":flag-za: Two function")


def three():
    st.title(":flag-za: Three function")


def four():
    st.title(":flag-za: Four function")

def contact_form():
    st.title("Contact form")
    left_column, right_column = st.columns(2)
    
    with left_column:
        name_first = st.text_input('First name')
        name_last = st.text_input('Last name')
        id_number = st.text_input('ID number')

    with right_column:
        gender = st.radio('Gender', ['Female','Male'])
        email = st.text_input('Email address')
        phone = st.text_input('Phone number')
    

    st.text_area('Text to translate')
    st.camera_input("Take a picture")

    st.checkbox('I agree')    
    st.button('Submit')
