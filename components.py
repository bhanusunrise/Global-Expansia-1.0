import streamlit as st

# The following variables are defined for color values

# This component can display a title with a content.
# You have to pass component title and captions as parameters.


def infomation_package(component_title, component_captions):
    st.markdown(f"""
        <div style="text-align: center;">
            <h1>{component_title}</h1>
            {''.join(
                [f"<p style='text-align:center; font-size:20px'>{caption}</p>" for caption in component_captions])}
        </div>
    """, unsafe_allow_html=True)


def infomation_package_quote(component_title, component_captions):
    st.markdown(f"""
        <div style="text-align: center;">
            <h3><em>{component_title}</em></h3>
            {''.join(
                [f"<em><p style='text-align:center; font-size:20px'>{caption}</p></em>" for caption in component_captions])}
        </div>
    """, unsafe_allow_html=True)
# This component is responsible for create horizontal lines.
# You have to pass number of lines as a parameter.


def create_gap(number_of_lines):
    for i in range(number_of_lines):
        st.write("####")

# This button is used to navigate between pages.
# You have to pass button color, value and destination as parameters


def nav_button(inner_text, button_color, text_color, url):
    button_code = f"""
        <div style="display: flex; justify-content: center;">
        <button class="css-1cpxqw2 edgvbvh5" style="background-color: {button_color}; color: {text_color}; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;"><strong>{inner_text}</strong></button>
        </div>
    """
    st.markdown(button_code, unsafe_allow_html=True)

# This component is created to create functional links
# You have to pass the function name, color, description and image link


def functional_link(function_name, color, description, image_link):
    st.image(image_link, caption="", width=100, use_column_width="always",
             clamp="", channels="RGB", output_format="auto")

    topic_code = f"""
        <div style="text-align: center">
            <h4 style="color: {color}">{function_name}</h4>
        </div>"""
    st.markdown(topic_code, unsafe_allow_html=True)

    description_code = f"""
        <div style="text-align: center">
            {''.join(
        [f"<p style = 'text-align:center; font-size:20px'>{caption}</p>" for caption in description])}
        </div>"""
    st.markdown(description_code, unsafe_allow_html=True)

    st.markdown(f"""
                <center>
                    <button style="background-color:#003577; border-color: white; border-radius: 20px; padding-top: 10px; padding-left: 30px; padding-right: 30px; padding-bottom: 10px;">Sign Up Now</button>
                </center>
                """,
                unsafe_allow_html=True)


# This component is created to show a topic
# You have to pass the topic


def section_topic(heading):
    st.markdown(f"""
        <div style="text-align: center;">
            <h1>{heading}</h1>
        </div>
    """, unsafe_allow_html=True)

# This component is created to show contacts of each OC member
# You have to pass the name, position, email, phone number and image link


def contact_section(person_name, position, email, contact_number, image_link):
    if position != "President":
        position = "Vice President - " + position

    st.markdown(
        """
        <style>
        .contact-container {
            text-align: center;
            font-size:20px;
        }
        .topic-container {
          /*  border: 2px solid #FFFFFF;  /* Border color and thickness */
          /*  background-color: #003577;
          /*  border-radius: 10px;   */     /* Rounded corners */
            text-align: center;
            padding-top: 15px; 
            margin-bottom: 10px;
        }
        .contact-image {
            border-radius: 50%;  /* Make the image circular */
        }
        .contact-popover {
            text-align: center;
        }
        .contacts a {
            color: #FFFFFF !important;   /* Font color white */
            text-decoration: none !important; /* Remove underlines */
            font-size : 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image(image_link, width=100, use_column_width=True)

    st.markdown(f"""
        <div class='topic-container'>
            <p style="font-size: 25px; color: #FFFFFF;"><strong>{person_name}</strong></p>
        </div>

        <div class='contact-container'>
            <p style="font-size:20px">Organizing Committee<br/> {position}<br/> Global Expansia</p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("View Contact"):
        st.markdown(f"""
        <div class='contact-popover'>
            <p class="contacts"><a href="mailto:{email}">Email:<br/>{email}</a><br/><br/>
            <a href="tel:{contact_number}">Contact Number : <br>{contact_number}</a></p>
        </div>
        """, unsafe_allow_html=True)

# This component is created to display opportunity


def volunteer_opportunity(title, country, project_name, description):
    st.markdown(f"""
                <div style="padding: 10px"; border-radius: 3; border: 1px solid black;">
                    <div style="padding-top: 5px"; border-radius: 3; border: 1px solid black;">

                    </div>
                </div>
                """)


# This
