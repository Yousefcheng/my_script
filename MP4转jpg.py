from cv2 import VideoCapture
from cv2 import imwrite
import os
import re
# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    imwrite(address, image)


if __name__ == '__main__':
    video_dir = r"C:\Users\cyf\Desktop\3"
    pic_dir = r"C:\Users\cyf\Desktop\3\pic"
    videos_list = [os.path.join(video_dir, video) for video in os.listdir(video_dir)]
    for video_path in videos_list:
        video_filename = os.path.basename(video_path).split("//")[-1]
        filename_num_t = re.findall("\d+\.?\d*", video_filename)
        video_filename_num=filename_num_t[0]
        out_path = pic_dir+str(video_filename_num)+'//'  # 保存图片路径+名字
        if not os.path.exists(out_path):
            os.makedirs(out_path)

        is_all_frame = True  # 是否取所有的帧
        sta_frame = 1  # 开始帧
        end_frame = 40  # 结束帧

        ######
        time_interval = 1  # 时间间隔

        # 读取视频文件
        videoCapture = VideoCapture(video_path)

        # 读帧
        success, frame = videoCapture.read()
        print(success)

        i = 0
        j = 0
        if is_all_frame:
            time_interval = 1

        while success:
            i = i + 1
            if (i % time_interval == 0):
                if is_all_frame == False:
                    if i >= sta_frame and i <= end_frame:
                        j = j + 1
                        print(video_filename+' save frame:', i)
                        save_image(frame, out_path, j)
                    elif i > end_frame:
                        break
                else:
                    j = j + 1
                    print(video_filename+' save frame:', i)
                    save_image(frame, out_path, j)

            success, frame = videoCapture.read()
