import os
from PIL import Image, ImageFont, ImageDraw
from PIL import ImageFont
from PIL import ImageDraw 

qr_codes_folder = 'qr_codes'  # Path to the folder containing QR codes


img = Image.open('base.jpg') # The base image to overlay on


qr_new_size = (585, 640)  # Width, Height in pixels for qr resize


output_folder = 'tickets_folder'


#Define the position (top-left corner) where the overlay will be placed
position = (116, 130)  # Replace x and y with the desired coordinates

count = 0

for qr_code_filename in os.listdir(qr_codes_folder):
    count +=1

    qr_path = os.path.join(qr_codes_folder, qr_code_filename)

    qr_code_image = Image.open(qr_path).convert("RGBA")
    qr_code_image = qr_code_image.resize(qr_new_size)

    # Paste the overlay image onto the background
    img.paste(qr_code_image, position, qr_code_image)

    # Save the result or show it
    output_path = os.path.join(output_folder, 'output_image' + str(count) + ".jpg")

    img.save(output_path)




print("total files: ", count)




