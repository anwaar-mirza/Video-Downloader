from yt_dlp import YoutubeDL
import streamlit as st
import os
import shutil

def download_instagram_reel(url, output_path='downloads/'):
    ydl_opts = {
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Save as "downloads/<title>.<ext>"
        'format': 'best',  # Download the best quality video
        'quiet': False,    # Show progress
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Ensure compatibility with ffmpeg
            'preferedformat': 'mp4',       # Convert to MP4 if not already
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
       

    
st.markdown("""<h1 style='text-align:center;'>Downloading Escape</h1>""", unsafe_allow_html=True)
st.markdown("""<p style='text-align:justify;'><strong>Downloading Escape</strong> is a user-friendly app that allows users to easily download videos from popular platforms like TikTok, YouTube, Instagram, and Facebook. By simply providing the URL of the video, users can instantly download high-quality video files for offline viewing. The app supports multiple platforms, making it a versatile tool for video download needs. Whether you're saving a TikTok reel, a YouTube video, or an Instagram or Facebook post, <strong>Downloading Escape</strong> provides a seamless, fast, and efficient way to grab your favorite videos.</p>""", unsafe_allow_html=True)
st.divider()
select = st.radio("Select Platform", ["Facebook", "Instagram", "Tiktok", "Youtube"])
url = st.text_input(f"Enter {select} URL", placeholder=f"Paste {select} URL Here...")
try:
    if select.lower() not in url and url != "":
        st.error(f"It's not a {select} URL")
    else:
        if url:
            with st.spinner("Downloading in progress..."): 
                info = download_instagram_reel(url=url)
            #file = os.listdir(dir_name)[0]
            if info.endswith(('.mp4', '.mkv', '.webm')):
                if st.download_button(label=f"Download {info}", data=open(f"{info}", "rb"), file_name={info}):
                    st.success("✅ Video Downloaded Successfully!")
            # shutil.rmtree(dir_name)
except Exception as e:
    st.error(e)
    st.error("OOPS! Enter a valid URL....")
