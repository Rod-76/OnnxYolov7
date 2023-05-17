import cv2

url = "rtsp://192.168.3.14:554/user=admin_password=Vokk1212*_channel=0_stream=0.sdp?real_stream"

# Create a VideoCapture object using the RTSP URL
cap = cv2.VideoCapture(url)

# Check if the VideoCapture object is opened successfully
if not cap.isOpened():
    print("Failed to open RTSP stream")
    exit()

# Read a frame from the IP camera
ret, frame = cap.read()

# Check if a frame was successfully read
if not ret:
    print("Failed to capture frame")
    exit()

# Save the captured image to disk
cv2.imwrite('captured_image.jpg', frame)

# Read the saved image using OpenCV
captured_image = cv2.imread('captured_image.jpg')

# Resize the window
cv2.namedWindow('Captured Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Captured Image', 720, 480)

# Display the captured image
cv2.imshow('Captured Image', captured_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Release the VideoCapture and close any open windows
cap.release()
