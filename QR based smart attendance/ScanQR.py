import cv2
import time
import sys
import base64
import pyzbar.pyzbar as pyz

# start web cam

cam = cv2.VideoCapture(0)
students=[]

# function for attendance file
f=open('attendance.txt','w+')
def enter(z):
    if z in students:
        pass
    else:
        students.append(z)
        z="".join(str(z))
        f.write(z+"\n")
        return students

# student attendance taken or not

def check(d):
    data=str(base64.b64decode(d).decode())
    if data in students:
        print("Already Present")
    else:
        print("Marked Present")
        enter(data)

# frame

while True:
    _,frame=cam.read()
    decodedobject=pyz.decode(frame)
    for obj in decodedobject:
        check(obj.data)
        time.sleep(1)

    cv2.imshow('Attendance Frame',frame)  # open camera frame

# close the other windows

    if cv2.waitKey(1)&0xff=='s':
        cv2.destroyAllWindows()
        break
f.close()
