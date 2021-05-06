import pytesseract  
import  numpy as np 
import cv2   
import os   
from PIL import Image

pics=[]
for items in os.listdir():
	if items == "main.py":
		pass
	else:
		pics.append(items)
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


try:
	f= open("contact.txt","w+")
	for i in pics:	
	    image=i

	    img = cv2.imread(image)
	    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
	    kernel = np.ones((1, 1), np.uint8)
	    img = cv2.dilate(img, kernel, iterations=1)
	    img = cv2.erode(img, kernel, iterations=1)
	    new_image = 'edited' + '_' + image  
	    cv2.imwrite(new_image, img)  
	    read = pytesseract.image_to_string(new_image)  
	    text=str(read)
	    # print(text)  
	    f.write(text)
	f.close()	    



except Exception as e:
    print('please provide proper name of the image')
    print(e)
List=[]
with open("contact.txt") as f:
	content=f.readlines()
for i in content:
	if i == "\n" or i == " \n" or i == "\x0c":
		pass
	else:
		List.append(i)

last=[]
for i in List:
	last.append(i.replace(" ","").replace("♀","").replace("\x0c",""))

Finished=[]
a=1
for i in last:
	if a==91:
		pass
	else:
		Finished.append(i)
	a +=1


Danny=[]
for i in Finished:
	Danny.append(i.replace("-",""))


f= open("new_contact.vcf","w+")
d=1
for i in Danny:
	f.write(f"BEGIN:VCARD\nVERSION:2.1\nN:{d};Contact {d};;;\nFN:Contact {d}\nTEL;CELL:{i}END:VCARD\n") #formate of vcf contats
	d +=1



