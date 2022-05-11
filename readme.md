This project focuses on improving the Human Action Recognition problem, which we found, action can not be effectively detected due to several background elements.
As a result, we developed a method that included background subtraction and object detection as a preprocessing strategy. We used a CNN model to train the frames after preprocessing. We were able to improve the accuracy of the previous model by using this strategy.


According to the project, this is an improvement on the publication "Human action recognition with 3D convolutional neural network." Like the paper, we used the UCF50 dataset.

To run this project follow these steps:

1.You need to run the BackgroundSubtraction.py file first to subtract the background of each class video.Follow the folder creation rules mentioned at the top of the py file. We have implemented the MaskRCNN model to substract the background. We also implemented the PixelLib framework for subtraction.    
   You may need to install some packages like pixellib, imgaug, etc to run this file.
2.Run the VideoToFrames.py file to get the frames from the subtracted videos.Follow the folder creation rules mentioned at the top of the py file.
3.Run the CNN Implementation.ipynb file to train the images you got earlier. Create folders for each of the class images separately and train the model. Also, update the file paths on your own. You will get a h5 and a pickle file after running this file.
  You may need to install some packages like tensorflow, keras, openCV, etc to run this file.
4.Finally, run the final output. ipynb file to show the output.You will need the previous h5 and pickle files to run this file. Also, you need a new video that you want to classify.  



The Links you may need:
1.https://pixellib.readthedocs.io/en/latest/
2.https://pixellib.readthedocs.io/en/latest/change_video_bg.html
3.https://pyimagesearch.com/2019/07/15/video-classification-with-keras-and-deep-learning/


Reference paper:
https://ieeexplore.ieee.org/document/8285700
T. Lima, B. Fernandes and P. Barros, "Human action recognition with 3D convolutional neural network," 2017 IEEE Latin American Conference on Computational Intelligence (LA-CCI), 2017, pp. 1-6, doi: 10.1109/LA-CCI.2017.8285700.
