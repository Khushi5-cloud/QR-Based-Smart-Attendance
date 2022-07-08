


from MyQR import myqr   # for generating QR code
import os
import base64          # for encoding and decoding the string
 
# open the text file and read it
f = open('Names.txt','r') # r is to read the file text
lines = f.read().split("\n") # read the text line by line

for i in range(0,len(lines)):
    data=lines[i].encode()
    name=base64.b64encode(data).decode()
    version,level,qr_name=myqr.run(
    str(name),
    version=1,
    level='H',
    # background
    picture=None,
    colorized=False,
    contrast=1.0,
    brightness=1.0,

    save_name=str(lines[i] + '.bmp'), # .bmp is for storing the file in jpg format
    save_dir=os.getcwd() #save the file in current file 'cwd'= current working directory
)
