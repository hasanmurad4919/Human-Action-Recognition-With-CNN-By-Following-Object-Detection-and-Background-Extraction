# **********************DISCLAIMER************************
# Step 1 : make a folder and keep the code file here;
# Step 2 : create 2 folders inside the same folder;
# Step 3 : rename them one folder name = videos and another =  save, create another folder videos inside this save folder;
# Step 4 : put the videos on the first videos folder and run the code;
# Step 5 : run this file and you will find the ouput videos inside save-->videos folder.
#****************************end*****************************




import tensorflow
import pixellib
from pixellib.instance import instance_segmentation
import cv2
import numpy as np
import os
from glob import glob
from pixellib.tune_bg import alter_bg
print("hello")

path = 'mask_rcnn_coco.h5'

segmentation_model = instance_segmentation()
segmentation_model.load_model(path)



#seg=segmentation_model
print("middle")

video_paths = glob("videos/*")
save_dir = "save"

for path in video_paths:
    name = path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    #save="output"+str(idx)
    change_bg = alter_bg(model_type = "pb")
    change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
    change_bg.color_video(path, colors =  (0, 0, 0), frames_per_second=30, output_video_name=f"{save_path}.mp4" )



print("ended")
