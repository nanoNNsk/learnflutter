import cv2
import torch
import numpy as np
path='C:/Users/Lenovo/yolov5/yolov5s.pt'
model = torch.hub.load('ultralytics/yolov5','custom',path,force_reload=True)
cap=cv2.VideoCapture(0)
while True :
    ret,frame=cap.read()
    results=model(frame)
    frame=np.squeeze(results.render())
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1)&0xff==27:
        break
cap.release()
cv2.destroyAllWindows()
