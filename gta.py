import components as comp
import constants as value
import streamlit as st


def gta_page():

    comp.create_gap(1)

    comp.section_topic("Internships")

    comp.create_gap(1)

    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

    with col2:
        st.image(value.GTA_1)
