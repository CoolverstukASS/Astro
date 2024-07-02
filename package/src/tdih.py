from datasety import Datasety
from sortdf import sorted_dataset_by_times
import cv2
import numpy as np

def two_dimensional_illumination_histogram(number, pyt):
   df_result = Datasety(pyt)
   df_video_number = df_result[number]
   df_type_video_events = df_video_number[df_video_number['types_of_video'] == 'events']
   df_sorted_moments = sorted_dataset_by_times(df_type_video_events)
   im_path = df_sorted_moments['file_path'].tolist()

   path_str = str(im_path[number])
   img = cv2.imread(path_str)

   img = np.array(img)
   illuminat = np.zeros((len(img),len(img[0]), len(img[0][0])), dtype=int)

   for path in im_path:
      img = cv2.imread(path)
      img = np.array(img)
      for line in range(len(img)):
         for tupl in range(len(img[0])): 
            for pix in range(len(img[0][0])):
               if img[line][tupl][pix] != 0:
                  illuminat[line][tupl][pix] += 1
   return illuminat