import cv2
img = cv2.imread(r'C:\Users\cyf\Desktop\3\pic3\1.jpg')  #读取第一张图片
imgInfo = img.shape
size = (imgInfo[1],imgInfo[0])  #获取图片宽高度信息
print(size)

videoWrite = cv2.VideoWriter(r'C:\Users\cyf\Desktop\3\33.mp4',-1,30,size)    # 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））

for i in range(1,292):
    print(i)
    fileName = fr"C:\Users\cyf\Desktop\3\res\{str(i)}.jpg"
    img = cv2.imread(fileName)
    videoWrite.write(img)   # 将图片写入所创建的视频对象
print('end!')