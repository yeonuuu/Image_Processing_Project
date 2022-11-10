from filters import happy

def apply_filter(emotion, img_path):
    if (emotion == "Happy"):
        return happy(img_path)
    pass