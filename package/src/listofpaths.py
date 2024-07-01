import glob
from pathlib import Path
def list_paths(data_path):
    memory = data_path/'**'
    pyt = []
    file_names = glob.glob(str(memory))
    for file_name in file_names:
        file_path = Path(file_name)
        pyt.append(file_path)
    return pyt