import cv2
import numpy as np

def disable_camera():
    camera = cv2.VideoCapture(0)  # 0 indicates the default camera (change if needed)

    if not camera.isOpened():
        print("Unable to access the camera.")
        return

    while True:
        ret, frame = camera.read()

        if ret:
            # Create a blank image of the same size as the camera 
            #frame
            blank_image = np.zeros_like(frame, dtype=np.uint8)
            cv2.imshow('Disabled Camera', blank_image)

            # Break the loop when any key is pressed
            if cv2.waitKey(1) != -1:
                break
        else:
            print("Failed to capture the camera frame.")
            break

    camera.release()
    cv2.destroyAllWindows()

def main():
    print("Disabling Camera Mode")
    print("Press any key to enable the camera.")
    input("Press Enter to continue...")

    disable_camera()

if _name_ == "_main_":
    main()