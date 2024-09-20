import components as comp
import constants as value
import streamlit as st


def gte_page():

    comp.create_gap(1)

    comp.section_topic("Become a Teacher")

    comp.infomation_package_description([value.DESC_GTE])

    comp.create_gap(1)

    col1, col2, col3, col4, col5 = st.columns([1, 10, 10, 10, 1])

    with col2:
        st.image(value.GTE_1)

    with col3:
        st.image(value.GTE_3)

    with col4:
        st.image(value.GTE_6)

    col6, col7, col8, col9, col10 = st.columns([1, 10, 10, 10, 1])

    with col7:
        st.image(value.GTE_8)

    with col8:
        st.image(value.GTE_5)

    with col9:
        st.image(value.GTE_8)

    col11, col12, col13, col14, col15 = st.columns([1, 10, 10, 10, 1])

    with col12:
        st.image(value.GTE_7)

    with col13:
        st.image(value.GTE_2)
