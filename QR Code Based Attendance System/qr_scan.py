import cv2
import pyzbar.pyzbar as py


camera =cv2.VideoCapture(0) 
l=[]

while True:
    _,frame=camera.read()
    decoded=py.decode(frame)
    for i in decoded:
        n=i.data.decode('utf-8')
        if n in l:
            print("Already marked")
            cv2.putText(frame,text='Already Marked',org=(50,50),fontScale=1, fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,0,0),thickness=2,bottomLeftOrigin=cv2.LINE_AA)
        else:
            l.append(n)
            file=open("Present_names.txt","w")
            file.write(n)
            file.close()
            cv2.putText(frame,text='Marked',org=(50,50),fontScale=1, fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,0,0),thickness=2,bottomLeftOrigin=cv2.LINE_4)
            print("Marked")

    cv2.imshow("Scan your Attendance",frame)
    key=cv2.waitKey(1)
    if key == 27:
        break




