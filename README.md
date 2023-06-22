# Annot-data-GUI

Simple app to annotate images for YOLOv4. Made in pygame.

Inspired and more compact version of https://github.com/proplayer2020/annot_data


# how to use
To use with this repo :

https://github.com/AlexeyAB/darknet

Follow instructions to clone it, build it.

Once finished execute those commands :

In command prompt :

```git clone https://github.com/proplayer2020/annot-data-GUI```

```python app.py```

Once annotation/marking is finished, click on "prepare data for training", and put the two files (train.txt and test.txt) generated in the result folder into build/darknet/data

Then follow instructions here : 

YOLOv4:

https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

YOLOv4-tiny:

https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects

# Troubleshooting
If an Error pops up when the app is oppened, it is possible to report it by clicking the text underneath.

# Dataset types
Two dataset types are supported :

- Dataset with classes as folders (e.g. images/dataset/class1/img.png)
  
- Dataset with just images (e.g. images/img1.png
  
To deal with the second option, tick the corresponding option in the start settings and enter the classes names, one by one, into the last textbox.
A preview of all the classes should be appearing under it.

## Use dataset that isn't in the "images" folder of this repo
In the start settings, enter the path of the dataset (e.g. /home/user/dataset/)
