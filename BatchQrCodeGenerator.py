import easygui
import pandas as pd
import pyqrcode
import png
from pyqrcode import QRCode
import re

print("Select input file")
filename = easygui.fileopenbox()
data = pd.read_excel(filename)

for index,row in data.iterrows():
    #fix each of the data points

    #for the names, remove whitespace, convert to all lowercase, and remove nicknames
    row['Last Name:'] = re.sub("[\(\[].*?[\)\]]", "", row['Last Name:'].replace(" ", "").replace("’","'").lower())
    row['First Name:'] = re.sub("[\(\[].*?[\)\]]", "", row['First Name:'].replace(" ", "").replace("’","'").lower())
    row['Grade:'] = re.search(r'\d+', row['Grade:']).group()

    qrname = row['Last Name:'] + ',' + row['First Name:'] + "," + row['Grade:']
    print(qrname)
    url = pyqrcode.create(qrname)
    url.png("output\\" + qrname + ".png", scale=6)

data.to_excel("FixedFile.xlsx")