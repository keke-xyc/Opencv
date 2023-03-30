#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import time

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

import cv2 as cv  # opencv读取的格式是BGR
import matplotlib.pyplot as plt
import numpy as np

'''plt.show()
cv2.namedWindow('cat',cv2.WINDOW_NORMAL)
img = cv2.imread('cat.jpg',0)
cv2.imshow("cat", img)
cv2.waitKey(-1)
cv2.destroyAllWindows()'''
cap = cv.VideoCapture('test.mp4')
out = cv.VideoWriter('out.mp4',cv.VideoWriter_fourcc(*'MP4V '),20.0,(1024,680))
tim1 = time.time()
while(cap.isOpened()):
    # 一帧一帧捕捉
    ret, frametmp = cap.read()
    if(ret==True):
        frame = cv.resize(frametmp,(1024,680))
        out.write(frame)
        '''cv.imshow('frame', frame)
        if (cv.waitKey(10) & 0xFF == ord('q')) or (cv.waitKey(1) & 0xFF == 27):
            break'''
    else:
        break
# 当所有事完成，释放 VideoCapture 对象
cap.release()
out.release()
cv.destroyAllWindows()
tim2=time.time()
print(tim2-tim1)

