import streamlit as st
from streamlit_option_menu import option_menu
from jinja2 import Environment, FileSystemLoader
import numpy as np
import pandas as pd
import os
import worker as worker


with st.sidebar:
    selected = option_menu(
        menu_title="Select a function",
        menu_icon=":flag-za:",
        options=["1", "2", "3", "4"],
        icons=["music-note-list", "archive-fill", "credit-card-2-front-fill", "play-btn-fill"],
        default_index=0
    )

if selected == "1":
    worker.one()

elif selected == "2":
    worker.two()

elif selected == "3":
    worker.three()
    
elif selected == "4":
    worker.four()
