from matplotlib.pyplot import imread
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications.imagenet_utils import preprocess_input
import cv2
from tensorflow.keras.models import load_model
import numpy as np
import urllib.request


def get_alt_text(img_path):

    #img = image.load_img(img_path, target_size=(224, 224))

    #x = img.img_to_array(img)
    urllib.request.urlretrieve(img_path, 'model/image.jpg')
    img = cv2.imread('model/image.jpg')

    img = cv2.resize(img, (224, 224))

    x = np.expand_dims(img, axis=0)

    x = preprocess_input(x)



    # load model

    loaded_model = load_model('./model/model.h5')

    preds=loaded_model.predict(x)
    if preds[0][0]>preds[0][1] and preds[0][0]>preds[0][2]:
        return "Laptop"
    elif preds[0][1]>preds[0][2]:
        return "Smartphone"
    else:
        return "Television"


