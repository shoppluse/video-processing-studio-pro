import speech_recognition as sr

from deep_translator import GoogleTranslator

from gtts import gTTS

from moviepy.editor import VideoFileClip, AudioFileClip

import os


def convert_language(input_video, target_language, output_video):

    try:

        # TEMP FILES
        audio_path = "outputs/temp_audio.wav"

        translated_audio = "outputs/translated_audio.mp3"

        # EXTRACT AUDIO
        video = VideoFileClip(input_video)

        video.audio.write_audiofile(audio_path)

        # SPEECH RECOGNITION
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_path) as source:

            audio_data = recognizer.record(source)

            text = recognizer.recognize_google(audio_data)

        # TRANSLATION
        translated_text = GoogleTranslator(
            source='auto',
            target=target_language
        ).translate(text)

        # TEXT TO SPEECH
        tts = gTTS(
            text=translated_text,
            lang=target_language
        )

        tts.save(translated_audio)

        # MERGE NEW AUDIO
        new_audio = AudioFileClip(translated_audio)

        final_video = video.set_audio(new_audio)

        final_video.write_videofile(
            output_video,
            codec="libx264",
            audio_codec="aac"
        )

        # CLEANUP
        video.close()
        new_audio.close()

        os.remove(audio_path)

        return translated_text, None

    except sr.RequestError:

        return None, "Speech recognition service unavailable."

    except sr.UnknownValueError:

        return None, "Could not understand audio clearly."

    except Exception as e:

        return None, str(e)
