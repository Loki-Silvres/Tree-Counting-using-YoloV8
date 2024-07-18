from ultralytics import YOLO
import cv2 as cv

model = YOLO('yolov8n.yaml').load('yolov8l.pt')
results = model.train(data="/home/loki/tree_counting/config/config.yaml", epochs=50)
results = model.val()
# model.export()