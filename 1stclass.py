'''filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))'''

# bird names list
bird_names = ("Parrot", "Owl", "Pigeon", "Crow", "Peacock", "Hen")
bird_names = [name.lower() for name in bird_names]

# bird guess
bird_guess = input("Enter a bird name (Guess 1): ")

# nested conditions starts here
if bird_guess.lower() in bird_names:
#if bird_guess.lower() in bird_names.lower():
  print("Yes, 1st try!")
else:
  bird_guess = input("Enter a bird name (Guess 2): ")
  if bird_guess.lower() in bird_names:
  #if bird_guess.lower() in bird_names.lower():
    print("Yes, 2nd try!")
  else:
    bird_guess = input("Enter a bird name (Guess 3): ")
    if bird_guess.lower() in bird_names:
      print("Yes, 3rd try!")
    else:
      print("Sorry, out of tries.")

