from filters.happy import happy
from filters.angry import angry
from filters.fear import fear
from filters.neutral import neutral
from filters.surprise import surprise
from filters.sad import sad
#from happy_mask import happy_face


def apply_filter(emotion, img_path, x, y, h, w):
    if emotion == "Happy":
        #img_path = happy_face(img_path)
        return happy(img_path)
    elif emotion == "Angry":
        return angry(img_path)
    elif emotion == "Fear":
        return fear(img_path)
    elif emotion == "Neutral":
        return neutral(img_path)
    elif emotion == "Sad":
        return sad(img_path, x, y, h, w)
    return surprise(img_path)
