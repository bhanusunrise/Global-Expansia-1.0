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

    st.markdown(
        """
        <iframe src="https://drive.google.com/file/d/Vz7Nj54Kxu4?si=3BuX9F31jbHX4PCb/preview" width="640" height="480" allow="autoplay" frameborder="0" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )
