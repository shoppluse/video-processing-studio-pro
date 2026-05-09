from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_videos(video1, video2, output_path):

    clip1 = VideoFileClip(video1)
    clip2 = VideoFileClip(video2)

    final = concatenate_videoclips([clip1, clip2])

    final.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    clip1.close()
    clip2.close()
