# Annot-data-GUI

Simple app to annotate images for YOLOv4. Made in pygame.

Inspired and more compact version of https://github.com/proplayer2020/annot_data


# how to use
In command prompt :

```git clone https://github.com/proplayer2020/annot-data-GUI```

```python app.py```

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
