import streamlit as st
from components.youtube_card import get_youtube_data, youtube_card
from components.reddit_card import get_reddit_data, reddit_card
from components.news_card import get_news_data, news_card
from components.twitter_card import get_twitter_data, twitter_card

# Set the page configuration and ensure layout is full width
st.set_page_config(page_title="BrandTalks", page_icon="📊", layout="wide")

def main():
    # Title and Caption
    st.title("BrandTalks - Social Media Analytics")
    st.caption("Capturing Brand-related info across social platforms")

    # Search Bar
    brand_name = st.text_input("Enter a Brand Name", placeholder="Search for a brand (e.g., Tesla, Nike, etc.)")

    if brand_name.strip():
        # Show brand name as header
        st.markdown(f"### Results for Brand: **{brand_name}**")
        st.write("---")  # Horizontal divider

        # Media Cards (Stacked One Below the Other)
        youtube_data = get_youtube_data(brand_name)
        youtube_card(youtube_data)

        reddit_data = get_reddit_data(brand_name)
        reddit_card(reddit_data)

        news_data = get_news_data(brand_name)
        news_card(news_data)

        twitter_data = get_twitter_data(brand_name)
        twitter_card(twitter_data)

if __name__ == "__main__":
    main()
