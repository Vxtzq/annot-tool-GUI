# Annot-data-GUI

Simple app to annotate data for YOLOv4. Made in pygame.

Inspired and more compact version of https://github.com/proplayer2020/annot_data

# How to install

This repository works with "darknet" YOLO, here is the link :

https://github.com/AlexeyAB/darknet

Clone it and compile it following instructions.

Useful links :

https://github.com/AlexeyAB/darknet#how-to-compile-on-linuxmacos-using-cmake

https://github.com/AlexeyAB/darknet#how-to-compile-on-windows-using-cmake

Then, in command prompt, enter :

```git clone https://github.com/proplayer2020/annot-tool-GUI```

```cd annot-tool-GUI```

```pip install -r requirements.txt```

```python download.py --both True``` to download yolo models

## Download useful files

It is possible to download yolov4 and yolov4-tiny models here, alternative to download.py:

Tiny YOLO : https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo-tiny/yolov4-tiny.conv.29

YOLO : https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo/yolov4.conv.137


# How to launch
## Windows

In command prompt :

```annotdataGUI.bat```

In file manager :

Simply click on "annotdataGUI.bat"

## Linux

In command prompt :

```chmod +x annotdataGUI.sh```

```./annotdataGUI.sh```

In file manager :

Go into the repository and go into the properties of "annotdataGUI.Appimage" file and tick "Allow Executing File As Program"

Then, simply click the .Appimage file, the app should open.

## Mac OS

In command prompt :

```chmod +x annotdataGUI.sh```

```sh annotdataGUI.sh```

# How to use :
See how to prepare your images here : https://github.com/proplayer2020/annot-tool-GUI/tree/main#dataset-types

Useful things : 

![demo](https://github.com/proplayer2020/annot-tool-GUI/assets/116555319/fd7f641b-554e-48d3-955d-41a36d41dbac)

Once annotation/marking is finished, click on "prepare data for training", and move the files (train.txt and test.txt) generated in the folder named "result" to build/darknet/data

# How to use generated files

After finishing the annotation, look into the "result" folder, all the files should be generated.
To train the model, Take the obj.data file, yolo model (yolo.conv.137 or yolo-tiny.conv.29) and the .cfg file corresponding to the model (if tiny yolo, use yolo-tiny-obj.cfg), and place those into darknet/data.

# Train
## Windows
Execute this command in the terminal, in the build/darknet/ folder :

Yolo : ```darknet.exe detector train data/obj.data data/yolo-obj.cfg data/yolo.conv.137```

Tiny yolo : ```darknet.exe detector train data/obj.data data/yolo-tiny-obj.cfg data/yolo-tiny.conv.29```
## Linux
Execute this command in the terminal, in the build/darknet/ folder :

Yolo : ```./darknet detector train data/obj.data data/yolo-obj.cfg data/yolov4.conv.137```

Tiny yolo : ```./darknet detector train data/obj.data data/yolo-tiny-obj.cfg data/yolov4-tiny.conv.29```

# Prepare dataset/images
## Dataset structures
Two dataset types are supported :

- Dataset with classes as folders (e.g. images/dataset/class1/img.png)
  
- Dataset with just images (e.g. images/img1.png
  
To deal with the second option, tick the corresponding option in the start settings and enter the classes names, one by one, into the last textbox.

## Supported images format
The python file "replaceformat.py" is used to replac image files like .jpg to .txt (bounding box data)

The current images format supported are : .jpg, .png, .jpeg, .JPG, .webp, .bmp and .heif.

It is easy to add images format by modifying "replaceformat.py"
  

A preview of all the classes should be appearing under it.

## Use a dataset located elsewhere on your computer
If the dataset used is somewhere else than in annot-data-GUI/images/*, it is possible to change its location
in the start settings, by entering the path of the dataset (e.g. /home/user/dataset/) or clicking on "Browse".


# Troubleshooting
## Error system
If an Error pops up when the app is oppened, it is possible to report it by clicking the text underneath.

Feel free to create an issue for problems/questions.
