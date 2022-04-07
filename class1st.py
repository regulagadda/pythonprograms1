import os
filename = [input("Enter file name:")]
for files in filename:
  fileName,fileExtension = os.path.splitext(files)

  #fileName,fileExtension = os.path.splitext(files)
  if fileExtension.endswith('.docx' or '.doc' or '.pdf'):
    print ('This file is:', files)
  elif  fileExtension.endswith('.json'):
    print ('This file is:', files)
  else:
    print ('Format is not valid')
import os
listdir =[]
path = "c://media"
movies = []
songs = []
for x in os:
  if x.endswith(".mp4"):
    movies.append(x)
    if x.endswith(".mp3"):
      songs.append(x)
      print("movies")
      print("songs")