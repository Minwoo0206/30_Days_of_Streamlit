import streamlit as st
import pandas as pd
import requests
from streamlit_option_menu import option_menu
from streamlit_tags import st_tags, st_tags_sidebar
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode
from dashboard_utils.gui import keyboard_to_url
from dashboard_utils.gui import load_keyboard_class

if "widen" not in st.session_state:
    layout = "centered"
else:
    layout = "wide" if st.session_state.widen else "centered"

st.set_page_config(layout=layout, page_title="Zero-Shot Text Classifier", page_icon="🤗")

load_keyboard_class()

if not "valid_inputs_received" in st.session_state:
    st.session_state["valid_inputs_received"] = False

c1, c2 = st.columns([0.4, 2])