
import pydicom

A = pydicom.dcmread("bmode.dcm")
print(A)

B  = pydicom.dcmread("ttfm.dcm")
print(B)

f1= open("bmode.txt","w")
f2= open("ttfm.txt","w")

str1 = str(A)
str2 = str(B)

f1.write(str1)
f2.write(str2)



f1.close()
f2.close()


