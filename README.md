Air Canvas - Hand Gesture Drawing Application
Overview
Air Canvas is a Python-based application that allows users to draw on a virtual canvas using hand gestures captured through a webcam. Leveraging the power of MediaPipe for hand tracking and OpenCV for image processing, this app provides an intuitive interface for gesture-based drawing.

Features
Gesture Recognition: Detects hand landmarks and recognizes pinch gestures to enable drawing.
Real-time Drawing: Draw lines on a virtual canvas using hand movements.
Webcam Feed Integration: Displays the webcam feed alongside the virtual canvas for seamless interaction.
Streamlit Interface: Deploy the app easily online with a user-friendly interface.
How It Works
Hand Detection: Uses MediaPipe to detect hand landmarks in real-time.
Gesture Detection: Identifies specific gestures (like pinch) to start drawing.
Drawing on Canvas: Draws lines on the canvas as you move your hand while pinching.
Web Integration: Streamlit provides a simple way to run the app in a web environment.
Installation
To run this project locally, follow these steps:

1. Clone the Repository:
bash
Copy code
git clone https://github.com/P-Sreeshanth/air-canvas.git
cd air-canvas
2. Install Dependencies:
Ensure you have Python 3.8+ installed. Then, install the required packages:

bash
Copy code
pip install -r requirements.txt
3. Run the Application:
bash
Copy code
streamlit run ac.py
Requirements
Python 3.8+
OpenCV
MediaPipe
Streamlit
Streamlit-WebRTC
Contributing
If you want to contribute to this project:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-branch
Make your changes and commit:
bash
Copy code
git commit -m 'Add new feature'
Push to the branch:
bash
Copy code
git push origin feature-branch
Open a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
MediaPipe for their robust hand tracking solution.
OpenCV for image processing functionalities.
Streamlit for providing an easy-to-deploy platform.
