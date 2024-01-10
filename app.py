import streamlit as st

import utils

st.set_page_config(
    page_title="OLX rent",
    page_icon="icon.png"
)
st.title("OLX rent")

option = st.selectbox(
    "Choose file",
    (utils.get_file_names_startswith_olx())
)

if option:
    st.header(f"You choose {option} file")
    df = utils.get_dataframe_from_file(option)
    st.dataframe(df)
