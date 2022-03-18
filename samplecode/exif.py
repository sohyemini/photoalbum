import exifread

with open("../CRW_3550.jpg", "rb") as f:
    tags = exifread.process_file(f)
    print(tags)

print(tags["EXIF DateTimeDigitized"])

#####################################################

from PIL import Image, ExifTags

img = Image.open("../CRW_3550.jpg")
img_exif = img.getexif()

if img_exif is None:
    print('Sorry, image has no exif data.')
else:
    for key, val in img_exif.items():
        if key == 0x0132:
            print(f'{ExifTags.TAGS[key]}:{val}')
