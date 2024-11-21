 
import streamlit as st
import random

def get_news_data(brand_name):
    """Generates dummy News API data for the given brand."""
    return {
        "title": f"{brand_name} in the News",
        "articles": random.randint(5, 30),
        "mentions": random.randint(50, 1000),
        "sentiment": random.uniform(-1, 1),
    }

def news_card(data):
    """Renders the News API media card."""
    st.subheader("News API")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**{data['title']}**")
        st.write(f"**Total Articles:** {data['articles']:,}")
        st.write(f"**Mentions:** {data['mentions']:,}")
        st.write(f"**Sentiment:** {data['sentiment']:.2f}")
