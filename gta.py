import components as comp
import constants as value
import streamlit as st


def gta_page():

    comp.create_gap(1)

    comp.section_topic("Internships")

    comp.infomation_package_description([value.DESC_GTA])

    comp.create_gap(1)

    col1, col2, col3, col4, col5 = st.columns([1, 10, 10, 10, 1])

    with col2:
        st.image(value.GTA_1)

    with col3:
        st.image(value.GTA_7)

    with col4:
        st.image(value.GTA_4)

    col6, col7, col8, col9, col10 = st.columns([1, 10, 10, 10, 1])

    with col7:
        st.image(value.GTA_5)

    with col8:
        st.image(value.GTA_8)

    with col9:
        st.image(value.GTA_3)
