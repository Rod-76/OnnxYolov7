import cv2
from yolov7 import YOLOv7
import time

url = "rtsp://192.168.3.14:554/user=admin_password=Vokk1212*_channel=0_stream=0.sdp?real_stream"
width, height = 720, 480
model_path = "yolov7.onnx"
yolov7_detector = YOLOv7(model_path, conf_thres=0.3, iou_thres=0.2)


cap = cv2.VideoCapture(url)
fps_start_time = time.time()
fps_counter = 0


while True:
    ret, frame = cap.read()

    if ret:
        
        frame = cv2.resize(frame,(width, height)) 
        
        boxes, scores, class_ids = yolov7_detector(frame)
        
        combined_img = yolov7_detector.draw_detections(frame)
        
        fps_counter += 1 
        fps_text = "FPS: {:.2f}".format(fps_counter / (time.time() - fps_start_time))
        cv2.putText(combined_img, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('Detected Objects', combined_img)
        
        fps_counter += 1

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
    if time.time() - fps_start_time >= 1:
        fps_start_time = time.time()
        fps_counter = 0
    


cap.release()
cv2.destroyAllWindows()
