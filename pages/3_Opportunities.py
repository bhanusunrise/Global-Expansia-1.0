import components as comp
import streamlit as st
import constants as value
import gv as gv
import gta as gta
import gte as gte

# Center the entire content within a wide column
col100, col101, col102 = st.columns([1, 9, 1])

with col101:
    st.image(value.EVENT_LOGO, caption="", width=20, use_column_width="always",
             clamp="", channels="RGB", output_format="auto")

    comp.create_gap(2)

    # Create a new centered column layout for the tabs
    col103, col104, col105 = st.columns([1, 8, 1])

    with col104:
        tab1, tab2, tab3 = st.tabs(
            ["Volunteer Abroad", "Teach Abroad", "Intern Abroad"])

        with tab1:
            gv.gv_page()

        with tab2:
            gte.gte_page()

        with tab3:
            gta.gta_page()

    comp.create_gap(3)
    comp.register_now_button()
    comp.footer()
