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


# How to make it work
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

Once the app is opened, enter settings (optional) and click "OK".

Useful buttons : 

![demo](https://github.com/proplayer2020/annot-tool-GUI/assets/116555319/851947ff-0e9d-4caf-a255-a869a6ee4c90)

Once annotation/marking is finished, click on "prepare data for training", and move the files (train.txt and test.txt) generated in the folder named "result" to build/darknet/data

Then follow instructions here : 

YOLOv4:

https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

YOLOv4-tiny:

https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects

# Dataset types
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

# Troubleshooting
If an Error pops up when the app is oppened, it is possible to report it by clicking the text underneath.

Feel free to create an issue for problems/questions.

## Use a dataset that isn't in the folder named "images" of this repo
If the used dataset is somewhere else than in annot-data-GUI/images/*, it is possible to change its location
in the start settings, by entering the path of the dataset (e.g. /home/user/dataset/)

