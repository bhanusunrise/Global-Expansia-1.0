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

    st.video(value.FLYER_7_VIDEO,
             loop=False, autoplay=False, muted=False)

    # Embed YouTube video using IFrame with parameters to reduce branding
    video_url = "https://www.youtube.com/embed/Vz7Nj54Kxu4?si=ixDj3PxlxJD-fabN?rel=0&modestbranding=1&autohide=1"
    st.markdown(f'<iframe width="640" height="360" src="{video_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
                unsafe_allow_html=True)
