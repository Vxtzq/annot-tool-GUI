import os

### Modify this (with absolute paths) ###

YOLO_TINY = False

TRAIN_LOC = "result/train.txt"
TEST_LOC = "result/test.txt"
NAMES = "result/obj.names"
BACKUP_LOC = "result/backup/"

if YOLO_TINY == False:
    WEIGHTS_LOC = "result/yolov4.weights"
    CFG_LOC = "result/yolo-obj.cfg"
else:
    WEIGHTS_LOC = "result/yolov4-tiny.weights"
    CFG_LOC = "result/yolo-tiny-obj.cfg"

### Do not modify this ###

TRAIN_LOC = os.path.abspath(TRAIN_LOC)
TEST_LOC = os.path.abspath(TEST_LOC)
NAMES = os.path.abspath(NAMES)
BACKUP_LOC = os.path.abspath(BACKUP_LOC)
WEIGHTS_LOC = os.path.abspath(WEIGHTS_LOC)
