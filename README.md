# GestureX

Real-time sign language recognition. GestureX reads live webcam video, detects hand signs, and converts them into on-screen text and spoken audio.

> **Status:** work in progress. Hand tracking works; data collection, training and speech output are being built. See the [Roadmap](#roadmap).

## How it works

```
Webcam  →  MediaPipe  →  GestureX classifier  →  Text  →  Speech
(OpenCV)   (21 hand      (trained on our own     (on       (pyttsx3)
           landmarks)     recorded dataset)       screen)
```

1. **OpenCV** captures frames from the webcam.
2. **MediaPipe Hand Landmarker** (a pre-trained Google model) locates each hand and returns 21 landmarks per hand as x, y, z coordinates.
3. **Our classifier** takes those landmark coordinates and predicts which sign is being shown. It is trained on a dataset recorded for this project.
4. The prediction is shown as text and spoken aloud with **pyttsx3**.

Using landmarks instead of raw images keeps the model small, fast, and less sensitive to lighting and background.

## Features

- [x] Live hand tracking with a skeleton overlay (one or two hands)
- [ ] Data collection tool for recording labelled landmark samples
- [ ] Classifier training and evaluation (accuracy, confusion matrix)
- [ ] Live sign prediction from the webcam
- [ ] Text-to-speech output with debouncing (speak only when a sign is held)
- [ ] Support for motion-based signs (sequence model)
- [ ] Sentence building and a simple UI

## Project structure

```
GestureX/
├── src/
│   ├── step1_test.py        # Webcam + hand tracking sanity check
│   ├── collect_data.py      # Record labelled landmark samples
│   ├── train_model.py       # Train and save the classifier
│   ├── real_time.py         # Live recognition + speech
│   ├── utils.py             # Shared helpers
│   └── hand_landmarker.task # MediaPipe model file (see Setup)
├── dataset/                 # Recorded landmark data
├── models/                  # Trained models
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.13
- A webcam
- Windows (text-to-speech uses the system voices through `pyttsx3`)

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/<your-username>/GestureX.git
cd GestureX
```

**2. Create a virtual environment and install dependencies**

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**3. Download the MediaPipe hand model**

If `src/hand_landmarker.task` is not already in the repository, download it from:

```
https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task
```

and place it in the `src/` folder, keeping the file name exactly `hand_landmarker.task`.

**4. Check that everything works**

```bash
python src/step1_test.py
```

You should see your webcam feed with a skeleton drawn over your hand. Press `q` to quit.

## Usage

Run these from the project root. Scripts marked *(planned)* are not finished yet.

| Step | Command | What it does |
|------|---------|--------------|
| Test | `python src/step1_test.py` | Verifies webcam and hand tracking |
| Collect | `python src/collect_data.py` | Record samples for each sign *(planned)* |
| Train | `python src/train_model.py` | Train and save the classifier *(planned)* |
| Run | `python src/real_time.py` | Live recognition with text and speech *(planned)* |

## Supported signs

*To be decided.* The first version will focus on a small set of static signs (held hand shapes). Motion signs such as ASL "J" and "Z" need a sequence model and are planned for later.

## Roadmap

1. Hand tracking with MediaPipe (done)
2. Record a dataset of static signs (about 200 samples per sign)
3. Train a classifier and evaluate it
4. Live prediction with on-screen text
5. Speech output
6. Motion signs using sequences of frames (LSTM or 1D-CNN)
7. UI and sentence building

## Tech stack

| Purpose | Library |
|---------|---------|
| Video capture and drawing | OpenCV |
| Hand landmark detection | MediaPipe (Tasks API) |
| Data handling | NumPy, pandas |
| Classifier training and metrics | scikit-learn |
| Motion model (planned) | TensorFlow / Keras |
| Plots for evaluation | matplotlib |
| Text-to-speech | pyttsx3 |

## Notes

- This project uses the MediaPipe **Tasks** API (`HandLandmarker`). Recent MediaPipe versions removed the older `mp.solutions` interface, so older tutorials may not run unchanged.
- Install only one OpenCV package. `opencv-python` and `opencv-contrib-python` share the same `cv2` module and can break each other if both are installed.

## Acknowledgements

- [MediaPipe](https://ai.google.dev/edge/mediapipe) by Google for hand landmark detection (Apache 2.0 licence)
- [OpenCV](https://opencv.org/) for video processing

## Author

Gaurab Tandukar
