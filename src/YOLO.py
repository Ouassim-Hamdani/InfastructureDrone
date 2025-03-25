from ultralytics import YOLO
from ultralytics.utils.ops import non_max_suppression
import os
import numpy as np
import cv2
class DroneAi:
    """Drone Ai Model Class for Trained YOLO"""
    def __init__(self):
        self.model = YOLO(os.path.join("..","models","detector.pt"))
        self.class_colors = {0:(0,255,0),1:(255,0,0)} # GREEN RED
        self.classes = {0:"Light Switch",1:"Socket"}

    def predict(self,img,return_img=False,iou=0.5,conf=0.4):
        """Predict function of Model
        INPUT :
        img : NumPY Array / Filepath string
        return_img : boolean to determien whetehr to return image with boxes on it of predicitons, or return YOLO BOXES results
        iou : iou metric for NMS Applied directly on YOLO Output
        conf : boxes to filter regarding a conf threshhold
        
        RETURNS : 
        NumPy array of processed image
        or 
        YOLO Boxes Output Class
        """
        self.check_input(img)
        results = self.model.predict(img,iou,conf=conf)
        for result in results:
            if not return_img:
                return result
            else:
                boxes = result.boxes
                return self.drawBoxes(img,boxes)
    def drawBoxes(self,img, boxes):
        """
        Draws YOLO Output Boxes on img
        INPUT :
        img : str path of image / NumPy Array
        boxes : YOLO Output boxes
        
        RETURNS :
        processed image with boxes on.
        """
        self.check_input(img)
        if isinstance(img,str):
            img = cv2.imread(img)
        for box, conf, cls in zip(boxes.xyxy, boxes.conf, boxes.cls):
            x1, y1, x2, y2 = map(int, box)
            color = self.class_colors[int(cls)]
            tag = self.class_colors[int(cls)]
            label = f"{tag}: {conf:.2f}"

            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return img
    
    def check_input(self,img):
        """Checks input of img if its valid (NumPy or String)"""
        if not isinstance(img,(np.ndarray,str)):
            raise ValueError("Please provide a numpy image or a string filepath")

if __name__=="__main__":
    model = DroneAi()
    print(model.predict(os.path.join("..","data","test.jpg"),return_img=True))