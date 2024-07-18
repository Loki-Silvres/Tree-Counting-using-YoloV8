from ultralytics import YOLO
import cv2 as cv

model = YOLO('yolov8n.yaml').load('yolov8n.pt')
results = model.train(data="/home/loki/tree_counting/config/config.yaml", epochs=50, degrees = 20, shear=20, flipud=0.5,crop_fraction=0.9, lr0=0.001)
results = model.val()
# model.export()