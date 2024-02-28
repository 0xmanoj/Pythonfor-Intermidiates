import cv2
import numpy as np

# Load the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Load the emotion classes
emotions = ["anger", "disgust", "fear", "happy", "sadness", "surprise", "neutral"]

# Load the model
model = tf.keras.models.load_model('model.h5')

# Define the function for detecting and analyzing emotions
def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        roi = np.expand_dims(roi_gray, axis=0) / 255.0
        preds = model.predict(roi)
        emotion = emotions[np.argmax(preds[0])]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame

# Start the video stream
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = detect_emotion(frame)
    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
