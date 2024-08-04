import components as comp
import constants as value
import streamlit as st


def home_page():

    col12, col13, col14 = st.columns([1, 9, 1])

    with col13:

        comp.create_gap(1)

        st.image("images/10.png", caption="", width=20, use_column_width="always",
                 clamp="", channels="RGB", output_format="auto")

        comp.infomation_package(" ", [
            "Global Expansia is a transformative event series providing global volunteering and talent opportunities. Our program combines online, and physical awareness sessions designed to educate delegates about international volunteering and internship possibilities.",
            "The final event of Global Expansia is a physical event exclusively for confirmed participants eager to grab these life-changing opportunities."
        ])

    comp.create_gap(3)

    comp.section_topic("Opportunities")

    col1, col2, col3, col10, col11 = st.columns([1, 3, 3, 3, 1])

    with col2:
        comp.functional_link(value.TOPIC_GV, value.COLOR_AIESEC_GV,
                             [value.DESC_GV], value.LOGO_GV)

    with col3:
        comp.functional_link(value.TOPIC_GTA, value.COLOR_AIESEC_GTA, [
            value.DESC_GTA], value.LOGO_GTA)

    with col10:
        comp.functional_link(value.TOPIC_GTE, value.COLOR_AIESEC_GTE, [
            value.DESC_GTE], value.LOGO_GTE)

    comp.create_gap(3)

    comp.section_topic("Contact Us")

    col4, col5, col6, col17, col18 = st.columns([1, 2, 2, 2, 1])

    with col6:
        comp.contact_section(value.UMAYANGI_NAME, value.UMAYANGI_POSITION,
                             value.UMAYANGI_EMAIL, value.UMAYANGI_CONTACT_NO, value.UMAYANGI_IMAGE)

    comp.create_gap(1)

    col7, col8, col9 = st.columns([1, 10, 1])

    with col8:
        st.image(value.FOOTER)
