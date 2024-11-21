import streamlit as st

def get_youtube_data(brand_name):
    # Dummy Data for YouTube Media Card (Replace with actual data fetching logic)
    return {
        "title": f"Youtube Analytics for {brand_name}",
        "description": "A quick overview of the brand's presence on YouTube, including views, likes, and comments.",
        "views": "1.2M",
        "likes": "35K",
        "comments": "2K",
        "sentiment": "Positive",
        "duration": "12 minutes"
    }

def youtube_card(data):
    with st.container():
        st.markdown(f"#### {data['title']}")
        st.write(f"**Description:** {data['description']}")
        st.write(f"**Views:** {data['views']}")
        st.write(f"**Likes:** {data['likes']}")
        st.write(f"**Comments:** {data['comments']}")
        st.write(f"**Sentiment:** {data['sentiment']}")
        st.write(f"**Video Duration:** {data['duration']}")
        
        st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line for separation

