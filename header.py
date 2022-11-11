import streamlit as st
from PIL import Image
import yaml
import time
import asyncio


### Load configuration
@st.experimental_memo
def load_config():
    with open('config.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

config = load_config()

# TODO: async 문제 해결
async def toastMessage(msg, style='warning', wait=3):
    placeholder = st.empty()
    if style == "success":
        placeholder.success(msg)
    elif style == "info":
        placeholder.info(msg)
    elif style == "warning":
        placeholder.warning(msg)
    elif style == "error":
        placeholder.error(msg)
    else:
        placeholder.exception(msg)
    await asyncio.sleep(wait)
    #time.sleep(wait)
    placeholder.empty()

def page_header():
    # Site Settings
    if "site_settings" not in st.session_state:
        st.session_state.site_settings = True
        favicon_path = config['favicon_path']
        favicon = Image.open(favicon_path)
        st.set_page_config(page_title = "Mask Wearing Status Classification Competition Demonstration [CV-12] @ Boostcamp AI Tech 4th ",
                        page_icon = favicon,
                        layout = config['st_layout'],
                        initial_sidebar_state = "expanded"
                        )
                    
    ### FontAwsome
    st.markdown('''
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
                ''', unsafe_allow_html=True)

    ### CSS
    st.markdown('''
                <style>
                .center {
                    text-align: center;
                }
                .subtitle {
                    font-size: 20px;
                }
                </style>
                ''', unsafe_allow_html=True)
    
    ### Hide Hamburger
    if config['hide_hamburger'] == True:
        hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden;}
                </style>
                """
        st.markdown(hide_menu_style, unsafe_allow_html=True)