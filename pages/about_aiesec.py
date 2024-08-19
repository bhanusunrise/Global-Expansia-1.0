import components as comp
import constants as value
import streamlit as st
import time as timer


def aiesec_page():

    comp.create_gap(1)

    col1, col2, col3 = st.columns([1, 9, 1])
    with col2:
        comp.infomation_package("What is AIESEC?", ["We are a global, youth-led organization that strives to achieve Peace and Fulfillment of Humankind's Potential by engaging and developing every young person in the world with our unique Leadership Development Model.",
                                "Our values guide us in our everyday behavior to encourage finding new solutions and ideas for current world issues. We believe that young people learn best by doing and reflecting. AIESEC enables young people to learn the most from every experience."])

    col4, col5, col6 = st.columns([4, 4, 4])
    with col5:
        st.image(value.AIESEC_LOGO)

    comp.create_gap(3)

    col7, col8, col9 = st.columns([1, 9, 1])
    with col8:
        comp.infomation_package("AIESEC in Sri Lanka", ["Our values guide us in our everyday behavior to encourage finding new solutions and ideas for current world issues. We believe that young people learn best by doing and reflecting. AIESEC enables young people to learn the most from every experience.",
                                "The organization is entrusted by many national and multinational organizations to help them gain access to youth opinion, approach top-talents for future recruitment, strengthen their image among youth and position themselves as socially responsible businesses by investing in youth leadership development."])

    comp.create_gap(1)

    col10, col11, col12, col13 = st.columns([1, 4, 4, 1])
    with col11:
        st.video("https://youtu.be/u56wqcSAaSU?si=95sAVBu_eL8GUvXD")

    with col12:
        st.video("https://youtu.be/oyIUvlRPfbo?si=CAgzRJo5WX7LKj8w")

    comp.create_gap(3)

    col14, col15, col16 = st.columns([1, 9, 1])
    with col15:
        comp.infomation_package("AIESEC in University of Kelaniya", [
                                "AIESEC in University of Kelaniya focuses on developing future leaders with a history of over 20 years starting operations since 1998. We as an organization shape our members' leadership attributes by encouraging active participation in volunteer efforts and other impactful activities. Beyond the local context, we also provide opportunities for youth to volunteer and intern overseas, gaining global exposure in the process."])

    comp.create_gap(1)

    col17, col18, col19, col20, col21 = st.columns([1, 3, 3, 3, 1])
    with col18:
        st.video("https://youtu.be/mkc-1LS9AkQ?si=ahvmpbwvi7wOFBiO")
    with col19:
        st.video("https://youtu.be/mY9z2PIN6nw?si=-yX9xGLgs6B0TlAB")
    with col20:
        st.video("https://youtu.be/4lT0ZttP7F8?si=ZDlLTvvAXhy__Ejx")


aiesec_page()
