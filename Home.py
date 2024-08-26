import streamlit as st
import components as comp
import constants as value
import time


st.set_page_config(page_title="Global Expansia",
                   page_icon=":earth_africa:", layout="wide")

col1, col2, col3 = st.columns([1, 9, 1])

with col2:

    st.image(value.EVENT_LOGO, caption="", width=20, use_column_width="always",
             clamp="", channels="RGB", output_format="auto")

    comp.create_gap(2)

    col19, col20 = st.columns([7, 5])

    with col19:
        comp.infomation_package(" ", [
            value.EVENT_DESCRIPTION_HOME
        ])

    with col20:
        st.image(value.FIRE_LOGO)
    comp.create_gap(2)

    st.video(value.FLYER_7_VIDEO,
             loop=False, autoplay=False, muted=False)

    # comp.create_gap(2)

    # comp.section_topic("Event Timeline")

    # comp.timeline_image_changer()

    comp.create_gap(3)

    comp.see_more_button(
        "https://globalexpansia.streamlit.app/About_Global_Expansia")

    comp.create_gap(3)

    comp.section_topic("Our Partners")

    comp.create_gap(1)

    col21, col22, col23 = st.columns([4, 3, 4,])

    with col22:

        comp.partner(value.CHARANA_LOGO, "Official Electronic Media Partner")

    comp.create_gap(3)

    col4, col5 = st.columns([5, 7])

    with col4:
        st.image(value.AIESEC_MAN_WALKING)

    with col5:
        comp.infomation_package("Get to Know AIESEC", ["We are a global, youth-led organization that strives to achieve Peace and Fulfillment of Humankind's Potential by engaging and developing every young person in the world with our unique Leadership Development Model.",
                                                       "Our values guide us in our everyday behavior to encourage finding new solutions and ideas for current world issues. We believe that young people learn best by doing and reflecting. AIESEC enables young people to learn the most from every experience."])

    comp.create_gap(1)

    col6, col7 = st.columns([1, 1])

    with col6:
        st.video(value.CN_LDS_VIDEO)
        comp.infomation_package_description(
            ["Leadership Development Seminar 2023"])

    with col7:
        st.video(value.CN_AWRUDU_VIDEO)
        comp.infomation_package_description(["CN Awurudu 2024"])

    comp.create_gap(3)

    comp.infomation_package("Unlocking Potential with Exchange Programs", [
        "An exchange program is an international experience that enables young people to develop their leadership potential and enhance their personal branding. Through volunteering or professional internships abroad, participants gain valuable skills and undergo significant personal growth. This transformative experience extends beyond merely visiting another country; it involves deep cultural engagement and contributing to positive global change, all while building a strong, unique personal brand."])

    comp.create_gap(3)

    comp.section_topic("Some of them ...")

    st.video("https://youtu.be/BvnFN2Ab-oQ?si=KfiKRGC-20TpaI92")

    comp.create_gap(1)

    col8, col9 = st.columns([1, 1])

    with col8:
        comp.infomation_package_quote("\"Worthy and an Unforgettable Experience Full of Learning and Challenges.\"", [
            "\"I worked with the renowned German Language Institute : Boosteno in the city of Gabes, South of Tunisia. The project was highly successful since I could fulfil all my expectations and goals set before departure. I had a really great time with the students and could initiate a lot of projects together. Apart from work, I got the chance to travel all around Tunisia from north to south and from azure beaches to sandy deserts.\""])

    with col9:
        comp.infomation_package_quote("\"An Incredible Adventure Filled with Unforgettable Experiences and Lifelong Friendships.\"", [
            "\"Deciding to go on an internship in India was one of the best decisions I've ever made. India was incredibly welcoming, and the people I met made me feel right at home. I always value experience over qualifications, and my videographer internship in India looks impressive on my CV and makes for an interesting discussion in interviews.\""])

    comp.create_gap(3)

    comp.see_more_button(
        "https://global-expansia-test.streamlit.app/about_aiesec")

    comp.create_gap(3)

    comp.section_topic("FAQ")

    comp.create_gap(1)

    comp.frequently_asked_questions(
        value.QUESTION_1, value.ANSWER_1, None)

    comp.frequently_asked_questions(
        value.QUESTION_2, value.ANSWER_2, value.LINK_2)
    comp.frequently_asked_questions(value.QUESTION_3, value.ANSWER_3, None)
    comp.frequently_asked_questions(value.QUESTION_4, value.ANSWER_4, None)
    comp.frequently_asked_questions(value.QUESTION_5, value.ANSWER_5, None)

    comp.create_gap(3)

    comp.section_topic("Meet Our Team")

col10, col11, col12, col13, col14 = st.columns([1, 2, 2, 2, 1])

with col12:
    comp.contact_section(value.UMAYANGI_NAME, value.UMAYANGI_POSITION,
                         value.UMAYANGI_EMAIL, value.UMAYANGI_CONTACT_NO, value.UMAYANGI_IMAGE)

comp.create_gap(1)

col15, col16, col17, col18, col19 = st.columns([1, 2, 2, 2, 1])

with col16:
    comp.contact_section(value.NADUNI_NAME, value.NADUNI_POSITION,
                         value.NADUNI_EMAIL, value.NADUNI_CONTACT_NO, value.NADUNI_IMAGE)

with col17:
    comp.contact_section(value.ASNA_NAME, value.ASNA_POSITION,
                         value.ASNA_EMAIL, value.ASNA_CONTACT_NO, value.ASNA_IMAGE)

with col18:
    comp.contact_section(value.THISHYA_NAME, value.THISHYA_POSITION,
                         value.THISHYA_EMAIL, value.THISHYA_CONTACT_NO, value.THISHYA_IMAGE)

comp.create_gap(3)
comp.see_more_button(
    "https://globalexpansia.streamlit.app/Contact_Us")

comp.create_gap(1)

comp.register_now_button()
comp.footer()
