import os
from PIL import Image

def list_dir(dir):
    return os.listdir(dir)

images = input("Enter file names: ").split("  ")
isReadDir = False
activeDirectory = ""

if images[0] == "dir":
    activeDirectory = images[1]
    images = list_dir(images[1])
    isReadDir = True

images_converted = images

def generate_path(path_for, use_cwd):
    if use_cwd == True:
        path_str = ""

        path_str += os.getcwd()

        path_str += '\\' + path_for
    else:
        path_str = ".\\" + path_for

    return path_str

output_file = generate_path(input("Enter output file name: "), False)

def convert_images(image_list):
    loop_count = 0
    result = []

    for current_image in image_list:
        loop_count = loop_count + 1

        if isReadDir:
            c_image = activeDirectory + "\\" + current_image

        # Opening image
        opened_image = Image.open(c_image)

        # Converted Image
        converted_image = opened_image.convert('RGB')

        if loop_count == len(image_list):
            result = result

            converted_image.save(activeDirectory + "\\" + output_file, save_all=True, append_images=result)
        else:
            result.append(converted_image)
        

# Converting
convert_images(images_converted)

print("Images converted successfully!")
