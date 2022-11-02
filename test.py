# %%
import cv2 #imports opencv-python library
from keras.models import load_model
import numpy as np #imports numpy library and renames it np
import time #imports time module


model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0) #captures the webcam video frame by frame and set as cap object - 0 is the first camera
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

start = time.time()
end = time.time() + 5
while time.time() < end: 
    ret, frame = cap.read() #reads the video from the camera frame by frame
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) #resizes image(input image, size, interpolation)
    #resampling using pixel area relation
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame) #displays video in a window called frame
    
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'): #if q is pressed, the video feed ends
        break
    end = time.time()
print(start)     
print(end)
print(end - start)

cap.release()#After the loop release the cap object
cv2.destroyAllWindows()#Destroy all the windows

# %%
