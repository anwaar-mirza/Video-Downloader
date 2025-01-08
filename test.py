import os
import tempfile
from yt_dlp import YoutubeDL
import streamlit as st

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

        # List the files in the temporary directory to verify if the download was successful
        downloaded_files = os.listdir(temp_dir)
        st.write("Files in temp directory:", downloaded_files)  # Debugging line

        # Find the video file in the temporary directory
        for file_name in downloaded_files:
            if file_name.endswith(".mp4"):  # Check if the file is a video
                return os.path.join(temp_dir, file_name)
        return None  # Return None if no video file is found

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

        # List the files in the temporary directory to verify if the download was successful
        downloaded_files = os.listdir(temp_dir)
        st.write("Files in temp directory:", downloaded_files)  # Debugging line

        # Find the video file in the temporary directory
        for file_name in downloaded_files:
            if file_name.endswith(".mp4"):  # Check if the file is a video
                return os.path.join(temp_dir, file_name)
        return None  # Return None if no video file is found

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
            if video_path:
                st.write("Video Downloaded Successfully.")
                with open(video_path, "rb") as f:
                    st.download_button("Download Video", data=f, file_name="facebook_video.mp4", mime="video/mp4")
            else:
                st.error("Video download failed.")
else:
    if select.lower() not in url and url != "":
        st.error(f"It's not a {select} URL")
    else:
        if url and st.button("Download"):
            with st.spinner("Downloading in progress..."):
                video_path = download_instagram_reel(url)
            if video_path:
                st.write("Video Downloaded Successfully.")
                with open(video_path, "rb") as f:
                    st.download_button("Download Video", data=f, file_name="instagram_video.mp4", mime="video/mp4")
            else:
                st.error("Video download failed.")
