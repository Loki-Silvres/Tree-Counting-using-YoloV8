import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolov8n.yaml').load('/home/loki/tree_counting/src/runs/detect/train15/weights/best.pt')
results = model.predict(source = "/home/loki/tree_counting/Count_trees_in_this_file.tif", conf = 0.1, imgsz=640, max_det = 10000, iou=0.8, show=True, show_conf = False, save = True, show_labels= False, save_txt = True)
# breakpoint()
