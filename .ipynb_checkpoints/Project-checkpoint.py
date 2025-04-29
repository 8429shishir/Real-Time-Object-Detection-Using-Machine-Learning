from ultralytics import YOLO

# Load a pretrained YOLOv8 model
model = YOLO("yolov8n.pt")  # 'n' means nano model (lightweight)

# Run inference on an image
results = model("sample.jpg", show=True)  # Replace 'sample.jpg' with your image path
