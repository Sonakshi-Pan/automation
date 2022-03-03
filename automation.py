import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    num=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)

    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imgName="pic"+ str(num) + ".png"
        cv2.imwrite(imgName,frame)
        start_time = time.time
        result = False

    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print("snapshot taken")    
    return imgName

def upload_file(imgName):
    access_token = 'sl.BDEkNcxq9qCeT5YPnpjEDesS3lxXo37vw4TGYExk2JUhCjx8SI_xmKFvk2oY3T8En0nFQhxE0N6QP4awqBOIjy2nAqAYZE9Alb-023wNT5RrIEf9CCL810QAWW4vYuoMp5ham0s'
  
    file_from = imgName
    file_to = "/newFolder1/"+ imgName 
  
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)  
        print("files uploaded successfully") 

def main():
    while(True):
        if((time.time()-start_time)>=300):
            snap=take_snapshot()
            upload_file(snap)

main()

