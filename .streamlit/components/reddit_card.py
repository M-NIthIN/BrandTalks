 
import streamlit as st
import random

def get_reddit_data(brand_name):
    """Generates dummy Reddit data for the given brand."""
    return {
        "title": f"{brand_name} on Reddit",
        "posts": random.randint(50, 500),
        "upvotes": random.randint(100, 10000),
        "comments": random.randint(50, 2000),
        "sentiment": random.uniform(-1, 1),
    }

def reddit_card(data):
    """Renders the Reddit media card."""
    st.subheader("Reddit")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**{data['title']}**")
        st.write(f"**Total Posts:** {data['posts']:,}")
        st.write(f"**Upvotes:** {data['upvotes']:,}")
        st.write(f"**Comments:** {data['comments']:,}")
        st.write(f"**Sentiment:** {data['sentiment']:.2f}")
