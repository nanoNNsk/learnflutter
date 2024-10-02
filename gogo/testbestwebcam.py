import torch
import cv2

# โหลดโมเดลที่เทรนเสร็จแล้ว
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Lenovo/yolov5/best.pt',force_reload=True)

# เปิดกล้องเว็บแคม (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

while True:
    # อ่านเฟรมจากกล้อง
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame")
        break

    # ทำการตรวจจับวัตถุ
    results = model(frame)

    # วาดผลลัพธ์ลงบนเฟรม
    for *box, conf, cls in results.xyxy[0]:
        cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 2)
        label = f'{model.names[int(cls)]} {conf:.2f}'
        cv2.putText(frame, label, (int(box[0]), int(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # แสดงเฟรม
    cv2.imshow('YOLOv5 Webcam', frame)

    # กด 'q' เพื่อออกจาก loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปล่อยทรัพยากร
cap.release()
cv2.destroyAllWindows()