### Add images types here (else, your label .txt file will be named for example image.png.txt) ###
def replace(name):
  
  name = name.replace(".jpg","")
  name = name.replace(".png","")
  name = name.replace(".jpeg","")
  return name
  
### Add images types here (else, your label .txt file will be named for example image.png.txt) ###
def replacetxt(name):
  
  name = name.replace(".jpg",".txt")
  name = name.replace(".png",".txt")
  name = name.replace(".jpeg",".txt")
  return name
  
