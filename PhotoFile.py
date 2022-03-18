import os
import random
from PIL import Image, ExifTags

class Photo():
    def __init__(self, fname, path):
        self.filename = fname
        self.path = path
        self.cnt = 0

    def createFileList(self):
        cnt = 0
        f = open(self.filename, 'a')
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".JPG") or file.endswith(".jpg"):
                    f.write(os.path.join(root, file) + '\n')
                    cnt += 1
        f.close()
        print(f"File count = {cnt}")
        self.cnt = cnt
        return cnt

    def getRandomPhoto(self):
        while(1):
            index = random.randint(1, self.cnt)
            print(f"random index number = {index}")
            with open(self.filename) as f:
                data = f.readlines()[index]
            length = len(data)
            print(data[0:length-1])
            image = Image.open(data[0:length-1])
            if image.width > image.height:
                print(f"filename is {data}")
                img = Image.open(data[0:length-1])
                img_exif = img.getexif()
                photo_date = "없음"
                if img_exif is None:
                    print('Sorry, image has no exif data.')
                else:
                    for key, val in img_exif.items():
                        if key == 0x0132:
                            photo_date = val
                return image, data[0:length-1], photo_date
        return None, 0, "없음"