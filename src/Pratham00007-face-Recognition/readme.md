# 🧠 Real-Time Face Recognition in Python

This project implements a real-time face recognition system using Python, OpenCV, and the `face_recognition` library. It captures video from a webcam, detects faces in each frame, and compares them against a set of known individuals to identify and label them.

## 📸 Features

- Detects faces from live webcam feed
- Compares detected faces with known encodings
- Displays bounding boxes and names for recognized individuals
- Supports multiple known faces
- Graceful exit with `'q'` key press

## 🛠 Requirements

- Python 3.x  
- OpenCV (`cv2`)  
- `face_recognition` library  
- Dlib (automatically installed with `face_recognition`)  
- Webcam

## 📦 Installation

```bash
pip install opencv-python face_recognition
```

> Note: You may need to install `cmake` and `dlib` separately depending on your system.

## 📁 Project Structure

```
face_recognition_project/
├── images/
│   ├── PR1.jpg
│   ├── PR2.jpg
│   └── PR3.jpg
├── face_recognition.py
└── README.md
```

## 🧑‍💻 How It Works

1. Loads known images and encodes faces.
2. Captures video frames from the webcam.
3. Detects faces and computes encodings for each.
4. Compares each detected face with known encodings.
5. Displays a red bounding box and name label if a match is found.

## 🧬 Known Faces

| Image File | Name       |
|------------|------------|
| PR1.jpg    | Amit       |
| PR2.jpg    | Rakesh     |
| PR3.jpg    | Pratyaksh  |

## 🏁 Running the Program

```bash
python face_recognition.py
```

Press `'q'` to quit the video stream.

## 🔮 Future Improvements

- Add dynamic face registration
- Support confidence scoring and tolerance adjustment
- Log recognition events to a `.roar` file
- Extend to video file input or multi-camera setups


