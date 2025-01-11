from yt_dlp import YoutubeDL
import streamlit as st
import os

# Function to download Instagram reels
def download_instagram_reel(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegMerger",
        }],
        "outtmpl": "downloads/%(title)s.%(ext)s",
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)  # Return the path of the downloaded file

# Function to download Facebook reels
def download_facebook_reel(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "force_generic_extractor": True,
        "postprocessors": [{
            "key": "FFmpegMerger",
        }],
        "outtmpl": "downloads/%(title)s.%(ext)s",
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
    if url:
        if select == "Facebook" and "facebook" not in url:
            st.error("It's not a Facebook URL")
        elif select != "Facebook" and select.lower() not in url:
            st.error(f"It's not a {select} URL")
        else:
            with st.spinner("Downloading in progress..."):
                if select == "Facebook":
                    downloaded_file = download_facebook_reel(url)
                else:
                    downloaded_file = download_instagram_reel(url)

            if downloaded_file and os.path.exists(downloaded_file):
                file_name = os.path.basename(downloaded_file)
                with open(downloaded_file, "rb") as f:
                    st.download_button(
                        label=f"Download {file_name}",
                        data=f,
                        file_name=file_name,
                        mime="video/mp4",
                    )
                st.success("✅ Video Downloaded Successfully!")
except Exception as e:
    st.error(e)
    st.error("OOPS! Enter a valid URL...")

# Cleanup logic
if st.button("Clean Downloads"):
    if os.path.exists(dir_name):
        for file in os.listdir(dir_name):
            os.remove(os.path.join(dir_name, file))
        st.success("✅ Downloads folder cleaned!")
