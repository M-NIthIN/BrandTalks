import streamlit as st
from streamlit_components.youtube_card import youtube_card, get_youtube_data
from streamlit_components.reddit_card import reddit_card, get_reddit_data
from streamlit_components.news_card import news_card, get_news_data
from streamlit_components.twitter_card import twitter_card, get_twitter_data

# Set page config
st.set_page_config(page_title="BrandTalks", page_icon="📊", layout="wide")

def main():
    st.title("BrandTalks")
    st.caption("Capturing Brand-related info across social platforms")

    brand_name = st.text_input("Enter a Brand Name", placeholder="Search for a brand (e.g., Tesla, Nike, etc.)")

    if brand_name.strip():
        st.subheader(f"Social Media Analysis for {brand_name}")

        # Display media cards with dummy data
        
        youtube_card(get_youtube_data(brand_name))
        reddit_card(get_reddit_data(brand_name))
        news_card(get_news_data(brand_name))
        twitter_card(get_twitter_data(brand_name))

if __name__ == "__main__":
    main()
