import os
import shutil
for i in  os.listdir(r'D:\Python\Assignment\data'):
   if i.endswith(".txt"):
      shutil.move(r'D:\Python\Assignment\Data'+'\\'+i,r'D:\Python\Assignment\txt'+'\\'+i)
   elif i.endswith(".jpg"):
      shutil.move(r'D:\Python\Assignment\Data'+'\\'+i,r'D:\Python\Assignment\image'+'\\'+i)
   elif i.endswith(".jpeg"):
      shutil.move(r'D:\Python\Assignment\Data'+'\\'+i,r'D:\Python\Assignment\image'+'\\'+i)
   elif i.endswith(".png"):
      shutil.move(r'D:\Python\Assignment\Data'+'\\'+i,r'D:\Python\Assignment\image'+'\\'+i)
      