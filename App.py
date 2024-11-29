# import streamlit as st
# import pandas as pd
# import json
# from wordcloud import WordCloud
# import plotly.express as px
# import matplotlib.pyplot as plt

# # Dummy Data Loading
# with open("youtube_dummy.json", "r") as file:
#     transformed_data = json.load(file)

# # Streamlit Config
# st.set_page_config(page_title="BrandTalks", page_icon="📊", layout="wide")
# st.title("BrandTalks")
# st.subheader("Capturing Brand-related info across social platforms.")

# brand_name = st.text_input("Enter Brand Name", value="Brand X", placeholder="Type here...")
# if st.button("Search") or brand_name.strip():

#     # Define CSS for the red border
#     st.markdown(
#         """
#         <style>
#         .red-border {
#             border: 2px solid red;
#             border-radius: 15px;
#             padding: 20px;
#             margin: 10px 0;
#             background-color: #f9f9f9; /* Optional for better contrast */
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Container for the YouTube Media Card
#     with st.container():
#         # Add the red-border styling
#         st.markdown('<div class="red-border">', unsafe_allow_html=True)

#         # YouTube Media Card Header
#         st.subheader(f"YouTube - {transformed_data['brand_name']} - Media Card")

#         # Line Graph and Stats
#         line_data = []
#         for video in transformed_data["videos"]:
#             for point in video["sentiment_over_time"]:
#                 line_data.append({
#                     "timestamp": point["timestamp"],
#                     "sentiment_score": point["sentiment_score"],
#                     "video_id": video["video_id"]
#                 })
#         df_line = pd.DataFrame(line_data)

#         col1, col2 = st.columns([7, 3])
#         with col1:
#             st.markdown(f"<h5>Sentimental Analysis over time</h5>", unsafe_allow_html=True)
#             fig = px.line(
#                 df_line,
#                 x="timestamp",
#                 y="sentiment_score",
#                 color="video_id",
#                 labels={"video_id": "Video ID", "timestamp": "Timestamp (s)", "sentiment_score": "Sentiment Score"},
#             )
#             fig.update_layout(legend_title="Videos")
#             st.plotly_chart(fig, use_container_width=True)

#         with col2:
#             selected_video = st.selectbox(
#                 "Video ID", options=["All"] + [v["video_id"] for v in transformed_data["videos"]]
#             )

#             if selected_video != "All":
#                 video = next(v for v in transformed_data["videos"] if v["video_id"] == selected_video)
#                 stats = {
#                     "Views": video["views"],
#                     "Likes": video["likes"],
#                     "Comments": video["comments"],
#                     "Sentiment Score": video["sentiment_score"],
#                     "Engagement Ratio": video["engagement_ratio"],
#                 }
#             else:
#                 stats = {
#                     "Views": transformed_data["total_views"],
#                     "Likes": transformed_data["total_likes"],
#                     "Comments": transformed_data["total_comments"],
#                     "Sentiment Score": round(transformed_data["sentiment_score"], 2),
#                     "Engagement Ratio": transformed_data["engagement_ratio"],
#                 }

#             cols = st.columns(2)
#             cols[0].markdown(f"<h5>Views</h5><p>{stats['Views']}</p>", unsafe_allow_html=True)
#             cols[1].markdown(f"<h5>Likes</h5><p>{stats['Likes']}</p>", unsafe_allow_html=True)
#             cols[0].markdown(f"<h5>Comments</h5><p>{stats['Comments']}</p>", unsafe_allow_html=True)
#             cols[1].markdown(f"<h5>Sentiment Score</h5><p>{stats['Sentiment Score']}</p>", unsafe_allow_html=True)
#             cols[0].markdown(f"<h5>Engagement Ratio</h5><p>{stats['Engagement Ratio']}</p>", unsafe_allow_html=True)

#         # Summary and Word Cloud
#         col1, col2 = st.columns([7, 3])

#         if selected_video == "All":
#             summary_text = transformed_data["overall_summary"]
#             word_cloud_data = transformed_data["total_word_cloud"]
#         else:
#             summary_text = video["summary"]
#             word_cloud_data = video["word_cloud"]

#         with col1:
#             st.markdown(f"<h5>Summary</h5>", unsafe_allow_html=True)
#             st.text(summary_text)
#         with col2:
#             wordcloud = WordCloud(width=200, height=100, background_color="white").generate_from_frequencies(word_cloud_data)
#             fig, ax = plt.subplots()
#             ax.imshow(wordcloud, interpolation="bilinear")
#             ax.axis("off")
#             st.pyplot(fig)

#         # Close the red-border div
#         st.markdown('</div>', unsafe_allow_html=True)



import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# CSS for styling the red box with rounded corners
st.markdown(
    """
    <style>
    .red-box {
        background-color: #ffcccc;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        color: #333333;
        font-size: 16px;
        font-family: Arial, sans-serif;
        display: inline-block;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def create_graph():
    """Generate a sample sine graph."""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, label='sin(x)', color='blue')
    ax.set_title('Sample Graph')
    ax.legend()
    return fig

# Create a container that wraps both the graph and text

with st.container():
    # Add the red box around both the graph and the text

    # Display the graph inside the red box
    fig = create_graph()
    st.pyplot(fig, use_container_width=True)  # Display graph with full width

    # Display the descriptive text below the graph
    st.markdown(f"<div class='red-box'><img>{st.pyplot(fig)}</img>",
                  unsafe_allow_html=True)
    st.markdown(
        "<p>This graph demonstrates the sine function over a range of values from 0 to 10. "
        "The curve oscillates between -1 and 1, representing the periodic nature of sine.</p>",
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
