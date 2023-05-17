import cv2
from yolov7 import YOLOv7

url = "rtsp://192.168.3.14:554/user=admin_password=Vokk1212*_channel=0_stream=0.sdp?real_stream"
model_path = "yolov7.onnx"
yolov7_detector = YOLOv7(model_path, conf_thres=0.3, iou_thres=0.2)
capture_width, capture_height = 1280, 720

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Failed to open RTSP stream")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, capture_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, capture_height)

ret, frame = cap.read()

if not ret:
    print("Failed to capture frame")
    exit()

cv2.imwrite('captured_image.jpg', frame)

captured_image = cv2.imread('captured_image.jpg')

boxes, scores, classes = yolov7_detector(captured_image)

combined_img = yolov7_detector.draw_detections(captured_image)

cv2.imwrite('detected_image.jpg', combined_img)

cv2.namedWindow('Detected Objects', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Detected Objects', 1280, 720)

cv2.imshow('Detected Objects', combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap.release()
