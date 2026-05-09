import streamlit as st
import os
import glob

from modules.cutter import cut_video
from modules.gif_converter import convert_to_gif
from modules.frame_extractor import extract_frames
from modules.format_converter import convert_format
from modules.speed_controller import change_speed
from modules.metadata import get_metadata
from modules.audio_extractor import extract_audio
from modules.compressor import compress_video
from modules.watermark import add_watermark
from modules.reverse_video import reverse_video
from modules.mute_video import mute_video
from modules.thumbnail_generator import generate_thumbnail
from modules.filters import apply_filter
from modules.language_converter import convert_language

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Video Processing Studio Pro",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom right, #050816, #0f172a);
    color: white;
}

.hero {
    padding: 40px;
    border-radius: 25px;
    background: linear-gradient(135deg, #7c3aed, #2563eb);
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0px 0px 25px rgba(0,0,0,0.4);
}

.hero h1 {
    color: white;
    font-size: 55px;
    margin-bottom: 10px;
}

.hero p {
    color: #e2e8f0;
    font-size: 20px;
}

.feature-card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 0px 20px rgba(255,255,255,0.08);
    margin-bottom: 20px;
}

.metric-box {
    background: linear-gradient(135deg,#1e293b,#111827);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
}

.metric-box h2 {
    color: #38bdf8;
    margin: 0;
}

.metric-box p {
    color: #cbd5e1;
    font-size: 18px;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3.2em;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    color: white;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# CREATE FOLDERS
# =====================================================

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero">
    <h1>🎬 Video Processing Studio Pro</h1>
    <p>Professional Multimedia Processing Platform</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("⚡ Features")

feature = st.sidebar.radio(
    "Choose Tool",
    [
        "✂️ Video Cutter",
        "🎞️ GIF Converter",
        "🖼️ Frame Extractor",
        "🔄 Format Converter",
        "⏩ Speed Controller",
        "📊 Metadata Viewer",
        "🔊 Audio Extractor",
        "📦 Video Compressor",
        "🖊️ Watermark Tool",
        "🔄 Reverse Video",
        "🔇 Mute Video",
        "📸 Thumbnail Generator",
        "🎨 Video Filter",
        "🌐 Audio Language Converter"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Built using Python, Streamlit, MoviePy, OpenCV and FFmpeg"
)

# =====================================================
# FILE UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "📤 Upload Video",
    type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_file is not None:

    upload_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(upload_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Video Uploaded Successfully")

    # =====================================================
    # VIDEO PREVIEW
    # =====================================================

    st.markdown("## 🎥 Video Preview")

    st.video(upload_path)

    st.markdown("---")

    # =====================================================
    # VIDEO CUTTER
    # =====================================================

    if feature == "✂️ Video Cutter":

        st.header("✂️ Smart Video Cutter")

        col1, col2 = st.columns(2)

        with col1:
            start_time = st.number_input(
                "Start Time",
                min_value=0,
                value=0
            )

        with col2:
            end_time = st.number_input(
                "End Time",
                min_value=1,
                value=10
            )

        if st.button("🚀 Cut Video"):

            output_path = "outputs/cut_video.mp4"

            cut_video(
                upload_path,
                start_time,
                end_time,
                output_path
            )

            st.success("✅ Video Trimmed Successfully")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="cut_video.mp4"
                )

    # =====================================================
    # GIF CONVERTER
    # =====================================================

    elif feature == "🎞️ GIF Converter":

        st.header("🎞️ Video to GIF Converter")

        if st.button("⚡ Convert to GIF"):

            output_path = "outputs/output.gif"

            convert_to_gif(
                upload_path,
                output_path
            )

            st.success("✅ GIF Created Successfully")

            st.image(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download GIF",
                    file,
                    file_name="output.gif"
                )

    # =====================================================
    # FRAME EXTRACTOR
    # =====================================================

    elif feature == "🖼️ Frame Extractor":

        st.header("🖼️ Frame Extractor")

        interval = st.slider(
            "Frame Interval",
            10,
            100,
            30
        )

        if st.button("📸 Extract Frames"):

            extract_frames(
                upload_path,
                "outputs",
                interval
            )

            st.success("✅ Frames Extracted")

            frames = glob.glob("outputs/frame_*.jpg")

            cols = st.columns(3)

            for index, frame in enumerate(frames[:9]):

                with cols[index % 3]:
                    st.image(frame)

    # =====================================================
    # FORMAT CONVERTER
    # =====================================================

    elif feature == "🔄 Format Converter":

        st.header("🔄 Format Converter")

        format_choice = st.selectbox(
            "Choose Format",
            ["mp4", "avi"]
        )

        if st.button("🎬 Convert Format"):

            output_path = f"outputs/converted.{format_choice}"

            convert_format(
                upload_path,
                output_path
            )

            st.success("✅ Format Converted")

            if format_choice == "mp4":
                st.video(output_path)
            else:
                st.info("AVI file created successfully. Download to view.")

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Converted File",
                    file,
                    file_name=f"converted.{format_choice}"
                )

    # =====================================================
    # SPEED CONTROLLER
    # =====================================================

    elif feature == "⏩ Speed Controller":

        st.header("⏩ Speed Controller")

        speed = st.slider(
            "Speed Factor",
            0.5,
            3.0,
            1.0
        )

        if st.button("⚡ Apply Speed Change"):

            output_path = "outputs/speed_video.mp4"

            change_speed(
                upload_path,
                speed,
                output_path
            )

            st.success("✅ Speed Changed Successfully")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="speed_video.mp4"
                )

    # =====================================================
    # METADATA VIEWER
    # =====================================================

    elif feature == "📊 Metadata Viewer":

        st.header("📊 Video Metadata")

        data = get_metadata(upload_path)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="metric-box">
                <h2>{data['Duration']} s</h2>
                <p>Duration</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-box">
                <h2>{data['FPS']}</h2>
                <p>FPS</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-box">
                <h2>{data['Resolution'][0]} x {data['Resolution'][1]}</h2>
                <p>Resolution</p>
            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # AUDIO EXTRACTOR
    # =====================================================

    elif feature == "🔊 Audio Extractor":

        st.header("🔊 Audio Extractor")

        if st.button("🎵 Extract Audio"):

            output_path = "outputs/audio.mp3"

            extract_audio(
                upload_path,
                output_path
            )

            st.success("✅ Audio Extracted Successfully")

            st.audio(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Audio",
                    file,
                    file_name="audio.mp3"
                )

    # =====================================================
    # VIDEO COMPRESSOR
    # =====================================================

    elif feature == "📦 Video Compressor":

        st.header("📦 Video Compressor")

        quality = st.selectbox(
            "Choose Compression Level",
            ["Low", "Medium", "High"]
        )

        if st.button("⚡ Compress Video"):

            output_path = "outputs/compressed.mp4"

            original_size, compressed_size = compress_video(
                upload_path,
                output_path,
                quality
            )

            # SIZE CONVERSION
            original_mb = original_size / (1024 * 1024)
            compressed_mb = compressed_size / (1024 * 1024)

            # REDUCTION %
            reduction = (
                (original_size - compressed_size)
                / original_size
            ) * 100

            st.success("✅ Video Compressed Successfully")

            # VIDEO PREVIEW
            st.video(output_path)

            st.markdown("---")

            st.subheader("📊 Compression Analytics")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Original Size",
                    f"{original_mb:.2f} MB"
                )

            with col2:
                st.metric(
                    "Compressed Size",
                    f"{compressed_mb:.2f} MB"
                )

            with col3:
                st.metric(
                    "Reduction",
                    f"{reduction:.1f}%"
                )

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Compressed Video",
                    file,
                    file_name="compressed.mp4"
                )

    # =====================================================
    # WATERMARK TOOL
    # =====================================================

    elif feature == "🖊️ Watermark Tool":

        st.header("🖊️ Watermark Tool")

        watermark_text = st.text_input(
            "Enter Watermark Text",
            "VideoStudioPro"
        )

        if st.button("✨ Add Watermark"):

            output_path = "outputs/watermarked.mp4"

            add_watermark(
                upload_path,
                watermark_text,
                output_path
            )

            st.success("✅ Watermark Added")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="watermarked.mp4"
                )

    # =====================================================
    # REVERSE VIDEO
    # =====================================================

    elif feature == "🔄 Reverse Video":

        st.header("🔄 Reverse Video")

        if st.button("⏪ Reverse Video"):

            output_path = "outputs/reversed.mp4"

            reverse_video(
                upload_path,
                output_path
            )

            st.success("✅ Video Reversed")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="reversed.mp4"
                )

    # =====================================================
    # MUTE VIDEO
    # =====================================================

    elif feature == "🔇 Mute Video":

        st.header("🔇 Mute Video")

        if st.button("🔇 Remove Audio"):

            output_path = "outputs/muted.mp4"

            mute_video(
                upload_path,
                output_path
            )

            st.success("✅ Audio Removed")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="muted.mp4"
                )

    # =====================================================
    # THUMBNAIL GENERATOR
    # =====================================================

    elif feature == "📸 Thumbnail Generator":

        st.header("📸 Thumbnail Generator")

        if st.button("📸 Generate Thumbnail"):

            output_path = "outputs/thumbnail.jpg"

            generate_thumbnail(
                upload_path,
                output_path
            )

            st.success("✅ Thumbnail Generated")

            st.image(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Thumbnail",
                    file,
                    file_name="thumbnail.jpg"
                )

       # =====================================================
    # LANGUAGE CONVERTER
    # =====================================================

    elif feature == "🌐 Audio Language Converter":

        st.header("🌐 Audio Language Converter")

        language = st.selectbox(
            "Select Target Language",
            [
                "Hindi",
                "Kannada",
                "Tamil",
                "Telugu",
                "French"
            ]
        )

        if st.button("🎙️ Convert Language"):

            output_path = "outputs/translated_video.mp4"

            lang_code = {
                "Hindi": "hi",
                "Kannada": "kn",
                "Tamil": "ta",
                "Telugu": "te",
                "French": "fr"
            }[language]

            translated_text, error = convert_language(
                upload_path,
                lang_code,
                output_path
            )

            if error:

                st.error(error)

            else:

                st.success("✅ Language Converted Successfully")

                st.video(output_path)

                st.subheader("📝 Translated Text")

                st.write(translated_text)

                with open(output_path, "rb") as file:

                    st.download_button(
                        "⬇️ Download Translated Video",
                        file,
                        file_name="translated_video.mp4"
                    )

    # =====================================================
    # VIDEO FILTER
    # =====================================================

    elif feature == "🎨 Video Filter":

        st.header("🎨 Black & White Filter")

        if st.button("🎨 Apply Filter"):

            output_path = "outputs/filtered.mp4"

            apply_filter(
                upload_path,
                output_path
            )

            st.success("✅ Filter Applied")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="filtered.mp4"
                )

else:

    st.markdown("""
    <div class="feature-card">
        <h2>🚀 Welcome to Video Processing Studio Pro</h2>

        <p>
        Upload a video and access powerful multimedia tools.
        </p>

        <ul>
            <li>✂️ Video Trimming</li>
            <li>🎞️ GIF Conversion</li>
            <li>🖼️ Frame Extraction</li>
            <li>🔄 Format Conversion</li>
            <li>⏩ Speed Control</li>
            <li>📊 Metadata Viewer</li>
            <li>🔊 Audio Extraction</li>
            <li>📦 Video Compression</li>
            <li>🖊️ Watermarking</li>
            <li>🔄 Reverse Video</li>
            <li>🔇 Audio Removal</li>
            <li>📸 Thumbnail Generator</li>
            <li>🎨 Video Filters</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
