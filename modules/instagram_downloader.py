import yt_dlp


def download_instagram_video(url, output_path):

    ydl_opts = {
        'outtmpl': output_path,
        'format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        ydl.download([url])
