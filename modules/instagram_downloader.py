import yt_dlp
import glob
import os


def download_instagram_video(url):

    # REMOVE OLD FILES
    old_files = glob.glob("outputs/instagram_*")

    for file in old_files:
        os.remove(file)

    ydl_opts = {
        'outtmpl': 'outputs/instagram_%(id)s.%(ext)s',
        'format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        ydl.download([url])

    files = glob.glob("outputs/instagram_*")

    return files[0]
