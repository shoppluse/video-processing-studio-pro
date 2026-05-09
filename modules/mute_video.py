from moviepy.editor import VideoFileClip

def mute_video(input_path, output_path):

    clip = VideoFileClip(input_path)

    muted = clip.without_audio()

    muted.write_videofile(
        output_path,
        codec="libx264"
    )

    clip.close()
