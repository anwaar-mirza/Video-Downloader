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
        "quiet": True,  # Suppress output
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)  # Return the path of the downloaded file

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
        "quiet": True,  # Suppress output
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)  # Return the path of the downloaded file

# Ensure the downloads directory exists
dir_name = "downloads"
os.makedirs(dir_name, exist_ok=True)

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
                    file_path = download_facebook_reel(url)
                if os.path.exists(file_path):
                    file_name = os.path.basename(file_path)
                    if st.download_button(label=f"Download {file_name}", data=open(file_path, "rb"), file_name=file_name):
                        st.success("✅ Video Downloaded Successfully!")
                else:
                    st.error("Download failed. Please try again.")

    else:
        if select.lower() not in url and url != "":
            st.error(f"It's not a {select} URL")
        else:
            if url:
                with st.spinner("Downloading in progress..."): 
                    file_path = download_instagram_reel(url)
                if os.path.exists(file_path):
                    file_name = os.path.basename(file_path)
                    if st.download_button(label=f"Download {file_name}", data=open(file_path, "rb"), file_name=file_name):
                        st.success("✅ Video Downloaded Successfully!")
                else:
                    st.error("Download failed. Please try again.")

except Exception as e:
    st.error(e)
    st.error("OOPS! Enter a valid URL....")

# Clean
