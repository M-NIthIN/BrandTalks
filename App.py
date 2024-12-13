import streamlit as st
import pandas as pd
import json
from wordcloud import WordCloud
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Dummy Data Loading, ideally calling dag?
with open("youtube_dummy.json", "r") as file:
    transformed_data = json.load(file)

# Streamlit Config
st.set_page_config(page_title="BrandTalks", page_icon="📊", layout="wide")
st.title("BrandTalks")
st.subheader("Capturing Brand-related info across social platforms.")

brand_name = st.text_input("Enter Brand Name", value="Brand X", placeholder="Type here...")
if st.button("Search") or brand_name.strip():

    # Youtube
    with st.expander("", expanded = False, icon="▶️"):

        st.subheader(f"YouTube - {brand_name} - Media Card")
        # sentiment analysis
        line_data = []
        for video in transformed_data["videos"]:
            for point in video["sentiment_over_time"]:
                line_data.append({
                    "timestamp": point["timestamp"],
                    "sentiment_score": point["sentiment_score"],
                    "video_id": video["video_id"]
                })
        df_line = pd.DataFrame(line_data)
        col1, col2, col3 = st.columns([7, 1, 2])
        with col1:
            st.markdown(f"<h5>Sentimental Analysis over time</h5>", unsafe_allow_html=True)
            fig = px.line(
                df_line,
                x="timestamp",
                y="sentiment_score",
                color="video_id",
                labels={"video_id": "Video ID", "timestamp": "Timestamp (s)", "sentiment_score": "Sentiment Score"},
            )
            fig.update_layout(legend_title="Videos", height=600)
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            selected_video = st.selectbox(
                "Video ID", options=["All"] + [v["video_id"] for v in transformed_data["videos"]]
            )
        with col3:
            if selected_video != "All":
                video = next(v for v in transformed_data["videos"] if v["video_id"] == selected_video)
                stats = {
                    "Views": video["views"],
                    "Likes": video["likes"],
                    "Comments": video["comments"],
                    "Sentiment Score": video["sentiment_score"],
                    "Engagement Ratio": video["engagement_ratio"],
                }
            else:
                stats = {
                    "Views": transformed_data["total_views"],
                    "Likes": transformed_data["total_likes"],
                    "Comments": transformed_data["total_comments"],
                    "Sentiment Score": round(transformed_data["sentiment_score"], 2),
                    "Engagement Ratio": transformed_data["engagement_ratio"],
                }
            cols = st.columns(2)
            cols[0].markdown(f"<h5>Views</h5><p>{stats['Views']}</p>", unsafe_allow_html=True)
            cols[1].markdown(f"<h5>Likes</h5><p>{stats['Likes']}</p>", unsafe_allow_html=True)
            cols[0].markdown(f"<h5>Comments</h5><p>{stats['Comments']}</p>", unsafe_allow_html=True)
            cols[1].markdown(f"<h5>Sentiment Score</h5><p>{stats['Sentiment Score']}</p>", unsafe_allow_html=True)
            cols[0].markdown(f"<h5>Engagement Ratio</h5><p>{stats['Engagement Ratio']}</p>", unsafe_allow_html=True)
            
            with col3 or col2:
                statistics = stats
                statistics["Engagement Ratio"] *= statistics["Views"]
                statistics["Sentiment Score"] *= statistics["Views"]/100
                categories, values = map(list, zip(*statistics.items()))
                fig = go.Figure(data=[
                    go.Scatterpolar(
                        r=values,
                        theta=categories,
                        fill='toself',
                        name= selected_video if selected_video != "All" else 'Total Stats',
                        line=dict(color='#f5b7b1')
                    )
                ]).update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, max(values) * 1.15]
                        ),
                         angularaxis=dict(
                            tickvals=categories,
                            ticktext=[
                                "Views", 
                                "Likes", 
                                "Comments", 
                                "Sentiment <br> Score", 
                                "Engagement <br> Ratio"
                            ]
                        )
                    ),
                    showlegend=False,
                    width = 349,
                    height = 350)
                st.plotly_chart(fig,use_container_width=True)


            # Summary and Word Cloud
        col1, col2 = st.columns([7, 3])
        if selected_video == "All":
            summary_text = transformed_data["overall_summary"]
            word_cloud_data = transformed_data["total_word_cloud"]
        else:
            summary_text = video["summary"]
            word_cloud_data = video["word_cloud"]
        with col1:
            st.markdown(f"<h5>Summary</h5>", unsafe_allow_html=True)
            st.text(summary_text)
        with col2:
            wordcloud = WordCloud(width=200, height=100, background_color="white").generate_from_frequencies(word_cloud_data)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)

    with st.expander("", expanded = True, icon="🤖"):
        st.subheader(f"Reddit - {brand_name} - Media Card")

    with st.expander("", expanded = False, icon="📰"):
        st.subheader(f"News - {brand_name} - Media Card")

    with st.expander("", expanded = False, icon="📷"):
        st.subheader(f"instagram - {brand_name} - Media Card")

    with st.expander("", expanded = False, icon="❎"):
        st.subheader(f"twitter - {brand_name} - Media Card")

