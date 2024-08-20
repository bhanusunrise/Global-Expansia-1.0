import components as comp
import streamlit as st
import constants as value


col100, col101, col102 = st.columns([1, 9, 1])

with col101:
    st.image(value.EVENT_LOGO, caption="", width=20, use_column_width="always",
             clamp="", channels="RGB", output_format="auto")
