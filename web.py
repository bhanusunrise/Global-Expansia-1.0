import streamlit as st
import components as comp
import constants as value
import base64

# Page Config and title

st.set_page_config(page_title="Global Expansia",
                   page_icon=":earth_africa:", layout="wide")


@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64(value.EVENT_LOGO)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

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
