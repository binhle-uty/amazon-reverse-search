from google_img_source_search import ReverseImageSearcher
import streamlit as st
import numpy as np
from typing import Tuple
import plotly.express as px
from st_keyup import st_keyup

def get_reverse_search(image_url):
    rev_img_searcher = ReverseImageSearcher()
    res = rev_img_searcher.search(image_url)
    list_searched = []
    for search_item in res:
        if "amazon.com/" in str(search_item.page_url):
        #   print(f'Title: {search_item.page_title}')
        #   print(f'Site: {search_item.page_url}')
        #   print(f'Img: {search_item.image_url}\n')

          list_searched.append(search_item)

    return list_searched


st.markdown("# THE TOOLBOX FOR AMAZON REVERSE SEARCH")
st.markdown("## Author: Thanh-Binh Le")

def submit():
    st.session_state.my_text = st.session_state.inputpath_src
    st.session_state.inputpath_src = ""


col1, col2 = st.columns(2)

st.write("---")
with col1:
    col1.header("Image")
    path_src = st.text_input(
        "Please input the path of image",
        key="inputpath_src",
        on_change=submit
    )
    

if "my_text" not in st.session_state:
    st.session_state.my_text = ""

my_text = st.session_state.my_text

with col2:
    if my_text!="":
        st.image(my_text)


if my_text!="":
    list_searched = get_reverse_search(my_text)
    if len(list_searched) == 0:
        st.markdown("## No finding!")
    else:
        i = 1
        for search_item in list_searched:
            st.markdown(f"## Found: product {i}")
            st.write(search_item.page_title)
            st.write(search_item.page_url)
            st.image(search_item.image_url)
            st.write("---")
            i+=1
    
    