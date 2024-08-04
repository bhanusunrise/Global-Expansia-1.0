import streamlit as st

import components as comp

import constants as value

# Create the standard details component


st.set_page_config(page_title="Global Expansia",
                   page_icon=":earth_africa:", layout="wide")

st.image("images/10.png", caption="", width=100, use_column_width="always",
         clamp="", channels="RGB", output_format="auto")

comp.nav_button("Let's Go", value.COLOR_PRIMARY, value.COLOR_WHITE, "home")


def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    comp.nav_button("Go to About Page", "#f63366", "white", "about")


def about_page():
    st.title("About Page")
    st.write("Welcome to the About Page!")
    comp.nav_button("Go to Home Page", "#f63366", "white", "home")


# Check the query parameters to determine the current page
page_params = st.query_params()
page = page_params("page", ["home"])[0]

if page == "about":
    about_page()
else:
    home_page()
