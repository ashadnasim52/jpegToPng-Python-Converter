import sys
import os
from PIL import Image
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(f'Input Folder is {image_folder} \nOutput Folder is {output_folder}')
print(os.path.exists(output_folder))
if not os.path.exists(output_folder):
    # make new folder
    os.mkdirs(output_folder)
    print(os.path.exists(output_folder))

for file_name in os.listdir(image_folder):
    print(output_folder, file_name)
    img = Image.open(f'{image_folder}{file_name}')
    # img.show()
    clean_name = os.path.splitext(file_name)
    img.save(f'{output_folder}{clean_name[0]}.png', 'png')
print('All Done!')
