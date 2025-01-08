from yt_dlp import YoutubeDL
import streamlit as st
import os

def download_instagram_reel(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "extractor_args": {
            "Instagram": {"use_video": True}
        }
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_facebook_reel(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "force_generic_extractor": True,
        "extractor_args": {
            "Instagram": {"use_video": True}
        }
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Create downloads directory if it doesn't exist
if not os.path.exists("downloads"):
    os.makedirs("downloads")

select = st.radio("Select Platform", ["Facebook", "Instagram", "Tiktok", "Youtube"])
url = st.text_input(f"Enter {select} URL")

if select == "Facebook":
    if "facebook" not in url and url != "":
        st.error("It's not a Facebook URL")
    else:
        if url and st.button("Download"):
            with st.spinner("Downloading in progress..."): 
                download_facebook_reel(url)
            st.success("Video Downloaded Successfully!")
            # List downloaded files
            files = os.listdir("downloads")
            for file in files:
                if file.endswith(('.mp4', '.mkv', '.webm')):  # Check for video files
                    st.download_button(label=f"Download {file}", data=open(f"downloads/{file}", "rb"), file_name=file)

else:
    if select.lower() not in url and url != "":
        st.error(f"It's not a {select} URL")
    else:
        if url and st.button("Download"):
            with st.spinner("Downloading in progress..."): 
                download_instagram_reel(url)
            st.success("Video Downloaded Successfully!")
            # List downloaded files
            files = os.listdir("downloads")
            for file in files:
                if file.endswith(('.mp4', '.mkv', '.webm')):  # Check for video files
                    st.download_button(label=f"Download {file}", data=open(f"downloads/{file}", "rb"), file_name=file)
