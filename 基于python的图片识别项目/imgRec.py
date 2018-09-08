# -*-coding:utf-8-*-
import os
import xlwt
from PIL import Image
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )



workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('ImageScan')
first_col=worksheet.col(0)       #xlwt中是行和列都是从0开始计算的
sec_col=worksheet.col(1)
first_col.width=320*20
sec_col.width=512*20
worksheet.write(0,0,label='企业注册号')
worksheet.write(0,1,label='企业名称')



rootdir = 'pic'
cato = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(cato)):
       path = os.path.join(rootdir,cato[i])
       if os.path.isfile(path):
           im = Image.open(path)
           x = 0
           y = 0
           w = 1000
           h = 235
           region = im.crop((x, y, x + w, y + h))
           tessdata_dir_config = '--tessdata-dir "Tesseract-OCR\\tessdata"'
           text = pytesseract.image_to_string(region, lang='chi_sim', config=tessdata_dir_config)
           list = text.split()
           #if str(list[2]).__len__()<18:
               #worksheet.write(i+1,0,label=str(list[2])+"1"+list[3])
           #else:
           worksheet.write(i + 1, 0, label=str(list[2]))
           if str(list[5]) != ":":
               worksheet.write(i + 1, 1, label=str(list[5]))
           else:
               worksheet.write(i + 1, 1, label=str(list[6]))
if os.path.exists('text.xls'):
   os.remove('text.xls')
workbook.save('text.xls')