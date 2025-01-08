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



st.markdown("""<h1 style='text-align:center;'>Downloading Escape</h1>""")
st.markdown("""<p style='justify-content:center;'><strong>Downloading Escape</strong> is a user-friendly app that allows users to easily download videos from popular platforms like TikTok, YouTube, Instagram, and Facebook. By simply providing the URL of the video, users can instantly download high-quality video files for offline viewing. The app supports multiple platforms, making it a versatile tool for video download needs. Whether you're saving a TikTok reel, a YouTube video, or an Instagram or Facebook post, **Downloading Escape** provides a seamless, fast, and efficient way to grab your favorite videos.</p>""")
select = st.radio("Select Platform", ["Facebook", "Instagram", "Tiktok", "Youtube"])
url = st.text_input(f"Enter {select} URL")

if select == "Facebook":
    if "facebook" not in url and url != "":
        st.error("It's not a Facebook URL")
    else:
        if url:
            with st.spinner("Downloading in progress..."): 
                download_facebook_reel(url)
            # List downloaded files
            # files = os.listdir("downloads")
            # for file in files:
            #     if file.endswith(('.mp4', '.mkv', '.webm')):  # Check for video files
            #         st.download_button(label=f"Download {file}", data=open(f"downloads/{file}", "rb"), file_name=file)
            file = os.listdir("downloads")[0]
            if file.endswith(('.mp4', '.mkv', '.webm')):  # Check for video files
                if st.download_button(label=f"Download {file}", data=open(f"downloads/{file}", "rb"), file_name=file):
                    st.success("✅ Video Downloaded Successfully!")


else:
    if select.lower() not in url and url != "":
        st.error(f"It's not a {select} URL")
    else:
        if url:
            with st.spinner("Downloading in progress..."): 
                download_instagram_reel(url)
            
            # List downloaded files
            file = os.listdir("downloads")[0]
            if file.endswith(('.mp4', '.mkv', '.webm')):  # Check for video files
                if st.download_button(label=f"Download {file}", data=open(f"downloads/{file}", "rb"), file_name=file):
                    st.success("✅ Video Downloaded Successfully!")
            # for file in files:
            #     if file.endswith(('.mp4', '.mkv', '.webm')):  # Check for video files
            #         st.download_button(label=f"Download {file}", data=open(f"downloads/{file}", "rb"), file_name=file)
