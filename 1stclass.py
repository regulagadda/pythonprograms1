'''filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))'''

import shutil, os
filename = [input("Enter file name:")]
for files in filename:
  filename, fileExtension = os.path.splitext(files)
  print(extention)

  if fileExtension.endswith(".pdf" or ".docx" or ".doc"):
    print ('This file is:', files)
  elif  fileExtension.endswith(".json"):
    print ('This file is:', files)
  else:
    print ('Format is not valid')