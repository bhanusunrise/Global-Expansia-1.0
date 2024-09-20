import components as comp
import constants as value
import streamlit as st


def gv_page():

    comp.create_gap(1)

    comp.section_topic("Volunteering Opportunities")

    comp.infomation_package_description(value.DESC_GV)

    comp.create_gap(1)

    col1, col2, col3, col4, col5 = st.columns([1, 10, 10, 10, 1])

    with col2:
        st.image(value.GV_1)

    with col3:
        st.image(value.GV_2)

    with col4:
        st.image(value.GV_3)

    col6, col7, col8, col9, col10 = st.columns([1, 10, 10, 10, 1])

    with col7:
        st.image(value.GV_4)

    with col8:
        st.image(value.GV_16)

    with col9:
        st.image(value.GV_6)

    col11, col12, col13, col14, col15 = st.columns([1, 10, 10, 10, 1])

    with col12:
        st.image(value.GV_7)

    with col13:
        st.image(value.GV_8)

    with col14:
        st.image(value.GV_9)

    col15, col16, col17, col18, col19 = st.columns([1, 10, 10, 10, 1])

    with col16:
        st.image(value.GV_10)

    with col17:
        st.image(value.GV_11)

    with col18:
        st.image(value.GV_12)

    col20, col21, col22, col23, col24 = st.columns([1, 10, 10, 10, 1])

    with col21:
        st.image(value.GV_13)

    with col22:
        st.image(value.GV_14)

    with col23:
        st.image(value.GV_15)

    col25, col26, col27, col28, col29 = st.columns([1, 10, 10, 10, 1])

    with col27:
        st.image(value.GV_5)
