import openpyxl
import qrcode

wb=openpyxl.load_workbook('Student_names.xlsx')
s=wb.active

l=[]
for i in s.iter_cols(min_row=1,min_col=1,max_row=5,max_col=1):
    for c in i:
        ch=c.value.split("\n")
        l.append(ch[0])
        
for i in range(0,len(l)):
    img=qrcode.make(l[i])
    img.save("img %s.png"%(i+1)) 
    

    




