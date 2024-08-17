import streamlit as st
import components as comp
import constants as value

# Page Config and title

st.set_page_config(page_title="Global Expansia",
                   page_icon=":earth_africa:", layout="wide")

col1, col2, col3 = st.columns([1, 9, 1])

with col2:

    st.image(value.EVENT_LOGO, caption="", width=20, use_column_width="always",
             clamp="", channels="RGB", output_format="auto")

    comp.infomation_package(" ", [
        value.EVENT_DESCRIPTION_HOME
    ])

    comp.create_gap(2)

    st.video(value.FLYER_7_VIDEO,
             loop=False, autoplay=False, muted=False)

    comp.create_gap(2)

    comp.section_topic("Event Timeline")
