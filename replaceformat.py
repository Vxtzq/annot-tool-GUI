### Add images types here (else, your label .txt file will be named for example image.png.txt) ###
def replace(name):
  
  name = name.replace(".jpg","")
  name = name.replace(".png","")
  name = name.replace(".jpeg","")
  name = name.replace(".JPG","")
  name = name.replace(".webp","")
  name = name.replace(".bmp","")
  name = name.replace(".heif","")
  name = name.replace(".heic","")
  return name
  
### Add images types here (else, your label .txt file will be named for example image.png.txt) ###
def replacetxt(name):
  
  name = name.replace(".jpg",".txt")
  name = name.replace(".png",".txt")
  name = name.replace(".jpeg",".txt")
  name = name.replace(".JPG",".txt")
  name = name.replace(".webp",".txt")
  name = name.replace(".bmp",".txt")
  name = name.replace(".heif",".txt")
  name = name.replace(".heic","")
  return name
  
