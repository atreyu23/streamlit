import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Primera aplicación chorras en Streamlit")
with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)