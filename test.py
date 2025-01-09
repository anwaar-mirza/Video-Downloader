from yt_dlp import YoutubeDL
import streamlit as st
import os
import shutil

# Function to download Instagram reels
def download_instagram_reel(url):
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegMerger",
            },
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Function to download Facebook reels
def download_facebook_reel(url):
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "force_generic_extractor": True,
        "postprocessors": [
            {
                "key": "FFmpegMerger",
            },
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Ensure the downloads directory exists
dir_name = "downloads"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

# Streamlit configuration
st.set_page_config(
    page_title="Downloading Escape",
    page_icon="📥",
    layout="wide",
    initial_sidebar_state="auto",
)

# Streamlit UI setup
st.title("Downloading Escape")
st.header("Your One-Stop Solution for Seamless Video Downloads!")
st.divider()
select = st.radio("Select Platform", ["Facebook", "Instagram", "Tiktok", "Youtube"])
url = st.text_input(f"Enter {select} URL", placeholder=f"Paste {select} URL Here...")



try:
    if select == "Facebook":
        if "facebook" not in url and url != "":
            st.error("It's not a Facebook URL")
        else:
            if url:
                with st.spinner("Downloading in progress..."): 
                    download_facebook_reel(url)
                file = os.listdir(dir_name)[0]
                if file.endswith(('.mp4', '.mkv', '.webm')):
                    if st.download_button(label=f"Download {file}", data=open(f"{dir_name}/{file}", "rb"), file_name=file):
                        st.success("✅ Video Downloaded Successfully!")
                shutil.rmtree(dir_name)


    else:
        if select.lower() not in url and url != "":
            st.error(f"It's not a {select} URL")
        else:
            if url:
                with st.spinner("Downloading in progress..."): 
                    download_instagram_reel(url)

                file = os.listdir(dir_name)[0]
                if file.endswith(('.mp4', '.mkv', '.webm')):
                    if st.download_button(label=f"Download {file}", data=open(f"{dir_name}/{file}", "rb"), file_name=file):
                        st.success("✅ Video Downloaded Successfully!")
                shutil.rmtree(dir_name)
except Exception as e:
    st.error(e)
    st.error("OOPS! Enter a valid URL....")


#ok done
