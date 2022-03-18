import os
import datetime
import sqlite3
import random
from time import sleep

###########################################################################
# 파일 스캔 후, 텍스트 파일에 저장
now = datetime.datetime.now()
cnt = 0
f = open('./photolist', 'a')
for root, dirs, files in os.walk("/Volumes/Photo/Original"):
    for file in files:
        if file.endswith(".JPG") or file.endswith(".jpg"):
             #print(os.path.join(root, file))
             f.write(os.path.join(root, file) + '\n')
             cnt += 1
f.close()
print(f"File count = {cnt}")
end = datetime.datetime.now()


############################################################################
# 파일 스캔 후, 데이터베이스에 저장
now1 = datetime.datetime.now()
_con = sqlite3.connect("photo.db", detect_types=sqlite3.PARSE_DECLTYPES)
db = _con.cursor()
sql = "CREATE TABLE album (idx INTEGER PRIMARY KEY, name TEXT)"
db.execute(sql)
for root, dirs, files in os.walk("/Volumes/Photo/Original"):
    for file in files:
        if file.endswith(".JPG") or file.endswith(".jpg"):
             #print(os.path.join(root, file))
             sql = "INSERT INTO album (name) VALUES(?)"
             _con.execute(sql, (os.path.join(root, file),))


end1 = datetime.datetime.now()
print(f"[TextFile]File scan operation and make a file list took : {end-now}")
print(f"[DB]File scan operation and make a file list took : {end1-now1}")

sql = "select count(name) from album"
db.execute(sql)
rows = db.fetchall()
x = rows[0]
print(x[0])

#randint(a, b)
#randint 함수는 인자로 들어온 a, b 사이의 랜덤한 정수(int)를 반환합니다.
#반환하는 x는  a, b를 포함한 범위 입니다. (a <= N <= b)
#randrange 함수에 a, b+1을 넣은것과 동일하게 동작합니다.
for i in range(10):
    index = random.randint(1, int(x[0]))
    print(f"[{i}] [DB] random index number = {index}")
    sql = "select name from album where idx = ?"
    db.execute(sql, (index,))
    rows = db.fetchall()
    y = rows[0]
    print(f"filename is {y[0]}")
    sleep(3)


for i in range(10):
    index = random.randint(1, int(x[0]))
    print(f"[{i}] [Txt] random index number = {index}")
    with open("photolist") as f:
        data = f.readlines()[index]
    print(f"filename is {data}")
    sleep(3)