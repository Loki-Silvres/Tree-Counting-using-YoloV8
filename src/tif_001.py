import cv2 as cv 
from ultralytics import YOLO

def display(img, waitKey = 0):
    print(img.shape)
    res = cv.resize(img, (img.shape[0]//2, img.shape[1]//2))
    cv.imshow("res", res)
    cv.waitKey(waitKey)

img = cv.imread("/home/loki/tree_counting/src/runs/detect/predict8/Count_trees_in_this_file.tif", cv.IMREAD_UNCHANGED)
# cv.imwrite("/home/loki/tree_counting/Count_trees_in_this_file.png", img)
display(img)

# # Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# # Use the model
# model.train(data="coco8.yaml", epochs=3)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format