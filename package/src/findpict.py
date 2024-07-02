import glob2
def poisk_png(directory):
    astro_mask = directory /  '**' / '*.png'
    file_names = glob2.glob(str(astro_mask))
    return file_names