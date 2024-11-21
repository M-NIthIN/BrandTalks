import streamlit as st
import random

def get_twitter_data(brand_name):
    """Generates dummy Twitter data for the given brand."""
    return {
        "title": f"{brand_name} on Twitter",
        "tweets": random.randint(200, 5000),
        "followers": random.randint(1000, 100000),
        "sentiment": random.uniform(-1, 1),
    }

def twitter_card(data):
    """Renders the Twitter media card."""
    st.subheader("Twitter")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**{data['title']}**")
        st.write(f"**Total Tweets:** {data['tweets']:,}")
        st.write(f"**Followers:** {data['followers']:,}")
        st.write(f"**Sentiment:** {data['sentiment']:.2f}")
