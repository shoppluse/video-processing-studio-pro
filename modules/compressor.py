from moviepy.editor import VideoFileClip
import os

def compress_video(input_path, output_path, quality):

    clip = VideoFileClip(input_path)

    bitrate_map = {
        "Low": "300k",
        "Medium": "700k",
        "High": "1200k"
    }

    clip.write_videofile(
        output_path,
        bitrate=bitrate_map[quality],
        codec="libx264",
        audio_codec="aac"
    )

    clip.close()

    # FILE SIZE ANALYTICS
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(output_path)

    return original_size, compressed_size
