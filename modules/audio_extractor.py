from moviepy.editor import VideoFileClip

def extract_audio(input_path, output_path):

    clip = VideoFileClip(input_path)

    clip.audio.write_audiofile(output_path)

    clip.close()
