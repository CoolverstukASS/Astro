import pandas as pd
import findpict
from pathlib import Path
def Datasety(pyt):
  
    dataframes = []
    for proc in pyt:
        types_of_video = []
        image_names = []
        moments = []
        file_paths = []
        nazvania = []
        times = []
        file_names = findpict.poisk_png(proc)
        for file_name in file_names:
            file_path = Path(file_name)
            name = file_path.stem
            if '_' in name:
                name_parts = name.split('_')
            elif '-' in name:
                name_parts = name.split('-')
            else:
                print('AAAAAAAAAAAAA!!!!!')
            nazvanie = file_path.parents[2].stem
            type_of_video = file_path.parents[0].stem
            image_name = name
            moment = name_parts[1]
            time = str(moment[1:])
            
            file_paths.append(file_path)
            image_names.append(image_name)
            moments.append(moment)
            types_of_video.append(type_of_video)
            nazvania.append(nazvanie)
            times.append(time)

        df = pd.DataFrame({
            'image_name': image_names,
            'file_path': file_paths,
            'types_of_video': types_of_video,
            'moments': moments,
            'nazvania': nazvania,
            'times' :times
        })
        dataframes.append(df)
    return dataframes