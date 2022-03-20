import os
import sys
import random
from PIL import Image, ExifTags
import exifread

class Photo():
    def __init__(self, fname, path):
        self.filename = fname
        self.path = path
        self.cnt = 100

    def createFileList(self):
        cnt = 0
        f = open(self.filename, 'a')
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".JPG") or file.endswith(".jpg"):
                    txt = os.path.join(root, file)
                    if "@eaDir" in txt:
                        ...
                    else:
                        print(os.path.join(root, file))
                        f.write(os.path.join(root, file) + '\n')
                        cnt += 1
        f.close()
        print(f"File count = {cnt}")
        self.cnt = cnt
        return cnt

    def getRandomPhoto(self):
        cnt = 0
        while(1):
            cnt += 1
            index = random.randint(1, self.cnt)
            print(f"random index number = {index}")
            with open(self.filename) as f:
                data = f.readlines()[index]
            length = len(data)
            if os.path.exists(data[0:length-1]):
                image = Image.open(data[0:length-1])
                if image.width > image.height:
                    print(data[0:length-1])
                    photo_date = self.getPhotoDate(data[0:length-1])
                    return image, data[0:length-1], photo_date
            #if cnt > 100: break

        return None, 0, "없음"


    def getPhotoDate(self, fname):
        if sys.platform.startswith('win'):
            image = Image.open(fname)
            photo_date = "없음"
            img_exif = image.getexif()
            if img_exif is None:
                print('Sorry, image has no exif data.')
            else:
                for key, val in img_exif.items():
                    if key == 0x0132:
                        return val

            return "No date"
        elif sys.platform.startswith('linux'): # or sys.platform.startswith('cygwin'):
            print(sys.platform.title)
            with open(fname, "rb") as f:
                tags = exifread.process_file(f)
                #print(tags)
            ret = tags.get("EXIF DateTimeDigitized")
            if ret: return tags["EXIF DateTimeDigitized"]
            else : return "No date"
        else:
            return "No date"