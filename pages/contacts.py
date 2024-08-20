import components as comp
import streamlit as st
import constants as value


def contacts_page():

    col100, col101, col102 = st.columns([1, 9, 1])

    with col101:

        st.image(value.EVENT_LOGO, caption="", width=20, use_column_width="always",
                 clamp="", channels="RGB", output_format="auto")

    comp.create_gap(2)

    comp.section_topic("Meet our team")

    comp.create_gap(1)

    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

    with col2:
        comp.contact_section(value.UMAYANGI_NAME, value.UMAYANGI_POSITION,
                             value.UMAYANGI_EMAIL, value.UMAYANGI_CONTACT_NO, value.UMAYANGI_IMAGE)
    with col3:
        comp.contact_section(value.ONNELA_NAME, value.ONNELA_POSITION,
                             value.ONNELA_EMAIL, value.ONNELA_CONTACT_NO, value.ONNELA_IMAGE)

    comp.create_gap(1)

    col6, col7, col8, col9, col10 = st.columns([1, 2, 2, 2, 1])

    with col7:
        comp.contact_section(value.NADUNI_NAME, value.NADUNI_POSITION,
                             value.NADUNI_EMAIL, value.NADUNI_CONTACT_NO, value.NADUNI_IMAGE)

    with col8:
        comp.contact_section(value.ASNA_NAME, value.ASNA_POSITION,
                             value.ASNA_EMAIL, value.ASNA_CONTACT_NO, value.ASNA_IMAGE)

    with col9:
        comp.contact_section(value.THISHYA_NAME, value.THISHYA_POSITION,
                             value.THISHYA_EMAIL, value.THISHYA_CONTACT_NO, value.THISHYA_IMAGE)
    comp.create_gap(1)

    col11, col12, col13, col14, col15 = st.columns([1, 2, 2, 2, 1])

    with col12:
        comp.contact_section(value.DANINDU_NAME, value.DANINDU_POSITION,
                             value.DANINDU_EMAIL, value.DANINDU_CONTACT_NO, value.DANINDU_IMAGE)

    with col13:
        comp.contact_section(value.GITHMI_NAME, value.GITHMI_POSITION,
                             value.GITHMI_EMAIL, value.GITHMI_CONTACT_NO, value.GITHMI_IMAGE)

    with col14:
        comp.contact_section(value.ROSHANA_NAME, value.ROSHANA_POSITION,
                             value.ROSHANA_EMAIL, value.ROSHANA_CONTACT_NO, value.ROSHANA_IMAGE)

    comp.create_gap(1)

    col16, col17, col18, col19, col20 = st.columns([1, 2, 2, 2, 1])

    with col17:
        comp.contact_section(value.PASINDU_NAME, value.PASINDU_POSITION,
                             value.PASINDU_EMAIL, value.PASINDU_CONTACT_NO, value.PASINDU_IMAGE)

    with col18:
        comp.contact_section(value.THARIDI_NAME, value.THARIDI_POSITION,
                             value.THARIDI_EMAIL, value.THARIDI_CONTACT_NO, value.THARIDI_IMAGE)

    with col19:
        comp.contact_section(value.HIRUSHAN_NAME, value.HIRUSHAN_POSITION,
                             value.HIRUSHAN_EMAIL, value.HIRUSHAN_CONTACT_NO, value.HIRUSHAN_IMAGE)

    comp.create_gap(1)

    col21, col22, col23, col24, col25 = st.columns([1, 2, 2, 2, 1])

    with col22:
        comp.contact_section(value.GEYATHI_NAME, value.GEYATHI_POSITION,
                             value.GEYATHI_EMAIL, value.GEYATHI_CONTACT_NO, value.GEYATHI_IMAGE)

    with col23:
        comp.contact_section(value.THEJANI_NAME, value.THEJANI_POSITION,
                             value.THEJANI_EMAIL, value.THEJANI_CONTACT_NO, value.THEJANI_IMAGE)

    with col24:
        comp.contact_section(value.SAFAA_NAME, value.SAFAA_POSITION,
                             value.SAFAA_EMAIL, value.SAFAA_CONTACT_NO, value.SAFAA_IMAGE)

    comp.create_gap(3)


contacts_page()
