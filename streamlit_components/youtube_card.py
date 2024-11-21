import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

# Dummy Data for YouTube Media Card (Replace with actual data fetching logic)
def get_youtube_data(brand_name):
    return {
        "title": f"YouTube {brand_name} Media Card",
        "description": "An overview of the brand's presence on YouTube, including views, likes, and comments.",
        "total_views": "1.2M",
        "total_likes": "35K",
        "total_comments": "2K",
        "engagement_ratio": "1.5%",
        "overall_sentiment": "Positive",
        "total_duration": "12 minutes",
        "sentiment_over_time": {
            "video1": np.random.uniform(0, 1, 100),  # Sentiment data for video1 (0 to 1 scale)
            "video2": np.random.uniform(0, 1, 100)   # Sentiment data for video2
        },
        "transcripts_summary": "This is a brief summary of the video content, highlighting key moments such as product launches and customer reactions.",
        "wordcloud_text": "brand, product, customer, launch, review, feedback, excellent, amazing, love, good, best"  # Sample words for word cloud
    }

# Function to create sentiment over time graph
def sentiment_graph_for_youtube(sentiment_data):
    plt.figure(figsize=(8, 4))
    for video, sentiment in sentiment_data.items():
        plt.plot(np.linspace(0, 100, len(sentiment)), sentiment, label=video)
    plt.title('Sentiment Over Time for Each Video')
    plt.xlabel('Time (Seconds)')
    plt.ylabel('Sentiment')
    plt.legend()
    st.pyplot(plt)

# Function to generate word cloud from the transcript
def generate_wordcloud_for_youtube(wordcloud_text):
    wordcloud = WordCloud(width=400, height=400, background_color="white").generate(wordcloud_text)
    plt.figure(figsize=(4, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

# Function to render the YouTube Media Card
def youtube_card(brand_name):
    # Fetch data using the dummy function
    data = get_youtube_data(brand_name)
    
    # CSS for the card's styling (rounded corners, shadow effect)
    st.markdown(
        """
        <style>
        .card {
            background-color: #f8f8f8;
            border-radius: 15px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 20px;
        }
        .card-header {
            font-size: 1.5em;
            font-weight: bold;
            color: #333;
        }
        .card-content {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .graph-stats-container {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            margin-top: 20px;
        }
        .graph-container {
            flex: 7; /* 70% width */
            padding-right: 20px;
        }
        .stats-container {
            flex: 3; /* 30% width */
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 10px;
        }
        .summary-wordcloud-container {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            margin-top: 20px;
        }
        .summary-container {
            flex: 8; /* 80% width */
        }
        .wordcloud-container {
            flex: 3; /* 20% width */
            padding-left: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    with st.container():
        # Card Header
        st.markdown(f"<div class='card'><div class='card-header'>{data['title']}</div>", unsafe_allow_html=True)

        # Card Content (Sentiment Graph + Stats)
        st.markdown("<div class='card-content'>", unsafe_allow_html=True)
        
        # Graph and Stats Container
        st.markdown("<div class='graph-stats-container'>", unsafe_allow_html=True)
        
        # Sentiment Graph (70%)
        st.markdown("<div class='graph-container'>", unsafe_allow_html=True)
        st.subheader("Sentiment Over Time")
        sentiment_graph_for_youtube(data["sentiment_over_time"])
        st.markdown("</div>", unsafe_allow_html=True)

        # Stats (30%)
        st.markdown("<div class='stats-container'>", unsafe_allow_html=True)
        st.subheader("Engagement Stats")
        st.write(f"**Total Views:** {data['total_views']}")
        st.write(f"**Total Likes:** {data['total_likes']}")
        st.write(f"**Total Comments:** {data['total_comments']}")
        st.write(f"**Engagement Ratio:** {data['engagement_ratio']}")
        st.write(f"**Overall Sentiment:** {data['overall_sentiment']}")
        st.write(f"**Total Duration:** {data['total_duration']}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Summary and Word Cloud Container
        st.markdown("<div class='summary-wordcloud-container'>", unsafe_allow_html=True)
        
        # Summary (80%)
        st.markdown("<div class='summary-container'>", unsafe_allow_html=True)
        st.subheader("Transcript Summary")
        st.write(data['transcripts_summary'])
        st.markdown("</div>", unsafe_allow_html=True)

        # Word Cloud (20%)
        st.markdown("<div class='wordcloud-container'>", unsafe_allow_html=True)
        st.subheader("Word Cloud from Transcript")
        generate_wordcloud_for_youtube(data["wordcloud_text"])
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        
        # Closing the card div
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # A small horizontal line for card separation
        st.markdown("<hr>", unsafe_allow_html=True)
