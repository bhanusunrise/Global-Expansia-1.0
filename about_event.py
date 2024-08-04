import components as comp
import constants as value
import streamlit as st
import time as timer


def event_page():

    comp.create_gap(1)

    col1, col2, col3 = st.columns([1, 9, 1])
    with col2:
        comp.infomation_package("What is Global Expansia?", ["Global Expansia, an event organized by AIESEC at the University of Kelaniya, focuses on abroad internships and volunteering opportunities. We create a platform for young people to gain valuable cultural experiences and develop their skills internationally. We connect young people from different nations, providing them with the chance to speak with opportunity providers abroad in a selection of countries they're interested in. Through these conversations, they will gain valuable insights into where they can best invest their skills."])

    comp.create_gap(3)

    col4, col5, col6 = st.columns([1, 9, 1])
    with col5:
        comp.infomation_package("It's all about exchanges", [
                                "An exchange program is an international experience that allows young people to develop their leadership potential and gain valuable skills. This can be achieved through volunteering or professional internships abroad. It's a transformative experience that goes far beyond simply visiting another country. It's about personal growth, cultural immersion, and contributing to positive change on a global scale."])

    comp.create_gap(3)

    comp.section_topic("Let's see some our exchange experiances")
    comp.create_gap(1)

    col7, col8, col9 = st.columns([1, 9, 1])
    with col8:
        st.video("https://youtu.be/BvnFN2Ab-oQ?si=KfiKRGC-20TpaI92")

    comp.create_gap(2)

    col10, col11, col12, col13 = st.columns([1, 4, 4, 1])
    with col11:
        with col11:
            comp.infomation_package_quote("\"Worthy and an unforgettable experience full of learning and challenges.\"", [
                "\"I worked with the renowned German Language Institute : Boosteno in the city of Gabes, South of Tunisia. The project was highly successful since I could fulfil all my expectations and goals set before departure. I had a really great time with the students and could initiate a lot of projects together. Apart from work, I got the chance to travel all around Tunisia from north to south and from azure beaches to sandy deserts.\""])

        with col12:
            comp.infomation_package_quote("\"An incredible adventure filled with unforgettable experiences and lifelong friendships.\"", [
                                          "\"Deciding to go on an internship in India was one of the best decisions I've ever made. India was incredibly welcoming, and the people I met made me feel right at home. I always value experience over qualifications, and my videographer internship in India looks impressive on my CV and makes for an interesting discussion in interviews.\""])
