import shutil, os
filename = [input("Enter file name:")]
for files in filename:
  fileName,fileExtension = os.path.splitext(files)

  if fileExtension.endswith(".docx"):
    print ('This file is DOCX:', files)
  elif  fileExtension.endswith(".json"):
    print ('This file is JSON:', files)
  elif fileExtension.endswith(".doc"):
    print("This file is DOC:", files)
  elif fileExtension.endswith(".pdf"):
    print("This file is PDF:", files)
  else:
    print ('Format is not valid')