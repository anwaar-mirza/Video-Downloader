from yt_dlp import YoutubeDL
import streamlit as st

def download_instagram_reel(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        # "force_generic_extractor": True,
        "extractor_args": {
            "Instagram": {"use_video": True}  # Forces usage of Instagram-specific extractor
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
            "Instagram": {"use_video": True}  # Forces usage of Instagram-specific extractor
        }
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


select = st.radio("Select Platform", ["Facebook", "Instagram", "Tiktok", "Youtube"])
if select == "Facebook":
    url = st.text_input(f"Enter {select} URL")
    if "facebook" not in url and url is not "":
        st.error("Its not a Facebook URL")
    else:
        if url is not None and st.button("Download"):
            with st.spinner("Downloading in progress..."): 
                download_facebook_reel(url)
            st.write("Video Download Successfully.....")
else:
    url = st.text_input(f"Enter {select} URL")
    if select.lower() not in url and url is not "":
        st.error(f"Its not a {select} URL")
    else:
        if url is not None and st.button("Download"):
            with st.spinner("Downloading in progress..."): 
                download_instagram_reel(url)
            st.write("Video Download Successfully.....")

    