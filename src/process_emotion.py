from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

def process_emotion(image_path):
    if not os.path.exists('model.h5'):
        return 'Model does not exist, you should train IA'
    classifier = load_model('model.h5')
    class_labels = ['Angry','Fear', 'Happy' ,'Neutral','Sad','Surprise']
    img = Image.open(image_path).convert('L').resize((48, 48), Image.ANTIALIAS)
    img = np.array(img)
    preds = classifier.predict(img[None,:,:])
    t = np.argmax(preds[0])
    return class_labels[t]