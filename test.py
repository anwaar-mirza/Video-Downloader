import os
from pathlib import Path
from yt_dlp import YoutubeDL
import streamlit as st
import tempfile

# Function to download Instagram reels
def download_instagram_reel(url):
    # Create a temporary directory to save the file
    with tempfile.TemporaryDirectory() as temp_dir:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),
            "extractor_args": {
                "Instagram": {"use_video": True}  # Forces usage of Instagram-specific extractor
            }
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Return the path to the downloaded file
        for file_name in os.listdir(temp_dir):
            if file_name.endswith(".mp4"):  # Check if the file is a video
                return os.path.join(temp_dir, file_name)

# Function to download Facebook reels
def download_facebook_reel(url):
    # Create a temporary directory to save the file
    with tempfile.TemporaryDirectory() as temp_dir:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),
            "force_generic_extractor": True,
            "extractor_args": {
                "Instagram": {"use_video": True}  # Forces usage of Instagram-specific extractor
            }
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Return the path to the downloaded file
        for file_name in os.listdir(temp_dir):
            if file_name.endswith(".mp4"):  # Check if the file is a video
                return os.path.join(temp_dir, file_name)

# Streamlit app
select = st.radio("Select Platform", ["Facebook", "Instagram", "Tiktok", "Youtube"])
url = st.text_input(f"Enter {select} URL")

if select == "Facebook":
    if "facebook" not in url and url != "":
        st.error("It's not a Facebook URL")
    else:
        if url and st.button("Download"):
            with st.spinner("Downloading in progress..."):
                video_path = download_facebook_reel(url)
            st.write("Video Downloaded Successfully.")
            
            # Provide the video file for download
            with open(video_path, "rb") as f:
                st.download_button("Download Video", data=f, file_name="facebook_video.mp4", mime="video/mp4")
else:
    if select.lower() not in url and url != "":
        st.error(f"It's not a {select} URL")
    else:
        if url and st.button("Download"):
            with st.spinner("Downloading in progress..."):
                video_path = download_instagram_reel(url)
            st.write("Video Downloaded Successfully.")
            
            # Provide the video file for download
            with open(video_path, "rb") as f:
                st.download_button("Download Video", data=f, file_name="instagram_video.mp4", mime="video/mp4")
