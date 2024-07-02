from datasety import Datasety
from sortdf import sorted_dataset_by_times
import cv2

def average_displacement_vector(number, pyt):

    df_result = Datasety(pyt)
    df_video_number = df_result[number]
    df_type_video_events = df_video_number[df_video_number['types_of_video'] == 'events']
    df_sorted_moments = sorted_dataset_by_times(df_type_video_events)
    im_path = df_sorted_moments['file_path'].tolist()

    finalx = 0
    finaly = 0
    finalnumber = 0
    for path in im_path:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        maxim = 0
        mn = -1
        for l in range(len(contours)):
            if cv2.contourArea(contours[l]) > maxim:
                maxim = cv2.contourArea(contours[l])
                mn = 1
        maximum = contours[mn]
        x,y,w,h = cv2.boundingRect(maximum)
        cenx = (x+w)//2
        ceny = (y+h)//2
        img2 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        c,d = cv2.findContours(img2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        maxim3 = 0
        mn2 = -1
        for r in range(len(c)):
            if cv2.contourArea(c[r]) > maxim3:
                maxim3 = cv2.contourArea(c[r])
                mn2 = r
        maximum2 = c[mn2]
        p, q, o, j = cv2.boundingRect(maximum2)
        cenx2 = (p + o)// 2
        ceny2 = (q + j)// 2
        if(-51 < (cenx - cenx2) < 51) and (-51 < (ceny - ceny2) < 51):
            finalx += (cenx - cenx2)
            finaly += (ceny - ceny2)
            finalnumber +=1
    return finalx/finalnumber, finaly/finalnumber