import os
from PIL import Image

def list_dir(dir):
    return os.listdir(dir)

s_images = input("Enter file names: ").split("  ")

print(s_images)

images = s_images

if images[0] == "dir":
    images = list_dir(images[1])

    # Dir images array
    d_images = ['dir']

    for image in images:
        d_images.append(image)

    images = d_images

images_converted = []

def generate_path(path_for, use_cwd):
    if use_cwd == True:
        path_str = ""

        path_str += os.getcwd()

        path_str += '\\' + path_for
    else:
        path_str = ".\\" + path_for

    return path_str


output_file = generate_path(input("Enter output file name: "), False)

for _image in images:
    d_image = images[1] + "\\" + _image
    # Generating exact path
    if images[0] != "dir":
        current_image = generate_path(_image)
    elif images[0] == "dir":
        current_image = s_images[1] + "\\" + image

    print(current_image)

    # Opening image
    opened_image = Image.open(current_image)

    # Converted Image
    converted_image = opened_image.convert('RGB')

    images_converted.append(converted_image)

    converted_image.save(s_images[1] + "\\" + output_file, save_all=True, append_images=images_converted)


print("Images converted successfully!")
