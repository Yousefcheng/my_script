# -*- coding: utf-8 -*-
from __future__ import division
from base64 import decode
import os
import xml.dom.minidom
import cv2
import sys
import numpy as np
# from imp import reload
# reload(sys)

def read_xml(ImgPath, AnnoPath, Savepath):
    imagelist = os.listdir(AnnoPath)
    for image in imagelist:
        image_pre, ext = os.path.splitext(image)
        # imgfile =  +'/'+ image_pre+ '.JPG'
        imgfile = os.path.join(ImgPath,image_pre+ '.jpg')
        # xmlfile = AnnoPath +'/'+ image_pre+ '.xml'
        xmlfile = os.path.join(AnnoPath, image_pre + '.xml')
        print(imgfile)
        print(xmlfile)
        
        
        f = open(xmlfile, "r")
        r = f.read()
        text = str(r.encode('utf-8'), encoding = "utf-8")
        #print(text)
        # 使用minidom解析器打开 XML 文档
        DomTree = xml.dom.minidom.parseString(text)

        
        # im = cv2.imread(imgfile)
        im = cv2.imdecode(np.fromfile(imgfile,dtype=np.uint8),cv2.IMREAD_UNCHANGED) #imdecode()读取图像数据并转换成图片格式
        #fromfile()读数据时需要用户指定元素类型，并对数组的形状进行适当的修改，cv2.IMREAD_UNCHANGED加载图像
        # DomTree = xml.dom.minidom.parse(xmlfile)  #读取xml文件中的值
        annotation = DomTree.documentElement #documentElement 属性可返回文档的根节点。
        filenamelist = annotation.getElementsByTagName('filename')#getElementById()可以访问Documnent中的某一特定元素，顾名思义，就是通过ID来取得元素，所以只能访问设置了ID的元素。
        filename = filenamelist[0].childNodes[0].data
        objectlist = annotation.getElementsByTagName('object')
        i = 1
        for objects in objectlist:
            namelist = objects.getElementsByTagName('name')
            objectname = namelist[0].childNodes[0].data #通过xml文件给图像加目标框
            bndbox = objects.getElementsByTagName('bndbox')
            for box in bndbox:
                try:
                    x1_list = box.getElementsByTagName('xmin')
                    x1 = int(x1_list[0].childNodes[0].data)

                    y1_list = box.getElementsByTagName('ymin')
                    y1 = int(y1_list[0].childNodes[0].data)

                    x2_list = box.getElementsByTagName('xmax')
                    x2 = int(x2_list[0].childNodes[0].data)

                    y2_list = box.getElementsByTagName('ymax')
                    y2 = int(y2_list[0].childNodes[0].data)

                    minX = x1
                    minY = y1
                    maxX = x2
                    maxY = y2
                    if(i % 3 == 0):
                        color = (128,0,0)
                    elif (i % 3 == 1):
                        color = (153, 51, 0)
                    elif (i % 3 == 2):
                        color = (255, 204, 0)
                    elif (i % 3 == 3):
                        color = (0, 51, 0)
                    elif (i % 9 == 4):
                        color = (51, 204, 204)
                    elif (i % 9 == 5):
                        color = (128, 0, 128)
                    elif (i % 9 == 6):
                        color = (0, 255, 255)
                    elif (i % 9 == 7):
                        color = (60, 179, 113)
                    elif (i % 9 == 8):
                        color = (255, 127, 80)
                    elif (i % 9 == 9):
                        color = (0, 255, 0)

                    cv2.rectangle(im,(minX,minY),(maxX,maxY),color,1)
                    if not os.path.exists(Savepath):
                        os.makedirs(Savepath)
                    path = os.path.join(Savepath, image_pre + '.jpg')
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    if objectname=='person':           
                        cv2.putText(im, ' ', (minX,minY - 7), font, 0.5, (255, 255, 0), 2)
                    else:
                        cv2.putText(im, objectname, (minX,minY - 7), font, 0.5, (255, 255, 0), 2)
                    cv2.imencode(".jpg",im)[1].tofile(path)
                    i += 1
                except Exception as e:
                    print(e)

if __name__ == "__main__":
    img_path = r'C:\Users\cyf\Desktop\3\pic3'
    xml_path = r'C:\Users\cyf\Desktop\3\xml'
    save_path = r'C:\Users\cyf\Desktop\3\res'
    read_xml(img_path, xml_path,save_path)

