import os
import sys
import cv2
import torch
from datetime import datetime
from ultralytics import YOLO
import easyocr
import re

# Check if CUDA is available
if not torch.cuda.is_available():
    print("CUDA is not available. Exiting...")
    sys.exit(1)

# Forcefully use the NVIDIA GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # Specify GPU ID (if you have multiple GPUs)

# Define paths
model_path = os.path.join("model", "best.pt")
video_path = os.path.join("model", "Sample Video.mp4")

# Load the YOLO model and EasyOCR reader
model = YOLO(model_path)
reader = easyocr.Reader(["en"], gpu=True, verbose=False)

# Initialize video capture
cap = cv2.VideoCapture(video_path)

vehicle_passed = {}
line_position_80 = int(0.8 * cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
line_position_90 = int(0.9 * cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


def send_to_server(plate_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Detected and sent: Plate={plate_text}, Time={timestamp}")


def is_valid_plate(plate_text):
    return bool(re.match(r"^[A-Za-z0-9]{5,10}$", plate_text))


def predict_boxes(model, frame):
    bbox = []
    results = model.predict(
        frame, device="cuda", verbose=False
    )  # Use GPU for prediction
    for res in results:
        boxes = res.boxes
        for box in boxes:
            xmin, ymin, xmax, ymax = box.xyxy.tolist()[0]
            bbox.append([int(xmin), int(ymin), int(xmax), int(ymax)])
    return bbox


def read_plate(reader, image):
    results = reader.readtext(image)
    return "".join([res[1] for res in results]).replace(" ", "")


def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to make the text stand out
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Reduce noise using Gaussian blur
    denoised = cv2.GaussianBlur(thresh, (5, 5), 0)

    # Enhance contrast by scaling pixel values
    enhanced = cv2.convertScaleAbs(denoised, alpha=1.5, beta=0)

    return enhanced


def process_frame(frame):
    bbox = predict_boxes(model, frame)

    for x_min, y_min, x_max, y_max in bbox:
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        vehicle_center_y = (y_min + y_max) / 2
        if vehicle_center_y > line_position_80:
            cropped_img = frame[y_min:y_max, x_min:x_max]
            processed_img = preprocess_image(cropped_img)
            plate_text = read_plate(reader, processed_img)

            if (
                plate_text
                and is_valid_plate(plate_text)
                and plate_text not in vehicle_passed
            ):
                send_to_server(plate_text)
                vehicle_passed[plate_text] = True

            if vehicle_center_y > line_position_90 and plate_text in vehicle_passed:
                del vehicle_passed[plate_text]

    cv2.line(
        frame, (0, line_position_80), (frame.shape[1], line_position_80), (0, 0, 255), 2
    )
    cv2.line(
        frame, (0, line_position_90), (frame.shape[1], line_position_90), (0, 0, 255), 2
    )
    cv2.imshow("Live Detection", frame)


# Main loop
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    if cap.get(cv2.CAP_PROP_POS_FRAMES) % 3 == 0:
        process_frame(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
