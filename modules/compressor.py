from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path):

    clip = VideoFileClip(input_path)

    clip.write_videofile(
        output_path,
        bitrate="500k",
        codec="libx264",
        audio_codec="aac"
    )

    clip.close()
