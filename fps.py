import cv2
import time


width, height = 640, 480



cap = cv2.VideoCapture(0)
fps_start_time = time.time()
fps_counter = 0


while True:
    ret, frame = cap.read()

    if ret:
        
        frame = cv2.resize(frame,(width, height)) 
        
        fps_counter += 1 
        fps_text = "FPS: {:.2f}".format(fps_counter / (time.time() - fps_start_time))
        cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('Detected Objects', frame)
        
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
