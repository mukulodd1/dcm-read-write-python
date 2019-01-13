# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pydicom

A = pydicom.dcmread("bmode.dcm")
print(A)

B  = pydicom.dcmread("ttfm.dcm")
print(B)


pydicom.filewriter.write_file("bmode.txt", A , write_like_original=True)
pydicom.filewriter.write_file("ttfm.txt", B , write_like_original=True)

