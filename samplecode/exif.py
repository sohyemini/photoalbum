import exifread

with open("/home/pi/media/Photo/Original/2012년/2012.12.23.베르사이유궁전/DSC02364.JPG", "rb") as f:
    tags = exifread.process_file(f)
    #print(tags)

print(tags["EXIF DateTimeDigitized"])

#####################################################
'''
from PIL import Image, ExifTags

img = Image.open("../CRW_3550.jpg")
img_exif = img.getexif()

if img_exif is None:
    print('Sorry, image has no exif data.')
else:
    for key, val in img_exif.items():
        if key == 0x0132:
            print(f'{ExifTags.TAGS[key]}:{val}')
'''