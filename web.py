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

    comp.timeline_image_changer()

    comp.create_gap(3)

    col4, col5 = st.columns([5, 7])

    with col4:
        st.image(value.AIESEC_LOGO)

    with col5:
        comp.infomation_package("Get to Know AIESEC", ["We are a global, youth-led organization that strives to achieve Peace and Fulfillment of Humankind's Potential by engaging and developing every young person in the world with our unique Leadership Development Model.",
                                                       "Our values guide us in our everyday behavior to encourage finding new solutions and ideas for current world issues. We believe that young people learn best by doing and reflecting. AIESEC enables young people to learn the most from every experience."])
