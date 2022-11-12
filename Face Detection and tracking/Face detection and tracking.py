import cv2 
import os

# initialise folder_named = dataset
dataset = "dataset"  

# create sub_folder
name = "champ" 


# Creating the respective folder created 
path = os.path.join(dataset,name) 
if not os.path.isdir(path) : # check availability of path
    os.makedirs(path) 


# initialise specific height, width required
(width,height) = (130,100) 

# Initialising & importing haar_cascade_frontalFace_algorithm
haar_cascade = cv2.CascadeClassifier('C:\\Users\\harit\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

# Initialise camers
cam = cv2.VideoCapture(0)

count = 1
while count < 31:
    print(count)
    _,img = cam.read()   # gettng camera frame
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # gray-scale conversion
    face = haar_cascade.detectMultiScale(grayImg,1.3,4) # passing algorithm
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
        faceOnly = grayImg[y:y+h,x:x+w]
        resizeImg = cv2.resize(faceOnly,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),faceOnly)
        count += 1
    
    cv2.imshow("FaceDetection",img) # display image
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Image captured sucessfully")
    
cam.release()
cv2.destroyAllWindows()
