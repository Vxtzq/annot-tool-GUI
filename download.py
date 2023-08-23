import argparse
from glob import glob
import urllib.request


parser = argparse.ArgumentParser()
parser.add_argument("--tiny", help="if you want to download yolo tiny model")

parser.add_argument("--both", help="if you want to download both yolo and tiny yolo model")
args = parser.parse_args()

exist = 0

error = 0

existtiny = 0
for file in glob('result/*'):
    if file != "result/yolov4-tiny.conv.29":
        
        if file != "result/yolov4.conv.137":
            pass
        else:
            
            exist = 1
    else:
        
        existtiny = 1

if args.both == "True":
    if existtiny == 1 or exist == 1:
        print("Yolo models already exists, aborting... Check result folder")
        error = 1
    else:
        print("downloading tiny yolo model (19MB)...")
        urllib.request.urlretrieve('https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo-tiny/yolov4-tiny.conv.29', "result/yolov4-tiny.conv.29")
        print("downloading yolo model (170MB)...")
        urllib.request.urlretrieve('https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo/yolov4.conv.137', "result/yolov4.conv.137")
else:
    
    if args.tiny == "True":
        if existtiny == 1:
            print("Tiny yolo model already exists, aborting... Check result folder")
            error = 1
        else:
            print("downloading tiny yolo model (19MB)...")
            urllib.request.urlretrieve('https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo-tiny/yolov4-tiny.conv.29', "result/yolov4-tiny.conv.29")
    else:
        
        if exist == 1:
            print("Tiny yolo model already exists, aborting... Check result folder")
            error = 1
        else:
            print("downloading yolo model (170MB)...")
            urllib.request.urlretrieve('https://github.com/proplayer2020/annot-tool-GUI/releases/download/yolo/yolov4.conv.137', "result/yolov4.conv.137")
if error == 0:
    print("Complete.")
else:
    print("Complete with Errors.")
