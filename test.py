'''import shutil, os
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
    print ('Format is not valid')'''

import shutil, os
filename = [input("Enter file name:")]
for files in filename:
  fileName,fileExtension = os.path.splitext(files)
  if fileExtension.endswith(".docx") or fileExtension.endswith(".pdf") or fileExtension.endswith(".doc"):

  #if fileExtension.endswith(".docx" or ".doc" or ".pdf"):
      print("This file is:", files)
      #print ('This file is:DOCX' and 'This file is PDF:' and 'This file is DOC:', files)
  elif  fileExtension.endswith(".json"):
    print ('This file is JSON:', files)
  else:
    print ('Format is not valid')