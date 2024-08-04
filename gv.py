import components as comp
import constants as value
import streamlit as st


def gv_page():

    col1, col2, col3, col4, col5 = st.columns([1, 2.2, 2, 1])

    with col2:
        st.image(value.GV_1)

    with col3:
        st.image(value.GV_2)

    with col4:
        st.image(value.GV_3)
