from yt_dlp import YoutubeDL
import streamlit as st
import os
import tempfile

def download_instagram_reel(url):
    # Create a temporary directory to store the downloaded video
    with tempfile.TemporaryDirectory() as tmpdirname:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": f"{tmpdirname}/%(title)s.%(ext)s",
            "extractor_args": {
                "Instagram": {"use_video": True}
            }
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Get the downloaded video file path
        downloaded_files = os.listdir(tmpdirname)
        video_files = [f for f in downloaded_files if f.endswith(('.mp4', '.mkv', '.avi'))]
        if not video_files:
            raise FileNotFoundError("No video file was downloaded")
        
        video_file = video_files[0]  # Assuming the first video is the correct one
        video_path = os.path.join(tmpdirname, video_file)
        
        return video_path

def download_facebook_reel(url):
    # Create a temporary directory to store the downloaded video
    with tempfile.TemporaryDirectory() as tmpdirname:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": f"{tmpdirname}/%(title)s.%(ext)s",
            "force_generic_extractor": True,
            "extractor_args": {
                "Facebook": {"use_video": True}
            }
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Get the downloaded video file path
        downloaded_files = os.listdir(tmpdirname)
        video_files = [f for f in downloaded_files if f.endswith(('.mp4', '.mkv', '.avi'))]
        if not video_files:
            raise FileNotFoundError("No video file was downloaded")
        
        video_file = video_files[0]  # Assuming the first video is the correct one
        video_path = os.path.join(tmpdirname, video_file)
        
        return video_path


select = st.radio("Select Platform", ["Facebook", "Instagram", "Tiktok", "Youtube"])

if select == "Facebook":
    url = st.text_input(f"Enter {select} URL")
    if "facebook" not in url and url != "":
        st.error("It's not a Facebook URL")
    else:
        if url != "" and st.button("Download"):
            with st.spinner("Downloading in progress..."):
                video_path = download_facebook_reel(url)
                with open(video_path, "rb") as video_file:
                    st.download_button(
                        label="Download Video",
                        data=video_file,
                        file_name=os.path.basename(video_path),
                        mime="video/mp4"
                    )
            st.write("Successfully Download")

else:
    url = st.text_input(f"Enter {select} URL")
    if select.lower() not in url and url != "":
        st.error(f"It's not a {select} URL")
    else:
        if url is not None and st.button("Download"):
            with st.spinner("Downloading in progress..."):
                video_path = download_instagram_reel(url)
                with open(video_path, "rb") as video_file:
                    st.download_button(
                        label="Download Video",
                        data=video_file,
                        file_name=os.path.basename(video_path),
                        mime="video/mp4"
                    )
            st.write("Successfully Download")

