This Python script implements a real-time face recognition system using OpenCV and the face_recognition library. The program begins by loading a known face image and encoding it to create a reference for comparison. It then continuously captures frames from the webcam and processes each frame to detect and recognize faces.

Detected faces are compared against the known encodings using facial distance measurements. If a match is found, the system displays the person's name with a bounding box on the video feed. If no match is found, the detected face is marked as "Unknown" and automatically saved as an image in a designated folder for later review.

To make the system practical for attendance tracking, it logs recognized faces into a CSV file with the current timestamp. To avoid duplicate logging, it uses a 5-minute cooldown timer for each person. The script also calculates and displays the current frames per second (FPS) on the video feed for performance monitoring.

The system is designed to be simple, efficient, and easy to extend, with applications in automated attendance systems, security checks, or personal recognition tools.
