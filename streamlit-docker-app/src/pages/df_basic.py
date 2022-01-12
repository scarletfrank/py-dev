import streamlit as st
import numpy as np
import pandas as pd


def app():
    dataframe = pd.DataFrame(
        np.random.randn(10, 7),
        columns=('col %d' % i for i in range(7)))

    st.dataframe(dataframe.style.highlight_max(axis=0))
