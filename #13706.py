import cv2 
import numpy as np





    #none = cv2.imread(frame1, 1)
t_image = cv2.imread("traffic.jpg")

t_image = cv2.medianBlur(t_image, 5)
t_hsv = cv2.cvtColor(t_image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(t_hsv)

circles = cv2.HoughCircles(v, cv2.HOUGH_GRADIENT, 1, 20, param1= 50, param2 = 50, minRadius= 0, maxRadius= 0)
    # 20 : 원끼리 최소 거리 50 : param1 = 원 중심 거리 100: param2 = CANNY EDGY 임계값(하한은 자동 절반 사용 50: 작을수록 원 많이 됨)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:

    cv2.circle(t_image, (i[0], i[1]), i[2], (0, 255, 0), 2) # x, y, r
    cr_img = v[i[1]-10 : i[1]+10, i[0]-10 : i[0]+10]
    img_str = 'x: {0}, y: {1}, mean : {2}'.format(i[0], i[1], cr_img.mean())
    print(img_str)
    #cv2.imshow('none', none)
cv2.imshow('t_image', t_image)
cv2.imshow("v", v)
cv2.waitKey(0)
cv2.destroyAllWindows()