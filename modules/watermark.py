from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_watermark(input_path, text, output_path):

    video = VideoFileClip(input_path)

    watermark = TextClip(
        text,
        fontsize=30,
        color='white'
    ).set_duration(video.duration)

    watermark = watermark.set_pos(("right", "bottom"))

    final = CompositeVideoClip([video, watermark])

    final.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    video.close()
