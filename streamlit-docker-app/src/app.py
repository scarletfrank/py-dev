import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from mulitpage import MultiPage
# import your pages here
from pages import df_basic, df_plot

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Logo.jpg')
display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.columns(2)
col1.image(display, width = 300)
col2.title("Data Visualization Application")

# Add all your application here
app.add_page("Data Analysis",df_plot.app)
app.add_page("Machine Learning", df_basic.app)

# The main app
app.run()