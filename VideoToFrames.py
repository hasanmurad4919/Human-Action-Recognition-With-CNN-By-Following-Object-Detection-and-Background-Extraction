import os
import numpy as np
import cv2
from glob import glob
# **********************DISCLAIMER************************
# Step 1 : make a folder and keep the code file here;
# Step 2 : create 2 folders inside the same folder;
# Step 3 : rename them one folder name = videos and another =  save;
# Step 4 : put the videos on videos folder and run the code;
#****************************end*****************************
a=1
def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_path, save_dir, gap=10):
    global a
    print(a,"Number video is processing")
    a+=1
    b=1
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    #create_dir(save_path)
    #print(save_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break

        if idx == 0:
            cv2.imwrite(f"{save_path}"+"_"+str(b)+'.png', frame)
            b+=1
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{save_path}"+"_"+str(b)+'.png', frame)
                b+=1

        idx += 1

if __name__ == "__main__":
    video_paths = glob("videos/*")
    save_dir = "save"

    for path in video_paths:

        save_frame(path, save_dir, gap=3)