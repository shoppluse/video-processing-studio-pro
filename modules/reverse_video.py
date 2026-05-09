from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

def reverse_video(input_path, output_path):

    clip = VideoFileClip(input_path)

    reversed_clip = clip.fx(vfx.time_mirror)

    reversed_clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    clip.close()
