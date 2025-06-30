🧠 Face Recognition Attendance System

This project is a real-time face recognition system built using Python, OpenCV, and the face_recognition library. It captures video from a webcam, detects faces in the frame, and identifies them by comparing with a set of known face encodings. Recognized faces are labeled on the screen, and their presence is logged with timestamps. Unrecognized faces are saved as images for future reference. The system is lightweight, efficient, and can be extended for use in attendance tracking, access control, or smart surveillance applications.

✨ Features
🔍 Real-time face detection and recognition using webcam

🏷️ Name labeling on detected faces

🗂️ Attendance logging with name and timestamp in a CSV file

🕐 Duplicate entry prevention (cooldown of 5 minutes per person)

📸 Auto-save unknown faces as image files

⚡ Live FPS display for performance monitoring

📁 Organized output: logs, unknown faces, and easy customization

📦 Requirements
To run the project, you need the following Python packages:

opencv-python

numpy

face_recognition

You can install them via:

pip install -r requirements.txt
Or install manually:

pip install opencv-python numpy face_recognition
For Windows users: make sure you use compatible versions and install via .whl files if needed (especially for dlib, which is a dependency of face_recognition).

🛠️ How It Works
Load known face image(s) and encode them using face_recognition.

Start capturing video from the webcam.

For each frame:

Detect face locations.

Encode the detected faces.

Compare them to known face encodings.

If a match is found:

Draw a bounding box and label with the person’s name.

Log attendance (if not already logged recently).

If no match:

Save the unknown face as an image.

Display the video feed with real-time annotations.

Exit the program by pressing the q key.

Run the program with:

python face_recognition.py
Make sure your known face image (e.g., photo (1).jpg) is in the same folder or update the path in the script.

📌 Notes
Make sure your webcam is connected and accessible.

Use high-resolution face images for better encoding accuracy.

You can expand the list of known faces by adding more images and encodings.

The system uses a 5-minute cooldown to avoid multiple entries for the same person within a short time.

💡 Future Improvements
Add a GUI with buttons for start/stop and add new face

Support for storing multiple known faces dynamically

Integration with a cloud database or online attendance dashboard

Audio greetings using text-to-speech (TTS)

Face registration from webcam

🙋‍♂️ Author
Arya Kant Pathak

Feel free to fork this project, suggest improvements, or use it in your own applications!
