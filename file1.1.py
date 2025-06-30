import cv2
import numpy as np
import face_recognition as fr
import time
import os
import csv
from datetime import datetime, timedelta

# --- Setup ---
video_capture = cv2.VideoCapture(0)

# Load and encode the known face
image = fr.load_image_file(r'C:\Users\aryak\OneDrive\Desktop\photo (1).jpg')
image_face_encoding = fr.face_encodings(image)[0]
known_face_encodings = [image_face_encoding]
known_faces_name = ["Arya Kant"]

# Attendance log dictionary
last_seen = {}

# Output folder for unknown faces
os.makedirs("UnknownFaces", exist_ok=True)

# CSV file for attendance
attendance_file = "attendance_log.csv"
if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Time"])

# Timer for FPS calculation
prev_time = time.time()

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    fc_locations = fr.face_locations(rgb_frame)
    fc_encodings = fr.face_encodings(rgb_frame, fc_locations)

    for (top, right, bottom, left), face_encoding in zip(fc_locations, fc_encodings):
        matches = fr.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        fc_distances = fr.face_distances(known_face_encodings, face_encoding)
        match_index = np.argmin(fc_distances)

        if matches[match_index]:
            name = known_faces_name[match_index]

            # Log attendance if not recently seen
            now = datetime.now()
            if name not in last_seen or now - last_seen[name] > timedelta(minutes=5):
                with open(attendance_file, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, now.strftime("%Y-%m-%d %H:%M:%S")])
                last_seen[name] = now
                print(f"✅ {name} logged at {now.strftime('%H:%M:%S')}")
        else:
            # Save unknown face as image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unknown_face = frame[top:bottom, left:right]
            cv2.imwrite(f"UnknownFaces/unknown_{timestamp}.jpg", unknown_face)

        # Draw box and name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0) if name != "Unknown" else (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0) if name != "Unknown" else (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Calculate and display FPS
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time)) if curr_time != prev_time else 0
    prev_time = curr_time
    cv2.putText(frame, f"FPS: {fps}", (10, 30), font, 0.8, (0, 255, 255), 2)

    # Show video frame
    cv2.imshow('Face Recognition System', frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
