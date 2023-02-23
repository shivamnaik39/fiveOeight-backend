from matplotlib.pyplot import imread

from matplotlib.pyplot import imshow

from tensorflow.keras.preprocessing import image

from tensorflow.keras.applications.imagenet_utils import decode_predictions

from tensorflow.keras.applications.imagenet_utils import preprocess_input
import cv2



 

img_path = ''


 

#img = image.load_img(img_path, target_size=(224, 224))

#x = img.img_to_array(img)


 

img = cv2.imread(img_path)

img = cv2.resize(img, (224, 224))


 

x = np.expand_dims(img, axis=0)

x = preprocess_input(x)


 

print('Input image shape:', x.shape)


 

my_image = imread(img_path)

imshow(my_image)

from tensorflow.keras.models import load_model

 

# load model

loaded_model = load_model('model.h5')

preds=loaded_model.predict(x)

preds