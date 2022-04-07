'''import shutil, os
filename = [input("Enter file name:")]
for files in filename:
  fileName,fileExtension = os.path.splitext(files)
  if fileExtension.endswith(".docx" or ".doc" or ".pdf"):
     print('This file is:', files)
        #S3url = os.environ['S3_URL'] + channel_name + '/' + file['name']
    elif fileExtension == ".json":
      print('This file is:', files)

      #S3url = os.environ['S3_JOBS_URL'] + channel_name + '/' + file['name']
   else:
    print("Format is not valid")'''

import shutil, os
filename = [input("Enter file name:")]
for files in filename:
  fileName,fileExtension = os.path.splitext(files)
  if fileExtension.endswith(".docx" or ".doc" or ".pdf"):
    print ('This file is:', files)
    print("fileExtension")

  elif  fileExtension.endswith(".json"):
    print ('This file is:', files)
  else:
    print ('Format is not valid')