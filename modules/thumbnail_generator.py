import cv2

def generate_thumbnail(video_path, output_path):

    cap = cv2.VideoCapture(video_path)

    ret, frame = cap.read()

    if ret:
        cv2.imwrite(output_path, frame)

    cap.release()
