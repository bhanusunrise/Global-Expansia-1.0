import components as comp
import constants as value
import streamlit as st
import time as timer


def event_page():

    comp.create_gap(1)

    col1, col2, col3 = st.columns([1, 9, 1])
    with col2:
        comp.infomation_package("What is Global Expansia?", ["Global Expansia mainly focuses on personal branding through the transformative impact of international internships and volunteering. The event offers youth the chance to embrace diverse cultures and develop their talents on a global scale. By connecting nations, we provide young people with opportunities to engage with international opportunity providers, helping them gain insights into how they can strategically invest their skills and build a strong personal brand that stands out in the global arena."])

    comp.create_gap(3)

    col4, col5, col6 = st.columns([1, 9, 1])
    with col5:
        comp.infomation_package("Unlocking Potential with Exchange Programs", [
                                "An exchange program is an international experience that enables young people to develop their leadership potential and enhance their personal branding. Through volunteering or professional internships abroad, participants gain valuable skills and undergo significant personal growth. This transformative experience extends beyond merely visiting another country; it involves deep cultural engagement and contributing to positive global change, all while building a strong, unique personal brand."])

    comp.create_gap(3)

    comp.section_topic("Let's See Some of Our Exchange Experiances")
    comp.create_gap(1)

    col7, col8, col9 = st.columns([1, 9, 1])
    with col8:
        st.video("https://youtu.be/BvnFN2Ab-oQ?si=KfiKRGC-20TpaI92")

    comp.create_gap(2)

    col10, col11, col12, col13 = st.columns([1, 4, 4, 1])
    with col11:
        with col11:
            comp.infomation_package_quote("\"Worthy and an Unforgettable Experience Full of Learning and Challenges.\"", [
                "\"I worked with the renowned German Language Institute : Boosteno in the city of Gabes, South of Tunisia. The project was highly successful since I could fulfil all my expectations and goals set before departure. I had a really great time with the students and could initiate a lot of projects together. Apart from work, I got the chance to travel all around Tunisia from north to south and from azure beaches to sandy deserts.\""])

        with col12:
            comp.infomation_package_quote("\"An Incredible Adventure Filled with Unforgettable Experiences and Lifelong Friendships.\"", [
                                          "\"Deciding to go on an internship in India was one of the best decisions I've ever made. India was incredibly welcoming, and the people I met made me feel right at home. I always value experience over qualifications, and my videographer internship in India looks impressive on my CV and makes for an interesting discussion in interviews.\""])


event_page()
