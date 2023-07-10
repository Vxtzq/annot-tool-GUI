
# Annot-data-GUI

Simple app to annotate data for YOLOv4. Made in pygame.

Inspired and more compact version of https://github.com/proplayer2020/annot_data


# Setup Darknet YOLO
To use with this repo :

https://github.com/AlexeyAB/darknet

Clone it, then compile it following instructions.

Useful links :

https://github.com/AlexeyAB/darknet#how-to-compile-on-linuxmacos-using-cmake

https://github.com/AlexeyAB/darknet#how-to-compile-on-windows-using-cmake

# Setup this repository

In command prompt, enter :

```git clone https://github.com/proplayer2020/annot-data-GUI```

```pip install -r requirements.txt```


# Open the app
## Windows

#### In command prompt :

```chmod +x annotdataGUI.sh```

```bash annotdataGUI.sh```

Then follow instructions on the screen.

Once annotation/marking is finished, click on "prepare data for training", and move the files (train.txt and test.txt) generated in the folder named "result" to build/darknet/data

Then follow instructions here : 

YOLOv4:

https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

YOLOv4-tiny:

https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects

## Linux

#### In command prompt :

```chmod +x annotdataGUI.sh```

```./annotdataGUI.sh```

#### In file manager :

Go into the repository and go into properties of the .Appimage file and tick "Allow Executing File As Program"

Then, simply click the .Appimage file, the app should open.

Enter the right settings and start annotating

Once annotation/marking is finished, click on "prepare data for training", and move the files (train.txt and test.txt) generated in the folder named "result" to build/darknet/data

Then follow instructions here : 

YOLOv4:

https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

YOLOv4-tiny:

https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects

## Mac OS

#### In command prompt :

```chmod +x annotdataGUI.sh```

```sh annotdataGUI.sh```

Then follow instructions on the screen.

Once annotation/marking is finished, click on "prepare data for training", and move the files (train.txt and test.txt) generated in the folder named "result" to build/darknet/data

Then follow instructions here : 

YOLOv4:

https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

YOLOv4-tiny:

https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects







# Dataset types
Two dataset types are supported :

- Dataset with classes as folders (e.g. images/dataset/class1/img.png)
  
- Dataset with just images (e.g. images/img1.png
  
To deal with the second option, tick the corresponding option in the start settings and enter the classes names, one by one, into the last textbox.

A preview of all the classes should be appearing under it.

# Troubleshooting
If an Error pops up when the app is oppened, it is possible to report it by clicking the text underneath.

Feel free to create an issue for problems/questions.

## Use a dataset that isn't in the folder named "images" of this repo
If the used dataset is somewhere else than in annot-data-GUI/images/*, it is possible to change its location
in the start settings, by entering the path of the dataset (e.g. /home/user/dataset/)

