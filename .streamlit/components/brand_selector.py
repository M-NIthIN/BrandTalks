 
import streamlit as st

def brand_selector():
    """
    A simple search bar for selecting a brand.
    Returns the entered brand name.
    """
    st.sidebar.title("Brand Selector")
    brand_name = st.sidebar.text_input("Enter a Brand Name:", "")
    return brand_name
