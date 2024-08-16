import streamlit as st
import components as comp
import constants as value


# Page Config and title

st.set_page_config(page_title="Global Expansia",
                   page_icon=":earth_africa:", layout="wide")

col1, col2, col3 = st.columns([1, 9, 1])

with col2:

    st.image("images/10.png", caption="", width=20, use_column_width="always",
             clamp="", channels="RGB", output_format="auto")

    comp.infomation_package(" ", [
        "Global Expansia organized by AIESEC in University of Kelaniya, is an event focused on personal branding through global volunteering and internships. Our program includes online sessions designed to educate delegates about international volunteering and internship opportunities while helping them build a strong personal brand. The series culminates in a final physical event offering a unique chance to secure life-changing opportunities and enhance their personal brand on a global scale."
    ])
