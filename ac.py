import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands and Drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Create a blank white image
canvas = np.ones((720, 1280, 3), dtype="uint8") * 255

drawing = False  # Variable to track if we are drawing
last_point = None  # Store the last drawn point for connecting lines

# Initialize webcam
cap = cv2.VideoCapture(0)

def detect_gesture(landmarks):
    thumb_tip = np.array([landmarks[mp_hands.HandLandmark.THUMB_TIP].x, landmarks[mp_hands.HandLandmark.THUMB_TIP].y])
    index_tip = np.array([landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y])
    distance = np.linalg.norm(thumb_tip - index_tip)
    
    if distance < 0.05:
        return "pinch"
    return "none"

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    canvas = cv2.resize(canvas, (w, h))  # Resize canvas to match webcam resolution
    
    # Process the frame for hand landmarks
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks.landmark)
            
            if gesture == "pinch":
                drawing = True
                index_finger = (int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w),
                                int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h))
                
                if last_point:
                    cv2.line(canvas, last_point, index_finger, (0, 0, 0), 5)
                last_point = index_finger
            else:
                drawing = False
                last_point = None

    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow("Air Canvas", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
