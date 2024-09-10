import components as comp
import streamlit as st
import constants as value
import gv as gv
import gta as gta
import gte as gte

with st.sidebar:
    comp.register_now_button()

col100, col101, col102 = st.columns([1, 9, 1])

with col101:
    st.image(value.EVENT_LOGO, caption="", width=20, use_column_width="always",
             clamp="", channels="RGB", output_format="auto")

    comp.create_gap(2)

    tab1, tab2, tab3 = st.tabs(
        ["Volunteer in Abroad", "Teach in Abroad", "Intern in Abroad"])

    with tab1:
        gv.gv_page()

    with tab2:
        gte.gte_page()

    with tab3:
        gta.gta_page()

    comp.create_gap(3)
    comp.register_now_button()
    comp.footer()
