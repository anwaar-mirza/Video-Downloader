from yt_dlp import YoutubeDL
import streamlit as st
import os
import shutil

def download_instagram_reel(url):
   ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",  # Prefer mp4 format
    "outtmpl": "downloads/%(title)s.%(ext)s",  # Set output template
    "postprocessors": [
        {
            "key": "FFmpegMerger",  # Merge audio and video streams into a single file
        },
        {
            "key": "FFmpegVideoConvertor",  # Ensure the final file is in mp4 format
            "preferedformat": "mp4",
        }
    ],
}

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_facebook_reel(url):
    ydl_opts = {
      "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",  # Prefer mp4 format
      "outtmpl": "downloads/%(title)s.%(ext)s",
      "force_generic_extractor": True,
       "postprocessors": [
        {
            "key": "FFmpegMerger",  # Merge audio and video streams into a single file
        },
        {
            "key": "FFmpegVideoConvertor",  # Ensure the final file is in mp4 format
            "preferedformat": "mp4",
        }
    ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

dir_name = "downloads"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; padding-bottom:30px;">
    <img src="data:image/png;base64,{}" width="100" height="100" style="margin-left: 10px; margin-top:25px">
    <h1 style="text-align: center; margin-right:95px;">Downloading Escape</h1>
</div>
""".format(base64.b64encode(open("insta.png", "rb").read()).decode()), unsafe_allow_html=True)
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
except:
    st.error("OOPS! Enter a valid URL....")



#ok done
