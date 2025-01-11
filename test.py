from yt_dlp import YoutubeDL
import streamlit as st
import os

def download_video(url, output_path='downloads/'):
    """
    Downloads a video from the given URL using yt-dlp.
    
    :param url: The video URL.
    :param output_path: The folder where the downloaded file will be saved.
    :return: The full path of the downloaded video.
    """
    ydl_opts = {
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Save as "<output_path>/<title>.<ext>"
        'format': 'best',  # Download the best quality video
        'quiet': True,     # Suppress console logs
    }

    # Ensure the output path exists
    os.makedirs(output_path, exist_ok=True)

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

# Streamlit App
st.markdown(
    """<h1 style='text-align:center;'>Downloading Escape</h1>""",
    unsafe_allow_html=True,
)
st.markdown(
    """<p style='text-align:justify;'><strong>Downloading Escape</strong> is a user-friendly app that allows users to easily download videos from popular platforms like TikTok, YouTube, Instagram, and Facebook. By simply providing the URL of the video, users can instantly download high-quality video files for offline viewing.</p>""",
    unsafe_allow_html=True,
)
st.divider()

# Platform selection
platforms = ["Facebook", "Instagram", "Tiktok", "Youtube"]
selected_platform = st.radio("Select Platform", platforms)

# URL input
url = st.text_input(
    f"Enter {selected_platform} URL",
    placeholder=f"Paste {selected_platform} URL Here..."
)

# Download button
if url:
    try:
        with st.spinner("Downloading in progress..."):
            video_path = download_video(url=url)

        # Provide a download button
        with open(video_path, "rb") as video_file:
            st.download_button(
                label="Download Video",
                data=video_file,
                file_name=os.path.basename(video_path),
                mime="video/mp4",
            )
        st.success("✅ Video Downloaded Successfully!")
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.error("OOPS! Please check the URL and try again.")
