import matplotlib.pyplot as plt
from datasety import Datasety
from sortdf import sorted_dataset_by_times
import cv2
import numpy as np

def center_large_area(number, pyt):

   df_result = Datasety(pyt)
   df_video_number = df_result[number]
   df_type_video_events = df_video_number[df_video_number['types_of_video'] == 'events']
   df_sorted_moments = sorted_dataset_by_times(df_type_video_events)
   im_path = df_sorted_moments['file_path'].tolist()
   cX = []
   cY = []
   
   for path in im_path:
      img = cv2.imread(path)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      ret, gray = cv2.threshold(gray, 10, 255,0)
      contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
      largest_area = sorted(contours, key=cv2.contourArea)[-1]
      mask = np.zeros(img.shape, np.uint8)
      yg = cv2.drawContours(mask, [largest_area], 0, (255,255,255,255), -1)
      canny_edges = cv2.Canny(yg, 10, 255, 0)
      M = cv2.moments(canny_edges)
      cX.append(int(M["m10"] / M["m00"]))
      cY.append(int(M["m01"] / M["m00"]))
   kadr = np.linspace(0, len(im_path)-1, len(im_path))
   plt.figure(figsize=(6.29, 3.24), dpi=300)  
   plt.plot(kadr, cX, color='red', linewidth=2)  
   plt.plot(kadr, cY, color='blue', linewidth=2)  
   plt.xlabel('Кадр')  
   plt.ylabel('Изменение центра области по координатам') 
   plt.title('Изменение центра области по кадрам')  
   plt.xlim(min(kadr), max(kadr))  
   plt.legend(['Координата Х', 'Координата Y'], loc='upper right')  
   plt.show()