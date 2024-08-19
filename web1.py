import streamlit as st
import home as hm
import pages.about_event as event
import pages.about_aiesec as aiesec
import contacts as cnt
import gv as gv
import gta as gta
import gte as gte
import components as comp
import constants as value

st.set_page_config(page_title="Global Expansia",
                   page_icon=":earth_africa:", layout="wide")

page_bg_img = """
<style>
body {{
background-image: url("images/global_expansia_girl.jpg);
background-size: cover;
}}
</style>
"""

# Display the background image
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("""
<style>
    /*
	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
        white-space: pre-wrap;
		background-color: #003577;
		border-radius: 10px 10px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
        padding-left :10px;
        padding-right :10px;
        margin:2px;
        font-size : 20px; !important
    }*/
    
    .stTabs :hover{
        color: #F0F0F0 !important;
    }


	.stTabs [aria-selected="true"] {
         color: #E8E8E8;
	}
 
    .stTabs [aria-selected="true"] :hover {
        color: #E0E0E0;
	}
 
    [data-testid ="stAppViewContainer"] {
        background-image:url("images/global_expansia_girl.jpg");
        background-size:cover;
    }
</style>""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    ["Home", "About Global Expansia", "About AIESEC", "Global Volunteer", "Global Talent", "Global Teacher", "Contact Us"])

with tab1:
    hm.home_page()

with tab2:
    event.event_page()

with tab3:
    aiesec.aiesec_page()

with tab4:
    gv.gv_page()

with tab5:
    gta.gta_page()

with tab6:
    gte.gte_page()

with tab7:
    cnt.contacts_page()


comp.create_gap(3)

st.divider()

col1, col2, col3 = st.columns([1, 20, 1])


with col2:
    st.image(value.FOOTER)

st.markdown(
    """
    <div style='text-align:center'>
        <p style='font-size: 15px; color: #FFFFFF;'>
            <b>Developed by :</b> Global Expansia Organizing Committee - AIESEC in University of Kelaniya
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
