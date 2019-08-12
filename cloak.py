import cv2
import numpy as np

def main():
    
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    #uncomment these lines and line 42 if u want to record video
    '''
    codecc = cv2.VideoWriter_fourcc(*'XVID')
    fileNamae = "video.mp4"
    frame_rate = 13
    resolution = (640, 480)
    output = cv2.VideoWriter(fileNamae, codecc, frame_rate, resolution)
    '''


    if cap.isOpened():
        for i in range(30):
            ret, frame1 = cap.read()
    else:
        ret = False
    frame1 = np.flip(frame1, axis = 1)
    
    while ret:
        ret, frame = cap.read()
        ret,frame = cap.read()
        frame = np.flip(frame, axis = 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #blue
        low = np.array([100, 100, 10])
        high = np.array([140, 255, 255])
        img_mask = cv2.inRange(hsv, low, high)
        
        img_mask1 = cv2.bitwise_not(img_mask)
        rem1 = cv2.bitwise_and(frame, frame, mask = img_mask1)
        rem2 = cv2.bitwise_and(frame1, frame1, mask = img_mask)
        final_output = cv2.addWeighted(rem1,1,rem2,1,0)

        
        cv2.imshow("windowX", final_output)
        #output.write(final_output)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()
    cap.release()

if __name__ == "__main__":
    main()